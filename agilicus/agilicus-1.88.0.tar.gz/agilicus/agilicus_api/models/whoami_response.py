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


class WhoamiResponse(object):
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
        'token': 'str',
        'orgs': 'list[Organisation]'
    }

    attribute_map = {
        'token': 'token',
        'orgs': 'orgs'
    }

    def __init__(self, token=None, orgs=None, local_vars_configuration=None):  # noqa: E501
        """WhoamiResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._orgs = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if orgs is not None:
            self.orgs = orgs

    @property
    def token(self):
        """Gets the token of this WhoamiResponse.  # noqa: E501

        access token  # noqa: E501

        :return: The token of this WhoamiResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this WhoamiResponse.

        access token  # noqa: E501

        :param token: The token of this WhoamiResponse.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def orgs(self):
        """Gets the orgs of this WhoamiResponse.  # noqa: E501

        list of orgs user belongs to  # noqa: E501

        :return: The orgs of this WhoamiResponse.  # noqa: E501
        :rtype: list[Organisation]
        """
        return self._orgs

    @orgs.setter
    def orgs(self, orgs):
        """Sets the orgs of this WhoamiResponse.

        list of orgs user belongs to  # noqa: E501

        :param orgs: The orgs of this WhoamiResponse.  # noqa: E501
        :type: list[Organisation]
        """

        self._orgs = orgs

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
        if not isinstance(other, WhoamiResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhoamiResponse):
            return True

        return self.to_dict() != other.to_dict()
