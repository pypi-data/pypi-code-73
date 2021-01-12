# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseApex(object):
    """
    Oracle Application Express (APEX) is a low-code development platform that enables you to build scalable, secure enterprise apps, with world-class features. Autonomous Database with the APEX workload type is optimized to support APEX development.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseApex object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param apex_version:
            The value to assign to the apex_version property of this AutonomousDatabaseApex.
        :type apex_version: str

        :param ords_version:
            The value to assign to the ords_version property of this AutonomousDatabaseApex.
        :type ords_version: str

        """
        self.swagger_types = {
            'apex_version': 'str',
            'ords_version': 'str'
        }

        self.attribute_map = {
            'apex_version': 'apexVersion',
            'ords_version': 'ordsVersion'
        }

        self._apex_version = None
        self._ords_version = None

    @property
    def apex_version(self):
        """
        Gets the apex_version of this AutonomousDatabaseApex.
        The Oracle Application Express service version.


        :return: The apex_version of this AutonomousDatabaseApex.
        :rtype: str
        """
        return self._apex_version

    @apex_version.setter
    def apex_version(self, apex_version):
        """
        Sets the apex_version of this AutonomousDatabaseApex.
        The Oracle Application Express service version.


        :param apex_version: The apex_version of this AutonomousDatabaseApex.
        :type: str
        """
        self._apex_version = apex_version

    @property
    def ords_version(self):
        """
        Gets the ords_version of this AutonomousDatabaseApex.
        The Oracle REST Data Services (ORDS) version.


        :return: The ords_version of this AutonomousDatabaseApex.
        :rtype: str
        """
        return self._ords_version

    @ords_version.setter
    def ords_version(self, ords_version):
        """
        Sets the ords_version of this AutonomousDatabaseApex.
        The Oracle REST Data Services (ORDS) version.


        :param ords_version: The ords_version of this AutonomousDatabaseApex.
        :type: str
        """
        self._ords_version = ords_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
