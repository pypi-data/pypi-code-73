import os
import sys
import copy
import ctypes
import cffi # lmao
import threading
import itertools
import pkg_resources
import logging
import pyvex
import claripy
import time
import binascii
import archinfo

from ..sim_options import UNICORN_HANDLE_TRANSMIT_SYSCALL
from ..errors import SimValueError, SimUnicornUnsupport, SimSegfaultError, SimMemoryError, SimMemoryMissingError, SimUnicornError
from .plugin import SimStatePlugin
from ..misc.testing import is_testing

l = logging.getLogger(name=__name__)
ffi = cffi.FFI()

try:
    import unicorn
except ImportError:
    l.warning("Unicorn is not installed. Support disabled.")
    unicorn = None

class MEM_PATCH(ctypes.Structure): # mem_update_t
    pass

MEM_PATCH._fields_ = [
        ('address', ctypes.c_uint64),
        ('length', ctypes.c_uint64),
        ('next', ctypes.POINTER(MEM_PATCH))
    ]

class TRANSMIT_RECORD(ctypes.Structure): # transmit_record_t
    pass

TRANSMIT_RECORD._fields_ = [
        ('data', ctypes.c_void_p),
        ('count', ctypes.c_uint32)
    ]

class TaintEntityEnum: # taint_entity_enum_t
    TAINT_ENTITY_REG = 0
    TAINT_ENTITY_TMP = 1
    TAINT_ENTITY_MEM = 2
    TAINT_ENTITY_NONE = 3

class MemoryValue(ctypes.Structure): # memory_value_t
    _MAX_MEM_ACCESS_SIZE = 8

    _fields_ = [
        ('address', ctypes.c_uint64),
        ('value', ctypes.c_uint8 * _MAX_MEM_ACCESS_SIZE),
        ('size', ctypes.c_uint64)
    ]

class RegisterValue(ctypes.Structure): # register_value_t
    _MAX_REGISTER_BYTE_SIZE = 32

    _fields_ = [
        ('offset', ctypes.c_uint64),
        ('value', ctypes.c_uint8 * _MAX_REGISTER_BYTE_SIZE)
    ]
class InstrDetails(ctypes.Structure): # instr_details_t
    _fields_ = [
        ('instr_addr', ctypes.c_uint64),
        ('has_memory_dep', ctypes.c_bool),
        ('memory_values', ctypes.POINTER(MemoryValue)),
        ('memory_values_count', ctypes.c_uint64),
    ]

class BlockDetails(ctypes.Structure): # block_details_ret_t
    _fields_ = [
        ('block_addr', ctypes.c_uint64),
        ('block_size', ctypes.c_uint64),
        ('symbolic_instrs', ctypes.POINTER(InstrDetails)),
        ('symbolic_instrs_count', ctypes.c_uint64),
        ('register_values', ctypes.POINTER(RegisterValue)),
        ('register_values_count', ctypes.c_uint64),
    ]

class STOP:  # stop_t
    STOP_NORMAL         = 0
    STOP_STOPPOINT      = 1
    STOP_ERROR          = 2
    STOP_SYSCALL        = 3
    STOP_EXECNONE       = 4
    STOP_ZEROPAGE       = 5
    STOP_NOSTART        = 6
    STOP_SEGFAULT       = 7
    STOP_ZERO_DIV       = 8
    STOP_NODECODE       = 9
    STOP_HLT            = 10
    STOP_VEX_LIFT_FAILED        = 11
    STOP_SYMBOLIC_CONDITION     = 12
    STOP_SYMBOLIC_PC            = 13
    STOP_SYMBOLIC_READ_ADDR     = 14
    STOP_SYMBOLIC_READ_SYMBOLIC_TRACKING_DISABLED = 15
    STOP_SYMBOLIC_WRITE_ADDR    = 16
    STOP_SYMBOLIC_BLOCK_EXIT_CONDITION = 17
    STOP_SYMBOLIC_BLOCK_EXIT_TARGET = 18
    STOP_UNSUPPORTED_STMT_PUTI    = 19
    STOP_UNSUPPORTED_STMT_STOREG  = 20
    STOP_UNSUPPORTED_STMT_LOADG   = 21
    STOP_UNSUPPORTED_STMT_CAS     = 22
    STOP_UNSUPPORTED_STMT_LLSC    = 23
    STOP_UNSUPPORTED_STMT_DIRTY   = 24
    STOP_UNSUPPORTED_EXPR_GETI    = 25
    STOP_UNSUPPORTED_STMT_UNKNOWN = 26
    STOP_UNSUPPORTED_EXPR_UNKNOWN = 27
    STOP_UNKNOWN_MEMORY_WRITE     = 28
    STOP_SYMBOLIC_MEM_DEP_NOT_LIVE = 29

    stop_message = {}
    stop_message[STOP_NORMAL]        = "Reached maximum steps"
    stop_message[STOP_STOPPOINT]     = "Hit a stop point"
    stop_message[STOP_ERROR]         = "Something wrong"
    stop_message[STOP_SYSCALL]       = "Unable to handle syscall"
    stop_message[STOP_EXECNONE]      = "Fetching empty page"
    stop_message[STOP_ZEROPAGE]      = "Accessing zero page"
    stop_message[STOP_NOSTART]       = "Failed to start"
    stop_message[STOP_SEGFAULT]      = "Permissions or mapping error"
    stop_message[STOP_ZERO_DIV]      = "Divide by zero"
    stop_message[STOP_NODECODE]      = "Instruction decoding error"
    stop_message[STOP_HLT]           = "hlt instruction encountered"
    stop_message[STOP_VEX_LIFT_FAILED]       = "Failed to lift block to VEX"
    stop_message[STOP_SYMBOLIC_CONDITION]    = "Symbolic condition for ITE"
    stop_message[STOP_SYMBOLIC_PC]           = "Instruction pointer became symbolic"
    stop_message[STOP_SYMBOLIC_READ_ADDR]    = "Attempted to read from symbolic address"
    stop_message[STOP_SYMBOLIC_READ_SYMBOLIC_TRACKING_DISABLED]= "Attempted to read symbolic data from memory but symbolic tracking is disabled"
    stop_message[STOP_SYMBOLIC_WRITE_ADDR]   = "Attempted to write to symbolic address"
    stop_message[STOP_SYMBOLIC_BLOCK_EXIT_CONDITION] = "Guard condition of block's exit statement is symbolic"
    stop_message[STOP_SYMBOLIC_BLOCK_EXIT_TARGET] = "Target of default exit of block is symbolic"
    stop_message[STOP_UNSUPPORTED_STMT_PUTI]   = "Symbolic taint propagation for PutI statement not yet supported"
    stop_message[STOP_UNSUPPORTED_STMT_STOREG] = "Symbolic taint propagation for StoreG statement not yet supported"
    stop_message[STOP_UNSUPPORTED_STMT_LOADG]  = "Symbolic taint propagation for LoadG statement not yet supported"
    stop_message[STOP_UNSUPPORTED_STMT_CAS]    = "Symbolic taint propagation for CAS statement not yet supported"
    stop_message[STOP_UNSUPPORTED_STMT_LLSC]   = "Symbolic taint propagation for LLSC statement not yet supported"
    stop_message[STOP_UNSUPPORTED_STMT_DIRTY]  = "Symbolic taint propagation for Dirty statement not yet supported"
    stop_message[STOP_UNSUPPORTED_EXPR_GETI]   = "Symbolic taint propagation for GetI expression not yet supported"
    stop_message[STOP_UNSUPPORTED_STMT_UNKNOWN]= "Canoo propagate symbolic taint for unsupported VEX statement type"
    stop_message[STOP_UNSUPPORTED_EXPR_UNKNOWN]= "Cannot propagate symbolic taint for unsupported VEX expression"
    stop_message[STOP_UNKNOWN_MEMORY_WRITE]    = "Cannot find a memory write at instruction; likely because unicorn reported PC value incorrectly"
    stop_message[STOP_SYMBOLIC_MEM_DEP_NOT_LIVE] = "A symbolic memory dependency on stack is no longer in scope"

    symbolic_stop_reasons = [STOP_SYMBOLIC_CONDITION, STOP_SYMBOLIC_PC, STOP_SYMBOLIC_READ_ADDR,
        STOP_SYMBOLIC_READ_SYMBOLIC_TRACKING_DISABLED, STOP_SYMBOLIC_WRITE_ADDR,
        STOP_SYMBOLIC_BLOCK_EXIT_CONDITION, STOP_SYMBOLIC_BLOCK_EXIT_TARGET]

    unsupported_reasons = [STOP_UNSUPPORTED_STMT_PUTI, STOP_UNSUPPORTED_STMT_STOREG, STOP_UNSUPPORTED_STMT_LOADG,
        STOP_UNSUPPORTED_STMT_CAS, STOP_UNSUPPORTED_STMT_LLSC, STOP_UNSUPPORTED_STMT_DIRTY,
        STOP_UNSUPPORTED_STMT_UNKNOWN, STOP_UNSUPPORTED_EXPR_UNKNOWN, STOP_VEX_LIFT_FAILED]

    @staticmethod
    def name_stop(num):
        for item in dir(STOP):
            if item.startswith('STOP_') and getattr(STOP, item) == num:
                return item
        raise ValueError(num)

    @staticmethod
    def get_stop_msg(stop_reason):
        if stop_reason in STOP.stop_message:
            return STOP.stop_message[stop_reason]

        return "Unknown stop reason"

