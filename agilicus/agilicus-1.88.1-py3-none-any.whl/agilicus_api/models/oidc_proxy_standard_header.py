# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.12
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class OIDCProxyStandardHeader(object):
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
        'location': 'bool',
        'origin': 'bool',
        'host': 'bool'
    }

    attribute_map = {
        'location': 'location',
        'origin': 'origin',
        'host': 'host'
    }

    def __init__(self, location=True, origin=True, host=True, local_vars_configuration=None):  # noqa: E501
        """OIDCProxyStandardHeader - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._origin = None
        self._host = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if origin is not None:
            self.origin = origin
        if host is not None:
            self.host = host

    @property
    def location(self):
        """Gets the location of this OIDCProxyStandardHeader.  # noqa: E501

        If the location flag is set to true, the location field will be automatically rewritten.  # noqa: E501

        :return: The location of this OIDCProxyStandardHeader.  # noqa: E501
        :rtype: bool
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this OIDCProxyStandardHeader.

        If the location flag is set to true, the location field will be automatically rewritten.  # noqa: E501

        :param location: The location of this OIDCProxyStandardHeader.  # noqa: E501
        :type: bool
        """

        self._location = location

    @property
    def origin(self):
        """Gets the origin of this OIDCProxyStandardHeader.  # noqa: E501

        If the origin flag is set to true, the origin field will be automatically rewritten.  # noqa: E501

        :return: The origin of this OIDCProxyStandardHeader.  # noqa: E501
        :rtype: bool
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OIDCProxyStandardHeader.

        If the origin flag is set to true, the origin field will be automatically rewritten.  # noqa: E501

        :param origin: The origin of this OIDCProxyStandardHeader.  # noqa: E501
        :type: bool
        """

        self._origin = origin

    @property
    def host(self):
        """Gets the host of this OIDCProxyStandardHeader.  # noqa: E501

        If the host flag is set to true, the host field will be automatically rewritten.  # noqa: E501

        :return: The host of this OIDCProxyStandardHeader.  # noqa: E501
        :rtype: bool
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this OIDCProxyStandardHeader.

        If the host flag is set to true, the host field will be automatically rewritten.  # noqa: E501

        :param host: The host of this OIDCProxyStandardHeader.  # noqa: E501
        :type: bool
        """

        self._host = host

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
        if not isinstance(other, OIDCProxyStandardHeader):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OIDCProxyStandardHeader):
            return True

        return self.to_dict() != other.to_dict()
