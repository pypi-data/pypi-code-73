# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class PluginConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'args': 'PluginConfigArgs',
        'description': 'str',
        'docker_version': 'str',
        'documentation': 'str',
        'entrypoint': 'list[str]',
        'env': 'list[PluginEnv]',
        'interface': 'PluginConfigInterface',
        'ipc_host': 'bool',
        'linux': 'PluginConfigLinux',
        'mounts': 'list[PluginMount]',
        'network': 'PluginConfigNetwork',
        'pid_host': 'bool',
        'propagated_mount': 'str',
        'user': 'PluginConfigUser',
        'work_dir': 'str',
        'rootfs': 'PluginConfigRootfs'
    }

    attribute_map = {
        'args': 'Args',
        'description': 'Description',
        'docker_version': 'DockerVersion',
        'documentation': 'Documentation',
        'entrypoint': 'Entrypoint',
        'env': 'Env',
        'interface': 'Interface',
        'ipc_host': 'IpcHost',
        'linux': 'Linux',
        'mounts': 'Mounts',
        'network': 'Network',
        'pid_host': 'PidHost',
        'propagated_mount': 'PropagatedMount',
        'user': 'User',
        'work_dir': 'WorkDir',
        'rootfs': 'rootfs'
    }

    def __init__(self, args=None, description=None, docker_version=None, documentation=None, entrypoint=None, env=None, interface=None, ipc_host=None, linux=None, mounts=None, network=None, pid_host=None, propagated_mount=None, user=None, work_dir=None, rootfs=None, local_vars_configuration=None):  # noqa: E501
        """PluginConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._description = None
        self._docker_version = None
        self._documentation = None
        self._entrypoint = None
        self._env = None
        self._interface = None
        self._ipc_host = None
        self._linux = None
        self._mounts = None
        self._network = None
        self._pid_host = None
        self._propagated_mount = None
        self._user = None
        self._work_dir = None
        self._rootfs = None
        self.discriminator = None

        self.args = args
        self.description = description
        if docker_version is not None:
            self.docker_version = docker_version
        self.documentation = documentation
        self.entrypoint = entrypoint
        self.env = env
        self.interface = interface
        self.ipc_host = ipc_host
        self.linux = linux
        self.mounts = mounts
        self.network = network
        self.pid_host = pid_host
        self.propagated_mount = propagated_mount
        if user is not None:
            self.user = user
        self.work_dir = work_dir
        if rootfs is not None:
            self.rootfs = rootfs

    @property
    def args(self):
        """Gets the args of this PluginConfig.  # noqa: E501


        :return: The args of this PluginConfig.  # noqa: E501
        :rtype: PluginConfigArgs
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this PluginConfig.


        :param args: The args of this PluginConfig.  # noqa: E501
        :type: PluginConfigArgs
        """
        if self.local_vars_configuration.client_side_validation and args is None:  # noqa: E501
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def description(self):
        """Gets the description of this PluginConfig.  # noqa: E501

        description  # noqa: E501

        :return: The description of this PluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PluginConfig.

        description  # noqa: E501

        :param description: The description of this PluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def docker_version(self):
        """Gets the docker_version of this PluginConfig.  # noqa: E501

        Docker Version used to create the plugin  # noqa: E501

        :return: The docker_version of this PluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this PluginConfig.

        Docker Version used to create the plugin  # noqa: E501

        :param docker_version: The docker_version of this PluginConfig.  # noqa: E501
        :type: str
        """

        self._docker_version = docker_version

    @property
    def documentation(self):
        """Gets the documentation of this PluginConfig.  # noqa: E501

        documentation  # noqa: E501

        :return: The documentation of this PluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this PluginConfig.

        documentation  # noqa: E501

        :param documentation: The documentation of this PluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and documentation is None:  # noqa: E501
            raise ValueError("Invalid value for `documentation`, must not be `None`")  # noqa: E501

        self._documentation = documentation

    @property
    def entrypoint(self):
        """Gets the entrypoint of this PluginConfig.  # noqa: E501

        entrypoint  # noqa: E501

        :return: The entrypoint of this PluginConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this PluginConfig.

        entrypoint  # noqa: E501

        :param entrypoint: The entrypoint of this PluginConfig.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and entrypoint is None:  # noqa: E501
            raise ValueError("Invalid value for `entrypoint`, must not be `None`")  # noqa: E501

        self._entrypoint = entrypoint

    @property
    def env(self):
        """Gets the env of this PluginConfig.  # noqa: E501

        env  # noqa: E501

        :return: The env of this PluginConfig.  # noqa: E501
        :rtype: list[PluginEnv]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this PluginConfig.

        env  # noqa: E501

        :param env: The env of this PluginConfig.  # noqa: E501
        :type: list[PluginEnv]
        """
        if self.local_vars_configuration.client_side_validation and env is None:  # noqa: E501
            raise ValueError("Invalid value for `env`, must not be `None`")  # noqa: E501

        self._env = env

    @property
    def interface(self):
        """Gets the interface of this PluginConfig.  # noqa: E501


        :return: The interface of this PluginConfig.  # noqa: E501
        :rtype: PluginConfigInterface
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this PluginConfig.


        :param interface: The interface of this PluginConfig.  # noqa: E501
        :type: PluginConfigInterface
        """
        if self.local_vars_configuration.client_side_validation and interface is None:  # noqa: E501
            raise ValueError("Invalid value for `interface`, must not be `None`")  # noqa: E501

        self._interface = interface

    @property
    def ipc_host(self):
        """Gets the ipc_host of this PluginConfig.  # noqa: E501

        ipc host  # noqa: E501

        :return: The ipc_host of this PluginConfig.  # noqa: E501
        :rtype: bool
        """
        return self._ipc_host

    @ipc_host.setter
    def ipc_host(self, ipc_host):
        """Sets the ipc_host of this PluginConfig.

        ipc host  # noqa: E501

        :param ipc_host: The ipc_host of this PluginConfig.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and ipc_host is None:  # noqa: E501
            raise ValueError("Invalid value for `ipc_host`, must not be `None`")  # noqa: E501

        self._ipc_host = ipc_host

    @property
    def linux(self):
        """Gets the linux of this PluginConfig.  # noqa: E501


        :return: The linux of this PluginConfig.  # noqa: E501
        :rtype: PluginConfigLinux
        """
        return self._linux

    @linux.setter
    def linux(self, linux):
        """Sets the linux of this PluginConfig.


        :param linux: The linux of this PluginConfig.  # noqa: E501
        :type: PluginConfigLinux
        """
        if self.local_vars_configuration.client_side_validation and linux is None:  # noqa: E501
            raise ValueError("Invalid value for `linux`, must not be `None`")  # noqa: E501

        self._linux = linux

    @property
    def mounts(self):
        """Gets the mounts of this PluginConfig.  # noqa: E501

        mounts  # noqa: E501

        :return: The mounts of this PluginConfig.  # noqa: E501
        :rtype: list[PluginMount]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this PluginConfig.

        mounts  # noqa: E501

        :param mounts: The mounts of this PluginConfig.  # noqa: E501
        :type: list[PluginMount]
        """
        if self.local_vars_configuration.client_side_validation and mounts is None:  # noqa: E501
            raise ValueError("Invalid value for `mounts`, must not be `None`")  # noqa: E501

        self._mounts = mounts

    @property
    def network(self):
        """Gets the network of this PluginConfig.  # noqa: E501


        :return: The network of this PluginConfig.  # noqa: E501
        :rtype: PluginConfigNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this PluginConfig.


        :param network: The network of this PluginConfig.  # noqa: E501
        :type: PluginConfigNetwork
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def pid_host(self):
        """Gets the pid_host of this PluginConfig.  # noqa: E501

        pid host  # noqa: E501

        :return: The pid_host of this PluginConfig.  # noqa: E501
        :rtype: bool
        """
        return self._pid_host

    @pid_host.setter
    def pid_host(self, pid_host):
        """Sets the pid_host of this PluginConfig.

        pid host  # noqa: E501

        :param pid_host: The pid_host of this PluginConfig.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and pid_host is None:  # noqa: E501
            raise ValueError("Invalid value for `pid_host`, must not be `None`")  # noqa: E501

        self._pid_host = pid_host

    @property
    def propagated_mount(self):
        """Gets the propagated_mount of this PluginConfig.  # noqa: E501

        propagated mount  # noqa: E501

        :return: The propagated_mount of this PluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._propagated_mount

    @propagated_mount.setter
    def propagated_mount(self, propagated_mount):
        """Sets the propagated_mount of this PluginConfig.

        propagated mount  # noqa: E501

        :param propagated_mount: The propagated_mount of this PluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and propagated_mount is None:  # noqa: E501
            raise ValueError("Invalid value for `propagated_mount`, must not be `None`")  # noqa: E501

        self._propagated_mount = propagated_mount

    @property
    def user(self):
        """Gets the user of this PluginConfig.  # noqa: E501


        :return: The user of this PluginConfig.  # noqa: E501
        :rtype: PluginConfigUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PluginConfig.


        :param user: The user of this PluginConfig.  # noqa: E501
        :type: PluginConfigUser
        """

        self._user = user

    @property
    def work_dir(self):
        """Gets the work_dir of this PluginConfig.  # noqa: E501

        work dir  # noqa: E501

        :return: The work_dir of this PluginConfig.  # noqa: E501
        :rtype: str
        """
        return self._work_dir

    @work_dir.setter
    def work_dir(self, work_dir):
        """Sets the work_dir of this PluginConfig.

        work dir  # noqa: E501

        :param work_dir: The work_dir of this PluginConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and work_dir is None:  # noqa: E501
            raise ValueError("Invalid value for `work_dir`, must not be `None`")  # noqa: E501

        self._work_dir = work_dir

    @property
    def rootfs(self):
        """Gets the rootfs of this PluginConfig.  # noqa: E501


        :return: The rootfs of this PluginConfig.  # noqa: E501
        :rtype: PluginConfigRootfs
        """
        return self._rootfs

    @rootfs.setter
    def rootfs(self, rootfs):
        """Sets the rootfs of this PluginConfig.


        :param rootfs: The rootfs of this PluginConfig.  # noqa: E501
        :type: PluginConfigRootfs
        """

        self._rootfs = rootfs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PluginConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginConfig):
            return True

        return self.to_dict() != other.to_dict()