class StopDetails(ctypes.Structure):
    _fields_ = [
        ('stop_reason', ctypes.c_int),
        ('block_addr', ctypes.c_uint64),
        ('block_size', ctypes.c_uint64),
    ]

#
# Memory mapping errors - only used internally
#

class MemoryMappingError(Exception):
    pass

class AccessingZeroPageError(MemoryMappingError):
    pass

class FetchingZeroPageError(MemoryMappingError):
    pass

class SegfaultError(MemoryMappingError):
    pass

class MixedPermissonsError(MemoryMappingError):
    pass

#
# This annotation is added to constraints that Unicorn generates in aggressive concretization mode
#

class AggressiveConcretizationAnnotation(claripy.SimplificationAvoidanceAnnotation):
    def __init__(self, addr):
        claripy.SimplificationAvoidanceAnnotation.__init__(self)
        self.unicorn_start_addr = addr

#
# Because Unicorn leaks like crazy, we use one Uc object per thread...
#

_unicounter = itertools.count()

class Uniwrapper(unicorn.Uc if unicorn is not None else object):
    # pylint: disable=non-parent-init-called
    def __init__(self, arch, cache_key, thumb=False):
        l.debug("Creating unicorn state!")
        self.arch = arch
        self.cache_key = cache_key
        self.wrapped_mapped = set()
        self.wrapped_hooks = set()
        self.id = None
        if thumb:
            uc_mode = arch.uc_mode_thumb
        else:
            uc_mode = arch.uc_mode
        unicorn.Uc.__init__(self, arch.uc_arch, uc_mode)

    def hook_add(self, htype, callback, user_data=None, begin=1, end=0, arg1=0):
        h = unicorn.Uc.hook_add(self, htype, callback, user_data=user_data, begin=begin, end=end, arg1=arg1)
        #l.debug("Hook: %s,%s -> %s", htype, callback.__name__, h)
        self.wrapped_hooks.add(h)
        return h

    def hook_del(self, h):
        #l.debug("Clearing hook %s", h)
        h = unicorn.Uc.hook_del(self, h)
        self.wrapped_hooks.discard(h)
        return h

    def mem_map(self, addr, size, perms=7):
        #l.debug("Mapping %d bytes at %#x", size, addr)
        m = unicorn.Uc.mem_map(self, addr, size, perms=perms)
        self.wrapped_mapped.add((addr, size))
        return m

    def mem_map_ptr(self, addr, size, perms, ptr):
        m = unicorn.Uc.mem_map_ptr(self, addr, size, perms, ptr)
        self.wrapped_mapped.add((addr, size))
        return m

    def mem_unmap(self, addr, size):
        #l.debug("Unmapping %d bytes at %#x", size, addr)
        m = unicorn.Uc.mem_unmap(self, addr, size)
        self.wrapped_mapped.discard((addr, size))
        return m

    def mem_reset(self):
        #l.debug("Resetting memory.")
        for addr,size in self.wrapped_mapped:
            #l.debug("Unmapping %d bytes at %#x", size, addr)
            unicorn.Uc.mem_unmap(self, addr, size)
        self.wrapped_mapped.clear()

    def hook_reset(self):
        #l.debug("Resetting hooks.")
        for h in self.wrapped_hooks:
            #l.debug("Clearing hook %s", h)
            unicorn.Uc.hook_del(self, h)
        self.wrapped_hooks.clear()

    def reset(self):
        self.mem_reset()
        #self.hook_reset()
        #l.debug("Reset complete.")

_unicorn_tls = threading.local()
_unicorn_tls.uc = None

class _VexCacheInfo(ctypes.Structure):
    _fields_ = [
        ("num_levels", ctypes.c_uint),
        ("num_caches", ctypes.c_uint),
        ("caches", ctypes.c_void_p),
        ("icaches_maintain_coherence", ctypes.c_bool),
    ]

class _VexArchInfo(ctypes.Structure):
    _fields_ = [
        ("hwcaps", ctypes.c_uint),
        ("endness", ctypes.c_int),
        ("hwcache_info", _VexCacheInfo),
        ("ppc_icache_line_szB", ctypes.c_int),
        ("ppc_dcbz_szB", ctypes.c_uint),
        ("ppc_dcbzl_szB", ctypes.c_uint),
        ("arm64_dMinLine_lg2_szB", ctypes.c_uint),
        ("arm64_iMinLine_lg2_szB", ctypes.c_uint),
        ("x86_cr0", ctypes.c_uint),
    ]

def _load_native():
    if sys.platform == 'darwin':
        libfile = 'angr_native.dylib'
    elif sys.platform in ('win32', 'cygwin'):
        libfile = 'angr_native.dll'
    else:
        libfile = 'angr_native.so'

    try:
        angr_path = pkg_resources.resource_filename('angr', os.path.join('lib', libfile))
        h = ctypes.CDLL(angr_path)

        VexArch = ctypes.c_int
        uc_err = ctypes.c_int
        state_t = ctypes.c_void_p
        stop_t = ctypes.c_int
        uc_engine_t = ctypes.c_void_p

        def _setup_prototype(handle, func, restype, *argtypes):
            realname = 'simunicorn_' + func
            _setup_prototype_explicit(handle, realname, restype, *argtypes)
            setattr(handle, func, getattr(handle, realname))

        def _setup_prototype_explicit(handle, func, restype, *argtypes):
            getattr(handle, func).restype = restype
            getattr(handle, func).argtypes = argtypes

        #_setup_prototype_explicit(h, 'logSetLogLevel', None, ctypes.c_uint64)
        _setup_prototype(h, 'alloc', state_t, uc_engine_t, ctypes.c_uint64)
        _setup_prototype(h, 'dealloc', None, state_t)
        _setup_prototype(h, 'hook', None, state_t)
        _setup_prototype(h, 'unhook', None, state_t)
        _setup_prototype(h, 'start', uc_err, state_t, ctypes.c_uint64, ctypes.c_uint64)
        _setup_prototype(h, 'stop', None, state_t, stop_t)
        _setup_prototype(h, 'sync', ctypes.POINTER(MEM_PATCH), state_t)
        _setup_prototype(h, 'bbl_addrs', ctypes.POINTER(ctypes.c_uint64), state_t)
        _setup_prototype(h, 'stack_pointers', ctypes.POINTER(ctypes.c_uint64), state_t)
        _setup_prototype(h, 'bbl_addr_count', ctypes.c_uint64, state_t)
        _setup_prototype(h, 'syscall_count', ctypes.c_uint64, state_t)
        _setup_prototype(h, 'step', ctypes.c_uint64, state_t)
        _setup_prototype(h, 'activate_page', None, state_t, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_void_p)
        _setup_prototype(h, 'set_stops', None, state_t, ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint64))
        _setup_prototype(h, 'cache_page', ctypes.c_bool, state_t, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_char_p, ctypes.c_uint64)
        _setup_prototype(h, 'uncache_pages_touching_region', None, state_t, ctypes.c_uint64, ctypes.c_uint64)
        _setup_prototype(h, 'clear_page_cache', None, state_t)
        _setup_prototype(h, 'enable_symbolic_reg_tracking', None, state_t, VexArch, _VexArchInfo)
        _setup_prototype(h, 'disable_symbolic_reg_tracking', None, state_t)
        _setup_prototype(h, 'symbolic_register_data', None, state_t, ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint64))
        _setup_prototype(h, 'get_symbolic_registers', ctypes.c_uint64, state_t, ctypes.POINTER(ctypes.c_uint64))
        _setup_prototype(h, 'is_interrupt_handled', ctypes.c_bool, state_t)
        _setup_prototype(h, 'set_transmit_sysno', None, state_t, ctypes.c_uint32, ctypes.c_uint64)
        _setup_prototype(h, 'process_transmit', ctypes.POINTER(TRANSMIT_RECORD), state_t, ctypes.c_uint32)
        _setup_prototype(h, 'set_tracking', None, state_t, ctypes.c_bool, ctypes.c_bool)
        _setup_prototype(h, 'executed_pages', ctypes.c_uint64, state_t)
        _setup_prototype(h, 'in_cache', ctypes.c_bool, state_t, ctypes.c_uint64)
        _setup_prototype(h, 'set_map_callback', None, state_t, unicorn.unicorn.UC_HOOK_MEM_INVALID_CB)
        _setup_prototype(h, 'set_vex_to_unicorn_reg_mappings', None, state_t, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.c_uint64)
        _setup_prototype(h, 'set_vex_sub_reg_to_reg_mappings', None, state_t, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.c_uint64)
        _setup_prototype(h, 'set_vex_offset_to_register_size_mapping', None, state_t, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.c_uint64)
        _setup_prototype(h, 'set_artificial_registers', None, state_t, ctypes.POINTER(ctypes.c_uint64), ctypes.c_uint64)
        _setup_prototype(h, 'get_count_of_blocks_with_symbolic_instrs', ctypes.c_uint64, state_t)
        _setup_prototype(h, 'get_details_of_blocks_with_symbolic_instrs', None, state_t, ctypes.POINTER(BlockDetails))
        _setup_prototype(h, 'get_stop_details', StopDetails, state_t)
        _setup_prototype(h, 'set_register_blacklist', None, state_t, ctypes.POINTER(ctypes.c_uint64), ctypes.c_uint64)
        _setup_prototype(h, 'set_cpu_flags_details', None, state_t, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.c_uint64)
        _setup_prototype(h, 'set_unicorn_flags_register_id', None, state_t, ctypes.c_int64)

        l.info('native plugin is enabled')

        return h
    except (OSError, AttributeError) as e:
        l.warning('failed loading "%s", unicorn support disabled (%s)', libfile, e)
        raise ImportError("Unable to import native SimUnicorn support") from e

