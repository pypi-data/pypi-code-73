# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationReplacement(object):
    """
    A record to add to a zone in replacement of contents that cannot be migrated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationReplacement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rtype:
            The value to assign to the rtype property of this MigrationReplacement.
        :type rtype: str

        :param substitute_rtype:
            The value to assign to the substitute_rtype property of this MigrationReplacement.
        :type substitute_rtype: str

        :param ttl:
            The value to assign to the ttl property of this MigrationReplacement.
        :type ttl: int

        :param rdata:
            The value to assign to the rdata property of this MigrationReplacement.
        :type rdata: str

        """
        self.swagger_types = {
            'rtype': 'str',
            'substitute_rtype': 'str',
            'ttl': 'int',
            'rdata': 'str'
        }

        self.attribute_map = {
            'rtype': 'rtype',
            'substitute_rtype': 'substituteRtype',
            'ttl': 'ttl',
            'rdata': 'rdata'
        }

        self._rtype = None
        self._substitute_rtype = None
        self._ttl = None
        self._rdata = None

    @property
    def rtype(self):
        """
        **[Required]** Gets the rtype of this MigrationReplacement.
        The type of DNS record, such as A or CNAME. For more information, see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :return: The rtype of this MigrationReplacement.
        :rtype: str
        """
        return self._rtype

    @rtype.setter
    def rtype(self, rtype):
        """
        Sets the rtype of this MigrationReplacement.
        The type of DNS record, such as A or CNAME. For more information, see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :param rtype: The rtype of this MigrationReplacement.
        :type: str
        """
        self._rtype = rtype

    @property
    def substitute_rtype(self):
        """
        Gets the substitute_rtype of this MigrationReplacement.
        The canonical name for a substitute type of the replacement record to be used if the specified `rtype` is not allowed at the domain. The specified `ttl` and `rdata` will still apply with the substitute type.


        :return: The substitute_rtype of this MigrationReplacement.
        :rtype: str
        """
        return self._substitute_rtype

    @substitute_rtype.setter
    def substitute_rtype(self, substitute_rtype):
        """
        Sets the substitute_rtype of this MigrationReplacement.
        The canonical name for a substitute type of the replacement record to be used if the specified `rtype` is not allowed at the domain. The specified `ttl` and `rdata` will still apply with the substitute type.


        :param substitute_rtype: The substitute_rtype of this MigrationReplacement.
        :type: str
        """
        self._substitute_rtype = substitute_rtype

    @property
    def ttl(self):
        """
        **[Required]** Gets the ttl of this MigrationReplacement.
        The Time To Live of the replacement record, in seconds.


        :return: The ttl of this MigrationReplacement.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this MigrationReplacement.
        The Time To Live of the replacement record, in seconds.


        :param ttl: The ttl of this MigrationReplacement.
        :type: int
        """
        self._ttl = ttl

    @property
    def rdata(self):
        """
        **[Required]** Gets the rdata of this MigrationReplacement.
        The record data of the replacement record, as whitespace-delimited tokens in
        type-specific presentation format.


        :return: The rdata of this MigrationReplacement.
        :rtype: str
        """
        return self._rdata

    @rdata.setter
    def rdata(self, rdata):
        """
        Sets the rdata of this MigrationReplacement.
        The record data of the replacement record, as whitespace-delimited tokens in
        type-specific presentation format.


        :param rdata: The rdata of this MigrationReplacement.
        :type: str
        """
        self._rdata = rdata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
