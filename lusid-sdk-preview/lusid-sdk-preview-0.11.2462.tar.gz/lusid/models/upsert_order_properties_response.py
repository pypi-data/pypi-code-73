# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2462
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertOrderPropertiesResponse(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'as_at_date': 'datetime',
        'links': 'list[Link]'
    }

    attribute_map = {
        'as_at_date': 'asAtDate',
        'links': 'links'
    }

    required_map = {
        'as_at_date': 'required',
        'links': 'optional'
    }

    def __init__(self, as_at_date=None, links=None):  # noqa: E501
        """
        UpsertOrderPropertiesResponse - a model defined in OpenAPI

        :param as_at_date:  The asAt datetime that the order was added to LUSID. (required)
        :type as_at_date: datetime
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._as_at_date = None
        self._links = None
        self.discriminator = None

        self.as_at_date = as_at_date
        self.links = links

    @property
    def as_at_date(self):
        """Gets the as_at_date of this UpsertOrderPropertiesResponse.  # noqa: E501

        The asAt datetime that the order was added to LUSID.  # noqa: E501

        :return: The as_at_date of this UpsertOrderPropertiesResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at_date

    @as_at_date.setter
    def as_at_date(self, as_at_date):
        """Sets the as_at_date of this UpsertOrderPropertiesResponse.

        The asAt datetime that the order was added to LUSID.  # noqa: E501

        :param as_at_date: The as_at_date of this UpsertOrderPropertiesResponse.  # noqa: E501
        :type: datetime
        """
        if as_at_date is None:
            raise ValueError("Invalid value for `as_at_date`, must not be `None`")  # noqa: E501

        self._as_at_date = as_at_date

    @property
    def links(self):
        """Gets the links of this UpsertOrderPropertiesResponse.  # noqa: E501


        :return: The links of this UpsertOrderPropertiesResponse.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpsertOrderPropertiesResponse.


        :param links: The links of this UpsertOrderPropertiesResponse.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, UpsertOrderPropertiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
