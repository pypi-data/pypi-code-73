# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.11
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class SecureAgentConnector(object):
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
        'max_number_connections': 'int',
        'connection_uri': 'str'
    }

    attribute_map = {
        'max_number_connections': 'max_number_connections',
        'connection_uri': 'connection_uri'
    }

    def __init__(self, max_number_connections=None, connection_uri=None, local_vars_configuration=None):  # noqa: E501
        """SecureAgentConnector - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_number_connections = None
        self._connection_uri = None
        self.discriminator = None

        self.max_number_connections = max_number_connections
        if connection_uri is not None:
            self.connection_uri = connection_uri

    @property
    def max_number_connections(self):
        """Gets the max_number_connections of this SecureAgentConnector.  # noqa: E501

        The maximum number of connections to maintain to the cluster when stable. Note that this value may be exceeded during times of reconfiguration. A value of zero means that the connector is effectively unused by this Secure Agent.   # noqa: E501

        :return: The max_number_connections of this SecureAgentConnector.  # noqa: E501
        :rtype: int
        """
        return self._max_number_connections

    @max_number_connections.setter
    def max_number_connections(self, max_number_connections):
        """Sets the max_number_connections of this SecureAgentConnector.

        The maximum number of connections to maintain to the cluster when stable. Note that this value may be exceeded during times of reconfiguration. A value of zero means that the connector is effectively unused by this Secure Agent.   # noqa: E501

        :param max_number_connections: The max_number_connections of this SecureAgentConnector.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_number_connections is None:  # noqa: E501
            raise ValueError("Invalid value for `max_number_connections`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_number_connections is not None and max_number_connections > 64):  # noqa: E501
            raise ValueError("Invalid value for `max_number_connections`, must be a value less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_number_connections is not None and max_number_connections < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_number_connections`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_number_connections = max_number_connections

    @property
    def connection_uri(self):
        """Gets the connection_uri of this SecureAgentConnector.  # noqa: E501

        Overrides the default URI used to connect to this connector. This can be used to point the Secure Agent somewhere other than the default.   # noqa: E501

        :return: The connection_uri of this SecureAgentConnector.  # noqa: E501
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """Sets the connection_uri of this SecureAgentConnector.

        Overrides the default URI used to connect to this connector. This can be used to point the Secure Agent somewhere other than the default.   # noqa: E501

        :param connection_uri: The connection_uri of this SecureAgentConnector.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                connection_uri is not None and len(connection_uri) > 1024):
            raise ValueError("Invalid value for `connection_uri`, length must be less than or equal to `1024`")  # noqa: E501

        self._connection_uri = connection_uri

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
        if not isinstance(other, SecureAgentConnector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecureAgentConnector):
            return True

        return self.to_dict() != other.to_dict()
