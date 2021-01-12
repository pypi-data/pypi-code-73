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


class OIDCProxyDomainSubstitution(object):
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
        'standard_headers': 'OIDCProxyStandardHeader',
        'other_headers': 'list[OIDCProxyHeaderMapping]'
    }

    attribute_map = {
        'standard_headers': 'standard_headers',
        'other_headers': 'other_headers'
    }

    def __init__(self, standard_headers=None, other_headers=None, local_vars_configuration=None):  # noqa: E501
        """OIDCProxyDomainSubstitution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._standard_headers = None
        self._other_headers = None
        self.discriminator = None

        if standard_headers is not None:
            self.standard_headers = standard_headers
        if other_headers is not None:
            self.other_headers = other_headers

    @property
    def standard_headers(self):
        """Gets the standard_headers of this OIDCProxyDomainSubstitution.  # noqa: E501


        :return: The standard_headers of this OIDCProxyDomainSubstitution.  # noqa: E501
        :rtype: OIDCProxyStandardHeader
        """
        return self._standard_headers

    @standard_headers.setter
    def standard_headers(self, standard_headers):
        """Sets the standard_headers of this OIDCProxyDomainSubstitution.


        :param standard_headers: The standard_headers of this OIDCProxyDomainSubstitution.  # noqa: E501
        :type: OIDCProxyStandardHeader
        """

        self._standard_headers = standard_headers

    @property
    def other_headers(self):
        """Gets the other_headers of this OIDCProxyDomainSubstitution.  # noqa: E501

        The list of other headers that need to be substituted.  # noqa: E501

        :return: The other_headers of this OIDCProxyDomainSubstitution.  # noqa: E501
        :rtype: list[OIDCProxyHeaderMapping]
        """
        return self._other_headers

    @other_headers.setter
    def other_headers(self, other_headers):
        """Sets the other_headers of this OIDCProxyDomainSubstitution.

        The list of other headers that need to be substituted.  # noqa: E501

        :param other_headers: The other_headers of this OIDCProxyDomainSubstitution.  # noqa: E501
        :type: list[OIDCProxyHeaderMapping]
        """

        self._other_headers = other_headers

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
        if not isinstance(other, OIDCProxyDomainSubstitution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OIDCProxyDomainSubstitution):
            return True

        return self.to_dict() != other.to_dict()