try:
    _UC_NATIVE = _load_native()
    #_UC_NATIVE.logSetLogLevel(2)
except ImportError:
    _UC_NATIVE = None


class Unicorn(SimStatePlugin):
    '''
    setup the unicorn engine for a state
    '''

    UC_CONFIG = {} # config cache for each arch

    def __init__(
        self,
        syscall_hooks=None,
        cache_key=None,
        unicount=None,
        symbolic_var_counts=None,
        symbolic_inst_counts=None,
        concretized_asts=None,
        always_concretize=None,
        never_concretize=None,
        concretize_at=None,
        concretization_threshold_memory=None,
        concretization_threshold_registers=None,
        concretization_threshold_instruction=None,
        cooldown_symbolic_stop=2,
        cooldown_unsupported_stop=2,
        cooldown_nonunicorn_blocks=100,
        cooldown_stop_point=1,
        max_steps=1000000,
    ):
        """
        Initializes the Unicorn plugin for angr. This plugin handles communication with
        UnicornEngine.
        """

        SimStatePlugin.__init__(self)

        self._syscall_pc = None
        self.jumpkind = 'Ijk_Boring'
        self.error = None
        self.errno = 0
        self.trap_ip = None

        self.cache_key = hash(self) if cache_key is None else cache_key

        # cooldowns to avoid thrashing in and out of unicorn
        # the countdown vars are the CURRENT counter that is counting down
        # when they hit zero execution will start
        # the cooldown vars are the settings for what the countdown should start at
        # the val is copied from cooldown to countdown on check fail
        self.cooldown_nonunicorn_blocks = cooldown_nonunicorn_blocks
        self.cooldown_symbolic_stop = cooldown_symbolic_stop
        self.cooldown_unsupported_stop = cooldown_unsupported_stop
        self.cooldown_stop_point = cooldown_stop_point
        self.countdown_nonunicorn_blocks = 0
        self.countdown_symbolic_stop = 0
        self.countdown_unsupported_stop = 0
        self.countdown_stop_point = 0

        # the default step limit
        self.max_steps = max_steps

        self.steps = 0
        self._mapped = 0
        self._uncache_regions = []
        self._symbolic_offsets = None
        self.gdt = None

        # following variables are used in python level hook
        # we cannot see native hooks from python
        self.syscall_hooks = { } if syscall_hooks is None else syscall_hooks

        # native state in libsimunicorn
        self._uc_state = None
        self.stop_reason = None
        self.stop_details = None
        self.stop_message = None

        # this is the counter for the unicorn count
        self._unicount = next(_unicounter) if unicount is None else unicount

        #
        # Selective concretization stuff
        #

        # this is the number of times specific symbolic variables have kicked us out of unicorn
        self.symbolic_var_counts = { } if symbolic_var_counts is None else symbolic_var_counts

        # this is the number of times we've been kept out of unicorn at given instructions
        self.symbolic_inst_counts = { } if symbolic_inst_counts is None else symbolic_inst_counts

        # these are threshold for the number of times that we tolerate being kept out of unicorn
        # before we start concretizing
        self.concretization_threshold_memory = concretization_threshold_memory
        self.concretization_threshold_registers = concretization_threshold_registers
        self.concretization_threshold_instruction = concretization_threshold_instruction

        # these are sets of names of variables that should either always or never
        # be concretized
        self.always_concretize = set() if always_concretize is None else always_concretize
        self.never_concretize = set() if never_concretize is None else never_concretize
        self.concretize_at = set() if concretize_at is None else concretize_at

        # this is a record of the ASTs for which we've added concretization constraints
        self._concretized_asts = set() if concretized_asts is None else concretized_asts

        # the address to use for concrete transmits
        self.transmit_addr = None

        self.time = None

        self._bullshit_cb = ctypes.cast(unicorn.unicorn.UC_HOOK_MEM_INVALID_CB(self._hook_mem_unmapped), unicorn.unicorn.UC_HOOK_MEM_INVALID_CB)
        self._skip_next_callback = False

    @SimStatePlugin.memo
    def copy(self, _memo):
        u = Unicorn(
            syscall_hooks=dict(self.syscall_hooks),
            cache_key=self.cache_key,
            #unicount=self._unicount,
            symbolic_var_counts = dict(self.symbolic_var_counts),
            symbolic_inst_counts = dict(self.symbolic_inst_counts),
            concretized_asts = set(self._concretized_asts),
            always_concretize = set(self.always_concretize),
            never_concretize = set(self.never_concretize),
            concretize_at = set(self.concretize_at),
            concretization_threshold_memory = self.concretization_threshold_memory,
            concretization_threshold_registers = self.concretization_threshold_registers,
            concretization_threshold_instruction = self.concretization_threshold_instruction,
            cooldown_nonunicorn_blocks=self.cooldown_nonunicorn_blocks,
            cooldown_symbolic_stop=self.cooldown_symbolic_stop,
            cooldown_unsupported_stop=self.cooldown_unsupported_stop,
            max_steps=self.max_steps,
        )
        u.countdown_nonunicorn_blocks = self.countdown_nonunicorn_blocks
        u.countdown_symbolic_stop = self.countdown_symbolic_stop
        u.countdown_unsupported_stop = self.countdown_unsupported_stop
        u.countdown_stop_point = self.countdown_stop_point
        u.transmit_addr = self.transmit_addr
        u._uncache_regions = list(self._uncache_regions)
        u.gdt = self.gdt
        return u

    def merge(self, others, merge_conditions, common_ancestor=None): # pylint: disable=unused-argument
        self.cooldown_nonunicorn_blocks = max(
            self.cooldown_nonunicorn_blocks,
            max(o.cooldown_nonunicorn_blocks for o in others)
        )
        self.cooldown_symbolic_stop = max(
            self.cooldown_symbolic_stop,
            max(o.cooldown_symbolic_stop for o in others)
        )
        self.cooldown_unsupported_stop = max(
            self.cooldown_unsupported_stop,
            max(o.cooldown_unsupported_stop for o in others)
        )
        self.countdown_nonunicorn_blocks = max(
            self.countdown_nonunicorn_blocks,
            max(o.countdown_nonunicorn_blocks for o in others)
        )
        self.countdown_symbolic_stop = max(
            self.countdown_symbolic_stop,
            max(o.countdown_symbolic_stop for o in others)
        )
        self.countdown_unsupported_stop = max(
            self.countdown_unsupported_stop,
            max(o.countdown_unsupported_stop for o in others)
        )
        self.countdown_stop_point = max(
            self.countdown_stop_point,
            max(o.countdown_stop_point for o in others)
        )

        # get a fresh unicount, just in case
        self._unicount = next(_unicounter)

        # keep these guys, since merging them sounds like a pain
        #self.symbolic_var_counts
        #self.symbolic_inst_counts

        # these are threshold for the number of times that we tolerate being kept out of unicorn
        # before we start concretizing
        def merge_nullable_min(*args):
            nonnull = [a for a in args if a is not None]
            if not nonnull:
                return None
            return min(nonnull)
        self.concretization_threshold_memory = merge_nullable_min(self.concretization_threshold_memory, *(o.concretization_threshold_memory for o in others))
        self.concretization_threshold_registers = merge_nullable_min(self.concretization_threshold_registers, *(o.concretization_threshold_registers for o in others))
        self.concretization_threshold_instruction = merge_nullable_min(self.concretization_threshold_instruction, *(o.concretization_threshold_instruction for o in others))

        # these are sets of names of variables that should either always or never
        # be concretized
        self.always_concretize.union(*[o.always_concretize for o in others])
        self.never_concretize.union(*[o.never_concretize for o in others])
        self.concretize_at.union(*[o.concretize_at for o in others])

        # intersect these so that we know to add future constraints properly
        self._concretized_asts.intersection(*[o._concretized_asts for o in others])

        # I guess always lie to the static analysis?
        return False

    def widen(self, others): # pylint: disable=unused-argument
        l.warning("Can't widen the unicorn plugin!")

    def __getstate__(self):
        d = dict(self.__dict__)
        del d['_bullshit_cb']
        del d['_uc_state']
        del d['cache_key']
        del d['_unicount']
        return d

    def __setstate__(self, s):
        self.__dict__.update(s)
        self._bullshit_cb = ctypes.cast(unicorn.unicorn.UC_HOOK_MEM_INVALID_CB(self._hook_mem_unmapped), unicorn.unicorn.UC_HOOK_MEM_INVALID_CB)
        self._unicount = next(_unicounter)
        self._uc_state = None
        self.cache_key = hash(self)
        _unicorn_tls.uc = None

    def set_state(self, state):
        SimStatePlugin.set_state(self, state)
        if self._is_mips32:
            self._unicount = next(_unicounter)

    @property
    def _reuse_unicorn(self):
        return not self._is_mips32

    @property
    def uc(self):
        new_id = next(_unicounter)
        is_thumb = self.state.arch.qemu_name == 'arm' and self.state.arch.is_thumb(self.state.addr)
        if (
            not hasattr(_unicorn_tls, "uc") or
            _unicorn_tls.uc is None or
            _unicorn_tls.uc.arch != self.state.arch or
            _unicorn_tls.uc.cache_key != self.cache_key
        ):
            _unicorn_tls.uc = Uniwrapper(self.state.arch, self.cache_key, thumb=is_thumb)
        elif _unicorn_tls.uc.id != self._unicount:
            if not self._reuse_unicorn:
                _unicorn_tls.uc = Uniwrapper(self.state.arch, self.cache_key, thumb=is_thumb)
            else:
                #l.debug("Reusing unicorn state!")
                _unicorn_tls.uc.reset()
        else:
            #l.debug("Reusing unicorn state!")
            pass

        _unicorn_tls.uc.id = new_id
        self._unicount = new_id
        return _unicorn_tls.uc

    @staticmethod
    def delete_uc():
        _unicorn_tls.uc = None

    @property
    def _uc_regs(self):
        return self.state.arch.uc_regs

    @property
    def _uc_prefix(self):
        return self.state.arch.uc_prefix

    @property
    def _uc_const(self):
        return self.state.arch.uc_const

    def _setup_unicorn(self):
        if self.state.arch.uc_mode is None:
            raise SimUnicornUnsupport("unsupported architecture %r" % self.state.arch)

    def set_stops(self, stop_points):
        _UC_NATIVE.set_stops(self._uc_state,
            ctypes.c_uint64(len(stop_points)),
            (ctypes.c_uint64 * len(stop_points))(*map(ctypes.c_uint64, stop_points))
        )

    def set_tracking(self, track_bbls, track_stack):
        _UC_NATIVE.set_tracking(self._uc_state, track_bbls, track_stack)

    def hook(self):
        #l.debug('adding native hooks')
        _UC_NATIVE.hook(self._uc_state) # prefer to use native hooks

        self.uc.hook_add(unicorn.UC_HOOK_MEM_UNMAPPED, self._hook_mem_unmapped, None, 1)

        arch = self.state.arch.qemu_name
        if arch == 'x86_64':
            self.uc.hook_add(unicorn.UC_HOOK_INTR, self._hook_intr_x86, None, 1, 0)
            self.uc.hook_add(unicorn.UC_HOOK_INSN, self._hook_syscall_x86_64, None, arg1=self._uc_const.UC_X86_INS_SYSCALL)
        elif arch == 'i386':
            self.uc.hook_add(unicorn.UC_HOOK_INTR, self._hook_intr_x86, None, 1, 0)
        elif arch == 'mips':
            self.uc.hook_add(unicorn.UC_HOOK_INTR, self._hook_intr_mips, None, 1, 0)
        elif arch == 'mipsel':
            self.uc.hook_add(unicorn.UC_HOOK_INTR, self._hook_intr_mips, None, 1, 0)
        elif arch == 'arm':
            # EDG says: Unicorn's ARM support has no concept of interrupts.
            # This is because interrupts are not a part of the ARM ISA per se, and interrupt controllers
            # are left to the vendor to provide.
            # TODO: This is not true for CortexM.  Revisit when Tobi's NVIC implementation gets upstreamed.
            pass
        else:
            raise SimUnicornUnsupport

    def _hook_intr_mips(self, uc, intno, user_data):
        self.trap_ip = self.uc.reg_read(unicorn.mips_const.UC_MIPS_REG_PC)

        if intno == 17:  # EXCP_SYSCALL
            sysno = uc.reg_read(self._uc_regs['v0'])
            pc = uc.reg_read(self._uc_regs['pc'])
            l.debug('hit sys_%d at %#x', sysno, pc)
            self._syscall_pc = pc
            self._handle_syscall(uc, user_data)
        else:
            l.warning('unhandled interrupt %d', intno)
            _UC_NATIVE.stop(self._uc_state, STOP.STOP_ERROR)

    def _hook_intr_x86(self, uc, intno, user_data):
        if _UC_NATIVE.is_interrupt_handled(self._uc_state):
            return

        if self.state.arch.bits == 32:
            self.trap_ip = self.uc.reg_read(unicorn.x86_const.UC_X86_REG_EIP)
        else:
            self.trap_ip = self.uc.reg_read(unicorn.x86_const.UC_X86_REG_RIP)

        # http://wiki.osdev.org/Exceptions
        if intno == 0:
            # divide by zero
            _UC_NATIVE.stop(self._uc_state, STOP.STOP_ZERO_DIV)
        elif intno == 0x80:
            if self.state.arch.bits == 32:
                self._hook_syscall_i386(uc, user_data)
            else:
                self._hook_syscall_x86_64(uc, user_data)
        else:
            l.warning('unhandled interrupt %d', intno)
            _UC_NATIVE.stop(self._uc_state, STOP.STOP_ERROR)

    def _hook_syscall_x86_64(self, uc, user_data):
        sysno = uc.reg_read(self._uc_regs['rax'])
        pc = uc.reg_read(self._uc_regs['rip'])
        l.debug('hit sys_%d at %#x', sysno, pc)
        self._syscall_pc = pc + 2  # skip syscall instruction
        self._handle_syscall(uc, user_data)

    def _hook_syscall_i386(self, uc, user_data):
        sysno = uc.reg_read(self._uc_regs['eax'])
        pc = uc.reg_read(self._uc_regs['eip'])
        l.debug('hit sys_%d at %#x', sysno, pc)
        self._syscall_pc = pc
        if not self._quick_syscall(sysno):
            self._handle_syscall(uc, user_data)

    def _quick_syscall(self, sysno):
        if sysno in self.syscall_hooks:
            self.syscall_hooks[sysno](self.state)
            return True
        else:
            return False

    def _handle_syscall(self, uc, user_data): #pylint:disable=unused-argument
        # unicorn does not support syscall, we should giveup emulation
        # and send back to SimProcedure. (ignore is always False)
        l.info('stop emulation')
        self.jumpkind = 'Ijk_Sys_syscall'
        _UC_NATIVE.stop(self._uc_state, STOP.STOP_SYSCALL)

    def _concretize(self, d):
        cd = self.state.solver.eval_to_ast(d, 1)[0]
        if hash(d) not in self._concretized_asts:
            constraint = (d == cd).annotate(AggressiveConcretizationAnnotation(self.state.regs.ip))
            self.state.add_constraints(constraint)
            self._concretized_asts.add(hash(d))
        return cd

    def _symbolic_passthrough(self, d):
        if not d.symbolic:
            return d
        elif options.UNICORN_AGGRESSIVE_CONCRETIZATION in self.state.options:
            return self._concretize(d)
        elif len(d.variables & self.never_concretize) > 0:
            return d
        elif d.variables.issubset(self.always_concretize):
            return self._concretize(d)
        elif self.state.solver.eval(self.state.ip) in self.concretize_at:
            return self._concretize(d)
        else:
            return d

    def _report_symbolic_blocker(self, d, from_where):
        if options.UNICORN_THRESHOLD_CONCRETIZATION in self.state.options:
            if self.concretization_threshold_instruction is not None:
                addr = self.state.solver.eval(self.state.ip)
                count = self.symbolic_inst_counts.get(addr, 0)
                l.debug("... inst count for %s: %d", addr, count)
                self.symbolic_inst_counts[addr] = count + 1
                if count >= self.concretization_threshold_instruction:
                    self.concretize_at.add(addr)

            threshold = (
                self.concretization_threshold_memory if from_where == 'mem' else
                self.concretization_threshold_registers
            )
            if threshold is None:
                return

            for v in d.variables:
                old_count = self.symbolic_var_counts.get(v, 0)
                l.debug("... %s: %d", v, old_count)
                self.symbolic_var_counts[v] = old_count + 1
                if old_count >= threshold:
                    self.always_concretize.add(v)

    def _process_value(self, d, from_where):
        """
        Pre-process an AST for insertion into unicorn.

        :param d: the AST
        :param from_where: the ID of the memory region it comes from ('mem' or 'reg')
        :returns: the value to be inserted into Unicorn, or None
        """
        if len(d.annotations):
            l.debug("Blocking annotated AST.")
            return None
        elif not d.symbolic:
            return d
        else:
            l.debug("Processing AST with variables %s.", d.variables)

        dd = self._symbolic_passthrough(d)

        if not dd.symbolic:
            if d.symbolic:
                l.debug("... concretized")
            return dd
        elif from_where == 'reg' and options.UNICORN_SYM_REGS_SUPPORT in self.state.options:
            l.debug("... allowing symbolic register")
            return dd
        else:
            l.debug("... denied")
            return None

    def _hook_mem_unmapped(self, uc, access, address, size, value, user_data): #pylint:disable=unused-argument
        """
        This callback is called when unicorn needs to access data that's not yet present in memory.
        """
        if user_data == 1:
            self._skip_next_callback = True
        elif self._skip_next_callback:
            self._skip_next_callback = False
            return True

        start = address & ~0xfff
        needed_pages = 2 if address - start + size > 0x1000 else 1

        attempt_pages = 10
        for pageno in range(attempt_pages):
            page_addr = (start + pageno * 0x1000) & ((1 << self.state.arch.bits) - 1)
            if page_addr == 0:
                if pageno >= needed_pages:
                    break
                if options.UNICORN_ZEROPAGE_GUARD in self.state.options:
                    self.error = 'accessing zero page (%#x)' % access
                    l.warning(self.error)

                    _UC_NATIVE.stop(self._uc_state, STOP.STOP_ZEROPAGE)
                    return False

            l.info('mmap [%#x, %#x] because %d', page_addr, page_addr + 0xfff, access)
            try:
                self._map_one_page(uc, page_addr)
            except SegfaultError:
                # this is the unicorn segfault error. idk why this would show up
                _UC_NATIVE.stop(self._uc_state, STOP.STOP_SEGFAULT)
                return False
            except SimSegfaultError:
                _UC_NATIVE.stop(self._uc_state, STOP.STOP_SEGFAULT)
                return False
            except unicorn.UcError as e:
                if e.errno != 11:
                    self.error = str(e)
                    _UC_NATIVE.stop(self._uc_state, STOP.STOP_ERROR)
                    return False
                l.info("...already mapped :)")
                break
            except SimMemoryError as e:
                if pageno >= needed_pages:
                    l.info("...never mind")
                    break
                else:
                    self.error = str(e)
                    _UC_NATIVE.stop(self._uc_state, STOP.STOP_ERROR)
                    return False

        return True

    def _map_one_page(self, _uc, addr):
        # allow any SimMemory errors to propagate upward. they will be caught immediately above
        perm = self.state.memory.permissions(addr)

        if perm.op != 'BVV':
            perm = 7
        elif options.ENABLE_NX not in self.state.options:
            perm = perm.args[0] | 4
        else:
            perm = perm.args[0]

        # this should return two memoryviews
        # if they are writable they are direct references to the state backing store and can be mapped directly
        data, bitmap = self.state.memory.concrete_load(addr, 0x1000, with_bitmap=True, writing=(perm & 2) != 0)

        if not bitmap:
            raise SimMemoryError('No bytes available in memory? when would this happen...')

        if bitmap.readonly:
            # old-style mapping, do it via copy
            self.uc.mem_map(addr, 0x1000, perm)
            # huge hack. why doesn't ctypes let you pass memoryview as void*?
            unicorn.unicorn._uc.uc_mem_write(self.uc._uch, addr, ctypes.cast(int(ffi.cast('uint64_t', ffi.from_buffer(data))), ctypes.c_void_p), len(data))
            #self.uc.mem_write(addr, data)
            self._mapped += 1
            _UC_NATIVE.activate_page(self._uc_state, addr, int(ffi.cast('uint64_t', ffi.from_buffer(bitmap))), None)
        else:
            # new-style mapping, do it directly
            self.uc.mem_map_ptr(addr, 0x1000, perm, int(ffi.cast('uint64_t', ffi.from_buffer(data))))
            self._mapped += 1
            _UC_NATIVE.activate_page(self._uc_state, addr, int(ffi.cast('uint64_t', ffi.from_buffer(bitmap))), int(ffi.cast('unsigned long', ffi.from_buffer(data))))

        return


        # do the mapping
        if not taint and not perm & 2:
            # page is non-writable, handle it with native code
            l.debug('caching non-writable page')
            out = _UC_NATIVE.cache_page(self._uc_state, start, length, bytes(data), perm)
            return out
        else:
            # if the memory range has already been mapped, or it somehow fails sanity checks, mem_map() may fail with
            # a unicorn.UcError raised. THe exception will be caught outside.
            uc.mem_map(start, length, perm)
            uc.mem_write(start, bytes(data))
            self._mapped += 1
            _UC_NATIVE.activate(self._uc_state, start, length, taint[0] if taint else None)
            return True

    def _get_details_of_blocks_with_symbolic_instrs(self):
        def _get_register_values(register_values):
            for register_value in register_values:
                # Convert the register value in bytes to number of appropriate size and endianness
                reg_name, reg_size = self.state.arch.vex_reg_offset_to_name[register_value.offset]
                if self.state.arch.register_endness == archinfo.Endness.LE:
                    reg_value = int.from_bytes(register_value.value, "little")
                else:
                    reg_value = int.from_bytes(register_value.value, "big")

                reg_value = reg_value & (pow(2, reg_size * 8) - 1)
                yield (reg_name, reg_value)

        def _get_memory_values(memory_values):
            for memory_value in memory_values:
                mem_address = memory_value.address
                mem_val_size = memory_value.size
                # Convert the memory value in bytes to number of appropriate size and endianness
                mem_val = memory_value.value[:mem_val_size]
                if self.state.arch.memory_endness == archinfo.Endness.LE:
                    mem_val = int.from_bytes(mem_val, "little")
                else:
                    mem_val = int.from_bytes(mem_val, "big")

                yield {"address": mem_address, "value": mem_val, "size": mem_val_size}

        def _get_instr_details(symbolic_instrs):
            for instr in symbolic_instrs:
                instr_entry = {"instr_addr": instr.instr_addr, "mem_dep": []}
                if instr.has_memory_dep:
                    instr_entry["mem_dep"] = _get_memory_values(instr.memory_values[:instr.memory_values_count])

                yield instr_entry

        block_count = _UC_NATIVE.get_count_of_blocks_with_symbolic_instrs(self._uc_state)
        if block_count == 0:
            return

        block_details_list = (BlockDetails * block_count)()
        _UC_NATIVE.get_details_of_blocks_with_symbolic_instrs(self._uc_state, block_details_list)
        for block_details in block_details_list:
            entry = {"block_addr": block_details.block_addr, "block_size": block_details.block_size, "registers": {}}
            entry["registers"] = _get_register_values(block_details.register_values[:block_details.register_values_count])
            entry["instrs"] = _get_instr_details(block_details.symbolic_instrs[:block_details.symbolic_instrs_count])
            yield entry

    def uncache_region(self, addr, length):
        self._uncache_regions.append((addr, length))

    def clear_page_cache(self):
        self._uncache_regions = [] # this is no longer needed, everything has been uncached
        _UC_NATIVE.clear_page_cache()

    @property
    def _is_mips32(self):
        """
        There seems to be weird issues with unicorn-engine support on MIPS32 code (see commit 01126bf7). As a result,
        we test if the current architecture is MIPS32 in several places, and if so, we perform some extra steps, like
        re-creating the thread-local UC object.

        :return:    True if the current architecture is MIPS32, False otherwise.
        :rtype:     bool
        """
        return self.state.arch.name == "MIPS32"

    def setup(self):
        if self._is_mips32 and options.COPY_STATES not in self.state.options:
            # we always re-create the thread-local UC object for MIPS32 even if COPY_STATES is disabled in state
            # options. this is to avoid some weird bugs in unicorn (e.g., it reports stepping 1 step while in reality it
            # did not step at all).
            self.delete_uc()
        self._setup_unicorn()
        try:
            self.set_regs()
        except SimValueError:
            # reset the state and re-raise
            self.uc.reset()
            raise
        # tricky: using unicorn handle from unicorn.Uc object
        self._uc_state = _UC_NATIVE.alloc(self.uc._uch, self.cache_key)

        if options.UNICORN_SYM_REGS_SUPPORT in self.state.options and \
                options.UNICORN_AGGRESSIVE_CONCRETIZATION not in self.state.options:
            archinfo = copy.deepcopy(self.state.arch.vex_archinfo)
            archinfo['hwcache_info']['caches'] = 0
            archinfo['hwcache_info'] = _VexCacheInfo(**archinfo['hwcache_info'])
            _UC_NATIVE.enable_symbolic_reg_tracking(
                self._uc_state,
                getattr(pyvex.pvc, self.state.arch.vex_arch),
                _VexArchInfo(**archinfo),
            )

            if self._symbolic_offsets:
                l.debug("Sybmolic offsets: %s", self._symbolic_offsets)
                sym_regs_array = (ctypes.c_uint64 * len(self._symbolic_offsets))(*map(ctypes.c_uint64, self._symbolic_offsets))
                _UC_NATIVE.symbolic_register_data(self._uc_state, len(self._symbolic_offsets), sym_regs_array)
            else:
                _UC_NATIVE.symbolic_register_data(self._uc_state, 0, None)

        # set (cgc, for now) transmit syscall handler
        if UNICORN_HANDLE_TRANSMIT_SYSCALL in self.state.options and self.state.has_plugin('cgc'):
            if self.transmit_addr is None:
                l.error("You haven't set the address for concrete transmits!!!!!!!!!!!")
                self.transmit_addr = 0
            _UC_NATIVE.set_transmit_sysno(self._uc_state, 2, self.transmit_addr)

        # set memory map callback so we can call it explicitly
        _UC_NATIVE.set_map_callback(self._uc_state, self._bullshit_cb)

        # activate gdt page, which was written/mapped during set_regs
        if self.gdt is not None:
            _UC_NATIVE.activate_page(self._uc_state, self.gdt.addr, bytes(0x1000), None)

        # Initialize list of artificial VEX registers
        artificial_regs_list = self.state.arch.artificial_registers_offsets
        artificial_regs_array = (ctypes.c_uint64 * len(artificial_regs_list))(*map(ctypes.c_uint64, artificial_regs_list))
        _UC_NATIVE.set_artificial_registers(self._uc_state, artificial_regs_array, len(artificial_regs_list))

        # Initialize VEX register offset to unicorn register ID mappings and VEX register offset to name map
        vex_reg_offsets = []
        unicorn_reg_ids = []
        for vex_reg_offset, unicorn_reg_id in self.state.arch.vex_to_unicorn_map.items():
            vex_reg_offsets.append(vex_reg_offset)
            unicorn_reg_ids.append(unicorn_reg_id)

        vex_reg_offsets_array = (ctypes.c_uint64 * len(vex_reg_offsets))(*map(ctypes.c_uint64, vex_reg_offsets))
        unicorn_reg_ids_array = (ctypes.c_uint64 * len(unicorn_reg_ids))(*map(ctypes.c_uint64, unicorn_reg_ids))
        _UC_NATIVE.set_vex_to_unicorn_reg_mappings(self._uc_state, vex_reg_offsets_array, unicorn_reg_ids_array, len(vex_reg_offsets))

        vex_reg_offsets = []
        vex_sub_reg_offsets = []
        for vex_sub_reg_offset, vex_reg_offset in self.state.arch.vex_sub_reg_to_reg_map.items():
            vex_reg_offsets.append(vex_reg_offset)
            vex_sub_reg_offsets.append(vex_sub_reg_offset)

        vex_reg_offsets_array = (ctypes.c_uint64 * len(vex_reg_offsets))(*map(ctypes.c_uint64, vex_reg_offsets))
        vex_sub_reg_offsets_array = (ctypes.c_uint64 * len(vex_sub_reg_offsets))(*map(ctypes.c_uint64, vex_sub_reg_offsets))
        _UC_NATIVE.set_vex_sub_reg_to_reg_mappings(self._uc_state, vex_sub_reg_offsets_array, vex_reg_offsets_array, len(vex_sub_reg_offsets_array))

        vex_reg_offsets = []
        vex_reg_sizes = []
        for vex_reg_offset, vex_reg_size in self.state.arch.vex_reg_to_size_map.items():
            vex_reg_offsets.append(vex_reg_offset)
            vex_reg_sizes.append(vex_reg_size)

        vex_reg_offsets_array = (ctypes.c_uint64 * len(vex_reg_offsets))(*map(ctypes.c_uint64, vex_reg_offsets))
        vex_reg_sizes_array = (ctypes.c_uint64 * len(vex_reg_sizes))(*map(ctypes.c_uint64, vex_reg_sizes))
        _UC_NATIVE.set_vex_offset_to_register_size_mapping(self._uc_state, vex_reg_offsets_array, vex_reg_sizes_array, len(vex_reg_offsets_array))

        # Initial VEX to unicorn mappings for flag register
        if self.state.arch.unicorn_flag_register:
            _UC_NATIVE.set_unicorn_flags_register_id(self._uc_state, self.state.arch.unicorn_flag_register)
            cpu_flag_vex_offsets = []
            cpu_flag_bitmasks = []
            for cpu_flag_reg_offset, cpu_flag_reg_bitmask in self.state.arch.cpu_flag_register_offsets_and_bitmasks_map.items():
                cpu_flag_vex_offsets.append(cpu_flag_reg_offset)
                cpu_flag_bitmasks.append(cpu_flag_reg_bitmask)

            if len(cpu_flag_vex_offsets) > 0:
                cpu_flag_vex_offsets_array = (ctypes.c_uint64 * len(cpu_flag_vex_offsets))(*map(ctypes.c_uint64, cpu_flag_vex_offsets))
                cpu_flag_bitmasks_array = (ctypes.c_uint64 * len(cpu_flag_bitmasks))(*map(ctypes.c_uint64, cpu_flag_bitmasks))
                _UC_NATIVE.set_cpu_flags_details(self._uc_state, cpu_flag_vex_offsets_array, cpu_flag_bitmasks_array,len(cpu_flag_vex_offsets))
        elif self.state.arch.name.startswith("ARM"):
            l.warning(f"Flag registers for {self.state.arch.name} not set in native unicorn interface.")

        # Initialize list of blacklisted registers
        blacklist_regs_offsets = self.state.arch.reg_blacklist_offsets
        if len(blacklist_regs_offsets) > 0:
            blacklist_regs_array = (ctypes.c_uint64 * len(blacklist_regs_offsets))(*map(ctypes.c_uint64, blacklist_regs_offsets))
            _UC_NATIVE.set_register_blacklist(self._uc_state, blacklist_regs_array, len(blacklist_regs_offsets))

    def start(self, step=None):
        self.jumpkind = 'Ijk_Boring'
        self.countdown_nonunicorn_blocks = self.cooldown_nonunicorn_blocks

        for addr, length in self._uncache_regions:
            l.debug("Un-caching writable page region @ %#x of length %x", addr, length)
            _UC_NATIVE.uncache_pages_touching_region(self._uc_state, addr, length)
        self._uncache_regions = []

        addr = self.state.solver.eval(self.state.ip)
        l.info('started emulation at %#x (%d steps)', addr, self.max_steps if step is None else step)
        self.time = time.time()
        self.errno = _UC_NATIVE.start(self._uc_state, addr, self.max_steps if step is None else step)
        self.time = time.time() - self.time

    def finish(self):
        # do the superficial synchronization
        self.get_regs()
        self.steps = _UC_NATIVE.step(self._uc_state)
        self.stop_details = _UC_NATIVE.get_stop_details(self._uc_state)
        self.stop_reason = self.stop_details.stop_reason
        self.stop_message = STOP.get_stop_msg(self.stop_reason)
        if self.stop_reason in (STOP.symbolic_stop_reasons + STOP.unsupported_reasons) or \
          self.stop_reason in (STOP.STOP_UNKNOWN_MEMORY_WRITE, STOP.STOP_VEX_LIFT_FAILED):
            self.stop_message += f". Block 0x{self.stop_details.block_addr:02x}(size: {self.stop_details.block_size})."

        # figure out why we stopped
        if self.stop_reason == STOP.STOP_NOSTART and self.steps > 0:
            # unicorn just does quits without warning if it sees hlt. detect that.
            if (self.state.memory.load(self.state.ip, 1) == 0xf4).is_true():
                self.stop_reason = STOP.STOP_HLT
            else:
                raise SimUnicornError("Got STOP_NOSTART but a positive number of steps. This indicates a serious unicorn bug.")

        addr = self.state.solver.eval(self.state.ip)
        l.info('finished emulation at %#x after %d steps: %s', addr, self.steps, STOP.name_stop(self.stop_reason))

        # should this be in destroy?
        _UC_NATIVE.disable_symbolic_reg_tracking(self._uc_state)

        # synchronize memory contents - head is a linked list of memory updates
        head = _UC_NATIVE.sync(self._uc_state)
        p_update = head
        while bool(p_update):
            update = p_update.contents
            address, length = update.address, update.length
            if self.gdt is not None and self.gdt.addr <= address < self.gdt.addr + self.gdt.limit:
                l.warning("Emulation touched fake GDT at %#x, discarding changes" % self.gdt.addr)
            else:
                s = bytes(self.uc.mem_read(address, int(length)))
                l.debug('...changed memory: [%#x, %#x] = %s', address, address + length, binascii.hexlify(s))
                self.state.memory.store(address, s)

            p_update = update.next

        # process the concrete transmits
        i = 0
        stdout = self.state.posix.get_fd(1)

        while True:
            record = _UC_NATIVE.process_transmit(self._uc_state, i)
            if not bool(record):
                break

            string = ctypes.string_at(record.contents.data, record.contents.count)
            stdout.write_data(string)
            i += 1

        if self.stop_reason in (STOP.STOP_NORMAL, STOP.STOP_SYSCALL, STOP.STOP_SYMBOLIC_MEM_DEP_NOT_LIVE):
            self.countdown_nonunicorn_blocks = 0
        elif self.stop_reason == STOP.STOP_STOPPOINT:
            self.countdown_nonunicorn_blocks = 0
            self.countdown_stop_point = self.cooldown_stop_point
        elif self.stop_reason in STOP.symbolic_stop_reasons:
            self.countdown_nonunicorn_blocks = 0
            self.countdown_symbolic_stop = self.cooldown_symbolic_stop
        elif self.stop_reason in STOP.unsupported_reasons:
            self.countdown_nonunicorn_blocks = 0
            self.countdown_unsupported_stop = self.cooldown_unsupported_stop
        elif self.stop_reason == STOP.STOP_UNKNOWN_MEMORY_WRITE:
            # Skip one block in case of unknown memory write
            self.countdown_nonunicorn_blocks = 0
            self.countdown_unsupported_stop = 2
        else:
            self.countdown_nonunicorn_blocks = self.cooldown_nonunicorn_blocks

        if not is_testing and self.time != 0 and self.steps / self.time < 10: # TODO: make this tunable
            l.info(
                "Unicorn stepped %d block%s in %fsec (%f blocks/sec), enabling cooldown",
                self.steps,
                '' if self.steps == 1 else 's',
                self.time,
                self.steps/self.time
            )
            self.countdown_nonunicorn_blocks = self.cooldown_nonunicorn_blocks
        else:
            l.info(
                "Unicorn stepped %d block%s in %fsec (%f blocks/sec)",
                self.steps,
                '' if self.steps == 1 else 's',
                self.time,
                self.steps/self.time if self.time != 0 else float('nan')
            )

        # get the address list out of the state
        if options.UNICORN_TRACK_BBL_ADDRS in self.state.options:
            bbl_addrs = _UC_NATIVE.bbl_addrs(self._uc_state)
            #bbl_addr_count = _UC_NATIVE.bbl_addr_count(self._uc_state)
            # why is bbl_addr_count unused?
            if self.steps:
                self.state.history.recent_bbl_addrs = bbl_addrs[:self.steps]
        # get the stack pointers
        if options.UNICORN_TRACK_STACK_POINTERS in self.state.options:
            stack_pointers = _UC_NATIVE.stack_pointers(self._uc_state)
            self.state.scratch.stack_pointer_list = stack_pointers[:self.steps]
        # syscall counts
        self.state.history.recent_syscall_count = _UC_NATIVE.syscall_count(self._uc_state)
        # executed page set
        self.state.scratch.executed_pages_set = set()
        while True:
            page = _UC_NATIVE.executed_pages(self._uc_state)
            if page == 2**64 - 1:
                break
            self.state.scratch.executed_pages_set.add(page)

    def destroy(self):
        #l.debug("Unhooking.")
        _UC_NATIVE.unhook(self._uc_state)
        self.uc.hook_reset()

        #l.debug('deallocting native state %#x', self._uc_state)
        _UC_NATIVE.dealloc(self._uc_state)
        self._uc_state = None

        # there's something we're not properly resetting for syscalls, so
        # we'll clear the state when they happen
        if self.stop_reason not in (STOP.STOP_NORMAL, STOP.STOP_STOPPOINT):
            self.delete_uc()

        #l.debug("Resetting the unicorn state.")
        self.uc.reset()

    def set_regs(self):
        ''' setting unicorn registers '''
        uc = self.uc

        self._symbolic_offsets = set()

        if self.state.arch.qemu_name == 'x86_64':
            fs = self.state.solver.eval(self.state.regs.fs)
            gs = self.state.solver.eval(self.state.regs.gs)
            self.write_msr(fs, 0xC0000100)
            self.write_msr(gs, 0xC0000101)
            flags = self._process_value(self.state.regs.eflags, 'reg')
            if flags is None:
                raise SimValueError('symbolic eflags')
            elif flags.symbolic:
                vex_offset = self.state.arch.registers['cc_op'][0]
                self._symbolic_offsets.update(range(vex_offset, vex_offset + 8*4))
            uc.reg_write(self._uc_const.UC_X86_REG_EFLAGS, self.state.solver.eval(flags))

        elif self.state.arch.qemu_name == 'i386':
            flags = self._process_value(self.state.regs.eflags, 'reg')
            if flags is None:
                raise SimValueError('symbolic eflags')
            elif flags.symbolic:
                vex_offset = self.state.arch.registers['cc_op'][0]
                self._symbolic_offsets.update(range(vex_offset, vex_offset + 4*4))

            uc.reg_write(self._uc_const.UC_X86_REG_EFLAGS, self.state.solver.eval(flags))

            fs = self.state.solver.eval(self.state.regs.fs) << 16
            gs = self.state.solver.eval(self.state.regs.gs) << 16
            self.setup_gdt(fs, gs)

        # handle ARM's "cpsr" register, equivalent of x86's eflags
        elif self.state.arch.qemu_name == 'arm':
            flags = self._process_value(self.state.regs.flags, 'reg')
            if flags is None:
                raise SimValueError('symbolic cpsr')
            elif flags.symbolic:
                vex_offset = self.state.arch.registers['cc_op'][0]
                self._symbolic_offsets.update(range(vex_offset, vex_offset + 4*4))
            uc.reg_write(self._uc_const.UC_ARM_REG_CPSR, self.state.solver.eval(flags))

        elif self.state.arch.qemu_name == 'mips':
            # ulr
            ulr = self.state.regs._ulr
            uc.reg_write(self._uc_const.UC_MIPS_REG_CP0_USERLOCAL, self.state.solver.eval(ulr))

        for r, c in self._uc_regs.items():
            if r in self.state.arch.reg_blacklist:
                continue
            v = self._process_value(getattr(self.state.regs, r), 'reg')
            if v is None:
                raise SimValueError('setting a symbolic register')
            # l.debug('setting $%s = %#x', r, self.state.solver.eval(v))
            uc.reg_write(c, self.state.solver.eval(v))

            start, size = self.state.arch.registers[r]
            if v.symbolic:
                self._symbolic_offsets.update(b for b,vb in enumerate(reversed(v.chop(8)), start) if vb.symbolic)

        # TODO: Support ARM hardfloat synchronization

        if self.state.arch.name in ('X86', 'AMD64'):
            # sync the fp clerical data
            c3210 = self.state.solver.eval(self.state.regs.fc3210)
            top = self.state.solver.eval(self.state.regs.ftop[2:0])
            rm = self.state.solver.eval(self.state.regs.fpround[1:0])
            control = 0x037F | (rm << 10)
            status = (top << 11) | c3210
            uc.reg_write(unicorn.x86_const.UC_X86_REG_FPCW, control)
            uc.reg_write(unicorn.x86_const.UC_X86_REG_FPSW, status)

            for rn in ('fc3210', 'ftop', 'fpround'):
                start, size = self.state.arch.registers[rn]
                self._symbolic_offsets.difference_update(range(start, start + size))

            # we gotta convert the 64-bit doubles values to 80-bit extended precision!
            uc_offset = unicorn.x86_const.UC_X86_REG_FP0
            vex_offset = self.state.arch.registers['fpu_regs'][0]
            vex_tag_offset = self.state.arch.registers['fpu_tags'][0]
            tag_word = 0
            for _ in range(8):
                tag = self.state.solver.eval(self.state.registers.load(vex_tag_offset, size=1))
                tag_word <<= 2
                if tag == 0:
                    tag_word |= 3       # unicorn doesn't care about any value other than 3 for setting
                else:
                    val = self._process_value(self.state.registers.load(vex_offset, size=8), 'reg')
                    if val is None:
                        raise SimValueError('setting a symbolic fp register')
                    if val.symbolic:
                        self._symbolic_offsets.difference_update(b for b,vb in enumerate(val.chop(8), start) if vb.symbolic)
                    val = self.state.solver.eval(val)

                    sign = bool(val & 0x8000000000000000)
                    exponent = (val & 0x7FF0000000000000) >> 52
                    mantissa =  val & 0x000FFFFFFFFFFFFF
                    if exponent not in (0, 0x7FF): # normal value
                        exponent = exponent - 1023 + 16383
                        mantissa <<= 11
                        mantissa |= 0x8000000000000000  # set integer part bit, implicit to double
                    elif exponent == 0:     # zero or subnormal value
                        mantissa = 0
                    elif exponent == 0x7FF:    # nan or infinity
                        exponent = 0x7FFF
                        if mantissa != 0:
                            mantissa = 0x8000000000000000
                        else:
                            mantissa = 0xFFFFFFFFFFFFFFFF

                    if sign:
                        exponent |= 0x8000

                    uc.reg_write(uc_offset, (exponent, mantissa))

                uc_offset += 1
                vex_offset += 8
                vex_tag_offset += 1

            uc.reg_write(unicorn.x86_const.UC_X86_REG_FPTAG, tag_word)

    def setup_gdt(self, fs, gs):
        gdt = self.state.project.simos.generate_gdt(fs, gs)
        uc = self.uc

        uc.mem_map(gdt.addr, gdt.limit)
        uc.mem_write(gdt.addr + 8, gdt.table)
        uc.reg_write(self._uc_const.UC_X86_REG_GDTR, (0, gdt.addr, gdt.limit, 0x0))

        uc.reg_write(self._uc_const.UC_X86_REG_CS, gdt.cs)
        uc.reg_write(self._uc_const.UC_X86_REG_DS, gdt.ds)
        uc.reg_write(self._uc_const.UC_X86_REG_ES, gdt.es)
        uc.reg_write(self._uc_const.UC_X86_REG_SS, gdt.ss)
        uc.reg_write(self._uc_const.UC_X86_REG_FS, gdt.fs)
        uc.reg_write(self._uc_const.UC_X86_REG_GS, gdt.gs)
        # if programs want to access this memory....... let them
        # uc.mem_unmap(GDT_ADDR, GDT_LIMIT)

        self.gdt = gdt

    # do NOT call either of these functions in a callback, lmao
    def read_msr(self, msr=0xC0000100):
        setup_code = b'\x0f\x32'
        BASE = 0x100B000000

        uc = self.uc
        uc.mem_map(BASE, 0x1000)
        uc.mem_write(BASE, setup_code)
        uc.reg_write(self._uc_const.UC_X86_REG_RCX, msr)
        uc.emu_start(BASE, BASE + len(setup_code))
        uc.mem_unmap(BASE, 0x1000)

        a = uc.reg_read(self._uc_const.UC_X86_REG_RAX)
        d = uc.reg_read(self._uc_const.UC_X86_REG_RDX)
        return (d << 32) + a

    def write_msr(self, val, msr=0xC0000100):
        setup_code = b'\x0f\x30'
        BASE = 0x100B000000

        uc = self.uc
        uc.mem_map(BASE, 0x1000)
        uc.mem_write(BASE, setup_code)
        uc.reg_write(self._uc_const.UC_X86_REG_RCX, msr)
        uc.reg_write(self._uc_const.UC_X86_REG_RAX, val & 0xFFFFFFFF)
        uc.reg_write(self._uc_const.UC_X86_REG_RDX, val >> 32)
        uc.emu_start(BASE, BASE + len(setup_code))
        uc.mem_unmap(BASE, 0x1000)

    def get_regs(self):
        ''' loading registers from unicorn '''

        # first, get the ignore list (in case of symbolic registers)
        saved_registers = []
        if options.UNICORN_SYM_REGS_SUPPORT in self.state.options:
            highest_reg_offset, reg_size = max(self.state.arch.registers.values())
            symbolic_list = (ctypes.c_uint64*(highest_reg_offset + reg_size))()
            num_regs = _UC_NATIVE.get_symbolic_registers(self._uc_state, symbolic_list)

            # we take the approach of saving off the symbolic regs and then writing them back

            cur_group = None
            last = None
            for i in sorted(symbolic_list[:num_regs]):
                if cur_group is None:
                    cur_group = i
                elif i != last + 1 or cur_group//self.state.arch.bytes != i//self.state.arch.bytes:
                    l.debug("Restoring symbolic register %d", cur_group)
                    saved_registers.append((
                        cur_group, self.state.registers.load(cur_group, last-cur_group+1)
                    ))
                    cur_group = i
                last = i
            if cur_group is not None:
                l.debug("Restoring symbolic register %d", cur_group)
                saved_registers.append((
                    cur_group, self.state.registers.load(cur_group, last-cur_group+1)
                ))

        # now we sync registers out of unicorn
        for r, c in self._uc_regs.items():
            if r in self.state.arch.reg_blacklist:
                continue
            v = self.uc.reg_read(c)
            # l.debug('getting $%s = %#x', r, v)
            setattr(self.state.regs, r, v)

        # some architecture-specific register fixups
        if self.state.arch.name in ('X86', 'AMD64'):
            # update the eflags
            self.state.regs.eflags = self.state.solver.BVV(self.uc.reg_read(self._uc_const.UC_X86_REG_EFLAGS), self.state.arch.bits)

            # sync the fp clerical data
            status = self.uc.reg_read(unicorn.x86_const.UC_X86_REG_FPSW)
            c3210 = status & 0x4700
            top = (status & 0x3800) >> 11
            control = self.uc.reg_read(unicorn.x86_const.UC_X86_REG_FPCW)
            rm = (control & 0x0C00) >> 10
            self.state.regs.fpround = rm
            self.state.regs.fc3210 = c3210
            self.state.regs.ftop = top

            # sync the stx registers
            # we gotta round the 80-bit extended precision values to 64-bit doubles!
            uc_offset = unicorn.x86_const.UC_X86_REG_FP0
            vex_offset = self.state.arch.registers['fpu_regs'][0]
            vex_tag_offset = self.state.arch.registers['fpu_tags'][0] + 7
            tag_word = self.uc.reg_read(unicorn.x86_const.UC_X86_REG_FPTAG)

            for _ in range(8):
                if tag_word & 3 == 3:
                    self.state.registers.store(vex_tag_offset, 0, size=1)
                else:
                    self.state.registers.store(vex_tag_offset, 1, size=1)

                    mantissa, exponent = self.uc.reg_read(uc_offset)
                    sign = bool(exponent & 0x8000)
                    exponent = (exponent & 0x7FFF)
                    if exponent not in (0, 0x7FFF): # normal value
                        exponent = exponent - 16383 + 1023
                        if exponent <= 0:   # underflow to zero
                            exponent = 0
                            mantissa = 0
                        elif exponent >= 0x7FF: # overflow to infinity
                            exponent = 0x7FF
                            mantissa = 0
                    elif exponent == 0:     # zero or subnormal value
                        mantissa = 0
                    elif exponent == 0x7FFF:    # nan or infinity
                        exponent = 0x7FF
                        if mantissa != 0:
                            mantissa = 0xFFFF

                    val = 0x8000000000000000 if sign else 0
                    val |= exponent << 52
                    val |= (mantissa >> 11) & 0xFFFFFFFFFFFFF
                    # the mantissa calculation is to convert from the 64-bit mantissa to 52-bit
                    # additionally, extended precision keeps around an high bit that we don't care about
                    # so 11-shift, not 12

                    self.state.registers.store(vex_offset, val, size=8)

                uc_offset += 1
                vex_offset += 8
                tag_word >>= 2
                vex_tag_offset -= 1

        # TODO: ARM hardfloat

        # now, we restore the symbolic registers
        if options.UNICORN_SYM_REGS_SUPPORT in self.state.options:
            for o, r in saved_registers:
                self.state.registers.store(o, r)

    def _check_registers(self, report=True):
        ''' check if this state might be used in unicorn (has no concrete register)'''
        for r in self.state.arch.uc_regs.keys():
            v = getattr(self.state.regs, r)
            processed_v = self._process_value(v, 'reg')
            if processed_v is None or processed_v.symbolic:
                #l.info('detected symbolic register %s', r)
                if report:
                    self._report_symbolic_blocker(v, 'reg')
                return False

        if self.state.arch.vex_conditional_helpers:
            flags = ccall._get_flags(self.state)
            processed_flags = self._process_value(flags, 'reg')
            if processed_flags is None or processed_flags.symbolic:
                #l.info("detected symbolic rflags/eflags")
                if report:
                    self._report_symbolic_blocker(flags, 'reg')
                return False

        #l.debug('passed quick check')
        return True


from angr.engines.vex.claripy import ccall
from .. import sim_options as options

from angr.sim_state import SimState
SimState.register_default('unicorn', Unicorn)
