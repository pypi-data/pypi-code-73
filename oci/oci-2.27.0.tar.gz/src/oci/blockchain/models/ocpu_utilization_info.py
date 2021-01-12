# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OcpuUtilizationInfo(object):
    """
    Ocpu utilization for a VM host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OcpuUtilizationInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host:
            The value to assign to the host property of this OcpuUtilizationInfo.
        :type host: str

        :param ocpu_utilization_number:
            The value to assign to the ocpu_utilization_number property of this OcpuUtilizationInfo.
        :type ocpu_utilization_number: float

        :param ocpu_capacity_number:
            The value to assign to the ocpu_capacity_number property of this OcpuUtilizationInfo.
        :type ocpu_capacity_number: float

        """
        self.swagger_types = {
            'host': 'str',
            'ocpu_utilization_number': 'float',
            'ocpu_capacity_number': 'float'
        }

        self.attribute_map = {
            'host': 'host',
            'ocpu_utilization_number': 'ocpuUtilizationNumber',
            'ocpu_capacity_number': 'ocpuCapacityNumber'
        }

        self._host = None
        self._ocpu_utilization_number = None
        self._ocpu_capacity_number = None

    @property
    def host(self):
        """
        Gets the host of this OcpuUtilizationInfo.
        Host name of VM


        :return: The host of this OcpuUtilizationInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this OcpuUtilizationInfo.
        Host name of VM


        :param host: The host of this OcpuUtilizationInfo.
        :type: str
        """
        self._host = host

    @property
    def ocpu_utilization_number(self):
        """
        Gets the ocpu_utilization_number of this OcpuUtilizationInfo.
        Number of OCPU utilized


        :return: The ocpu_utilization_number of this OcpuUtilizationInfo.
        :rtype: float
        """
        return self._ocpu_utilization_number

    @ocpu_utilization_number.setter
    def ocpu_utilization_number(self, ocpu_utilization_number):
        """
        Sets the ocpu_utilization_number of this OcpuUtilizationInfo.
        Number of OCPU utilized


        :param ocpu_utilization_number: The ocpu_utilization_number of this OcpuUtilizationInfo.
        :type: float
        """
        self._ocpu_utilization_number = ocpu_utilization_number

    @property
    def ocpu_capacity_number(self):
        """
        Gets the ocpu_capacity_number of this OcpuUtilizationInfo.
        Number of total OCPU capacity on the host


        :return: The ocpu_capacity_number of this OcpuUtilizationInfo.
        :rtype: float
        """
        return self._ocpu_capacity_number

    @ocpu_capacity_number.setter
    def ocpu_capacity_number(self, ocpu_capacity_number):
        """
        Sets the ocpu_capacity_number of this OcpuUtilizationInfo.
        Number of total OCPU capacity on the host


        :param ocpu_capacity_number: The ocpu_capacity_number of this OcpuUtilizationInfo.
        :type: float
        """
        self._ocpu_capacity_number = ocpu_capacity_number

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
