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


class JSONBodyConstraint(object):
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
        'name': 'str',
        'exact_match': 'str',
        'match_type': 'str',
        'pointer': 'str'
    }

    attribute_map = {
        'name': 'name',
        'exact_match': 'exact_match',
        'match_type': 'match_type',
        'pointer': 'pointer'
    }

    def __init__(self, name=None, exact_match=None, match_type=None, pointer=None, local_vars_configuration=None):  # noqa: E501
        """JSONBodyConstraint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._exact_match = None
        self._match_type = None
        self._pointer = None
        self.discriminator = None

        self.name = name
        if exact_match is not None:
            self.exact_match = exact_match
        if match_type is not None:
            self.match_type = match_type
        if pointer is not None:
            self.pointer = pointer

    @property
    def name(self):
        """Gets the name of this JSONBodyConstraint.  # noqa: E501

        The name that refers to a specific constraint.  # noqa: E501

        :return: The name of this JSONBodyConstraint.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JSONBodyConstraint.

        The name that refers to a specific constraint.  # noqa: E501

        :param name: The name of this JSONBodyConstraint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def exact_match(self):
        """Gets the exact_match of this JSONBodyConstraint.  # noqa: E501

        The value that's matched against and should be exactly the same to satisfy the rule.  # noqa: E501

        :return: The exact_match of this JSONBodyConstraint.  # noqa: E501
        :rtype: str
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this JSONBodyConstraint.

        The value that's matched against and should be exactly the same to satisfy the rule.  # noqa: E501

        :param exact_match: The exact_match of this JSONBodyConstraint.  # noqa: E501
        :type: str
        """

        self._exact_match = exact_match

    @property
    def match_type(self):
        """Gets the match_type of this JSONBodyConstraint.  # noqa: E501

        The type of the value that's matched against.  # noqa: E501

        :return: The match_type of this JSONBodyConstraint.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this JSONBodyConstraint.

        The type of the value that's matched against.  # noqa: E501

        :param match_type: The match_type of this JSONBodyConstraint.  # noqa: E501
        :type: str
        """
        allowed_values = ["string"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and match_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `match_type` ({0}), must be one of {1}"  # noqa: E501
                .format(match_type, allowed_values)
            )

        self._match_type = match_type

    @property
    def pointer(self):
        """Gets the pointer of this JSONBodyConstraint.  # noqa: E501

        The json pointer path that system follows to store or retrieve data. The pointers are defined in (https://tools.ietf.org/html/rfc6901).   # noqa: E501

        :return: The pointer of this JSONBodyConstraint.  # noqa: E501
        :rtype: str
        """
        return self._pointer

    @pointer.setter
    def pointer(self, pointer):
        """Sets the pointer of this JSONBodyConstraint.

        The json pointer path that system follows to store or retrieve data. The pointers are defined in (https://tools.ietf.org/html/rfc6901).   # noqa: E501

        :param pointer: The pointer of this JSONBodyConstraint.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pointer is not None and not re.search(r'(\/(([^\/~])|(~[01]))*)', pointer)):  # noqa: E501
            raise ValueError(r"Invalid value for `pointer`, must be a follow pattern or equal to `/(\/(([^\/~])|(~[01]))*)/`")  # noqa: E501

        self._pointer = pointer

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
        if not isinstance(other, JSONBodyConstraint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JSONBodyConstraint):
            return True

        return self.to_dict() != other.to_dict()
