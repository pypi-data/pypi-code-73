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


class MFAEnrollmentQuestionLoginInfo(object):
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
        'issuer_org_id': 'str',
        'enrollment_expiry': 'datetime',
        'user_mfa_methods': 'list[str]'
    }

    attribute_map = {
        'issuer_org_id': 'issuer_org_id',
        'enrollment_expiry': 'enrollment_expiry',
        'user_mfa_methods': 'user_mfa_methods'
    }

    def __init__(self, issuer_org_id=None, enrollment_expiry=None, user_mfa_methods=None, local_vars_configuration=None):  # noqa: E501
        """MFAEnrollmentQuestionLoginInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._issuer_org_id = None
        self._enrollment_expiry = None
        self._user_mfa_methods = None
        self.discriminator = None

        self.issuer_org_id = issuer_org_id
        self.enrollment_expiry = enrollment_expiry
        self.user_mfa_methods = user_mfa_methods

    @property
    def issuer_org_id(self):
        """Gets the issuer_org_id of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501

        The id of the organisation for the issuer the user is logging in through. This determines what policy to query  # noqa: E501

        :return: The issuer_org_id of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._issuer_org_id

    @issuer_org_id.setter
    def issuer_org_id(self, issuer_org_id):
        """Sets the issuer_org_id of this MFAEnrollmentQuestionLoginInfo.

        The id of the organisation for the issuer the user is logging in through. This determines what policy to query  # noqa: E501

        :param issuer_org_id: The issuer_org_id of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issuer_org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer_org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issuer_org_id is not None and len(issuer_org_id) > 40):
            raise ValueError("Invalid value for `issuer_org_id`, length must be less than or equal to `40`")  # noqa: E501

        self._issuer_org_id = issuer_org_id

    @property
    def enrollment_expiry(self):
        """Gets the enrollment_expiry of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501

        The expiry time for multi-factor authentication enrollment. Requests to enroll outside this time bound will be denied.  # noqa: E501

        :return: The enrollment_expiry of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._enrollment_expiry

    @enrollment_expiry.setter
    def enrollment_expiry(self, enrollment_expiry):
        """Sets the enrollment_expiry of this MFAEnrollmentQuestionLoginInfo.

        The expiry time for multi-factor authentication enrollment. Requests to enroll outside this time bound will be denied.  # noqa: E501

        :param enrollment_expiry: The enrollment_expiry of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and enrollment_expiry is None:  # noqa: E501
            raise ValueError("Invalid value for `enrollment_expiry`, must not be `None`")  # noqa: E501

        self._enrollment_expiry = enrollment_expiry

    @property
    def user_mfa_methods(self):
        """Gets the user_mfa_methods of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501

        The list of multi-factor challenge methods the user has set up.  # noqa: E501

        :return: The user_mfa_methods of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_mfa_methods

    @user_mfa_methods.setter
    def user_mfa_methods(self, user_mfa_methods):
        """Sets the user_mfa_methods of this MFAEnrollmentQuestionLoginInfo.

        The list of multi-factor challenge methods the user has set up.  # noqa: E501

        :param user_mfa_methods: The user_mfa_methods of this MFAEnrollmentQuestionLoginInfo.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and user_mfa_methods is None:  # noqa: E501
            raise ValueError("Invalid value for `user_mfa_methods`, must not be `None`")  # noqa: E501

        self._user_mfa_methods = user_mfa_methods

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
        if not isinstance(other, MFAEnrollmentQuestionLoginInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MFAEnrollmentQuestionLoginInfo):
            return True

        return self.to_dict() != other.to_dict()
