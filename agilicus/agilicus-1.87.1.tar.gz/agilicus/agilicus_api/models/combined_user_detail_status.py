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


class CombinedUserDetailStatus(object):
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
        'user': 'User',
        'mfa_challenge_methods': 'list[MFAChallengeMethod]'
    }

    attribute_map = {
        'user': 'user',
        'mfa_challenge_methods': 'mfa_challenge_methods'
    }

    def __init__(self, user=None, mfa_challenge_methods=None, local_vars_configuration=None):  # noqa: E501
        """CombinedUserDetailStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._mfa_challenge_methods = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if mfa_challenge_methods is not None:
            self.mfa_challenge_methods = mfa_challenge_methods

    @property
    def user(self):
        """Gets the user of this CombinedUserDetailStatus.  # noqa: E501


        :return: The user of this CombinedUserDetailStatus.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CombinedUserDetailStatus.


        :param user: The user of this CombinedUserDetailStatus.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def mfa_challenge_methods(self):
        """Gets the mfa_challenge_methods of this CombinedUserDetailStatus.  # noqa: E501

        The Multifactor authentication challenge methods configured by the user.  # noqa: E501

        :return: The mfa_challenge_methods of this CombinedUserDetailStatus.  # noqa: E501
        :rtype: list[MFAChallengeMethod]
        """
        return self._mfa_challenge_methods

    @mfa_challenge_methods.setter
    def mfa_challenge_methods(self, mfa_challenge_methods):
        """Sets the mfa_challenge_methods of this CombinedUserDetailStatus.

        The Multifactor authentication challenge methods configured by the user.  # noqa: E501

        :param mfa_challenge_methods: The mfa_challenge_methods of this CombinedUserDetailStatus.  # noqa: E501
        :type: list[MFAChallengeMethod]
        """

        self._mfa_challenge_methods = mfa_challenge_methods

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
        if not isinstance(other, CombinedUserDetailStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CombinedUserDetailStatus):
            return True

        return self.to_dict() != other.to_dict()
