# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Backend(object):
    """
    The configuration of a backend server that is a member of a load balancer backend set.
    For more information, see `Managing Backend Servers`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendservers.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Backend object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Backend.
        :type name: str

        :param ip_address:
            The value to assign to the ip_address property of this Backend.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this Backend.
        :type port: int

        :param weight:
            The value to assign to the weight property of this Backend.
        :type weight: int

        :param drain:
            The value to assign to the drain property of this Backend.
        :type drain: bool

        :param backup:
            The value to assign to the backup property of this Backend.
        :type backup: bool

        :param offline:
            The value to assign to the offline property of this Backend.
        :type offline: bool

        """
        self.swagger_types = {
            'name': 'str',
            'ip_address': 'str',
            'port': 'int',
            'weight': 'int',
            'drain': 'bool',
            'backup': 'bool',
            'offline': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'ip_address': 'ipAddress',
            'port': 'port',
            'weight': 'weight',
            'drain': 'drain',
            'backup': 'backup',
            'offline': 'offline'
        }

        self._name = None
        self._ip_address = None
        self._port = None
        self._weight = None
        self._drain = None
        self._backup = None
        self._offline = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Backend.
        A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.

        Example: `10.0.0.3:8080`


        :return: The name of this Backend.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Backend.
        A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.

        Example: `10.0.0.3:8080`


        :param name: The name of this Backend.
        :type: str
        """
        self._name = name

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this Backend.
        The IP address of the backend server.

        Example: `10.0.0.3`


        :return: The ip_address of this Backend.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Backend.
        The IP address of the backend server.

        Example: `10.0.0.3`


        :param ip_address: The ip_address of this Backend.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Backend.
        The communication port for the backend server.

        Example: `8080`


        :return: The port of this Backend.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Backend.
        The communication port for the backend server.

        Example: `8080`


        :param port: The port of this Backend.
        :type: int
        """
        self._port = port

    @property
    def weight(self):
        """
        **[Required]** Gets the weight of this Backend.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
        as a server weighted '1'.
        For more information on load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :return: The weight of this Backend.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Backend.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
        as a server weighted '1'.
        For more information on load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :param weight: The weight of this Backend.
        :type: int
        """
        self._weight = weight

    @property
    def drain(self):
        """
        **[Required]** Gets the drain of this Backend.
        Whether the load balancer should drain this server. Servers marked \"drain\" receive no new
        incoming traffic.

        Example: `false`


        :return: The drain of this Backend.
        :rtype: bool
        """
        return self._drain

    @drain.setter
    def drain(self, drain):
        """
        Sets the drain of this Backend.
        Whether the load balancer should drain this server. Servers marked \"drain\" receive no new
        incoming traffic.

        Example: `false`


        :param drain: The drain of this Backend.
        :type: bool
        """
        self._drain = drain

    @property
    def backup(self):
        """
        **[Required]** Gets the backup of this Backend.
        Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

        **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.

        Example: `false`


        :return: The backup of this Backend.
        :rtype: bool
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """
        Sets the backup of this Backend.
        Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

        **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.

        Example: `false`


        :param backup: The backup of this Backend.
        :type: bool
        """
        self._backup = backup

    @property
    def offline(self):
        """
        **[Required]** Gets the offline of this Backend.
        Whether the load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :return: The offline of this Backend.
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """
        Sets the offline of this Backend.
        Whether the load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :param offline: The offline of this Backend.
        :type: bool
        """
        self._offline = offline

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
