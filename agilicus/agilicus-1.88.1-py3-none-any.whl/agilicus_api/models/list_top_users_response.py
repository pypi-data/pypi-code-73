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


class ListTopUsersResponse(object):
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
        'top_users': 'list[UserMetrics]',
        'limit': 'int'
    }

    attribute_map = {
        'top_users': 'top_users',
        'limit': 'limit'
    }

    def __init__(self, top_users=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """ListTopUsersResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._top_users = None
        self._limit = None
        self.discriminator = None

        if top_users is not None:
            self.top_users = top_users
        self.limit = limit

    @property
    def top_users(self):
        """Gets the top_users of this ListTopUsersResponse.  # noqa: E501

        List of top users  # noqa: E501

        :return: The top_users of this ListTopUsersResponse.  # noqa: E501
        :rtype: list[UserMetrics]
        """
        return self._top_users

    @top_users.setter
    def top_users(self, top_users):
        """Sets the top_users of this ListTopUsersResponse.

        List of top users  # noqa: E501

        :param top_users: The top_users of this ListTopUsersResponse.  # noqa: E501
        :type: list[UserMetrics]
        """

        self._top_users = top_users

    @property
    def limit(self):
        """Gets the limit of this ListTopUsersResponse.  # noqa: E501

        Limit on number of users in response  # noqa: E501

        :return: The limit of this ListTopUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTopUsersResponse.

        Limit on number of users in response  # noqa: E501

        :param limit: The limit of this ListTopUsersResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

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
        if not isinstance(other, ListTopUsersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListTopUsersResponse):
            return True

        return self.to_dict() != other.to_dict()
