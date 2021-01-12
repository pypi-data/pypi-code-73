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

class GetRecipeResponse(object):
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
        'href': 'str',
        'value': 'ConfigurationRecipe',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'value': 'value',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'value': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, value=None, links=None):  # noqa: E501
        """
        GetRecipeResponse - a model defined in OpenAPI

        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param value: 
        :type value: lusid.ConfigurationRecipe
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._value = None
        self._links = None
        self.discriminator = None

        self.href = href
        if value is not None:
            self.value = value
        self.links = links

    @property
    def href(self):
        """Gets the href of this GetRecipeResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this GetRecipeResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this GetRecipeResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this GetRecipeResponse.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def value(self):
        """Gets the value of this GetRecipeResponse.  # noqa: E501


        :return: The value of this GetRecipeResponse.  # noqa: E501
        :rtype: ConfigurationRecipe
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetRecipeResponse.


        :param value: The value of this GetRecipeResponse.  # noqa: E501
        :type: ConfigurationRecipe
        """

        self._value = value

    @property
    def links(self):
        """Gets the links of this GetRecipeResponse.  # noqa: E501


        :return: The links of this GetRecipeResponse.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GetRecipeResponse.


        :param links: The links of this GetRecipeResponse.  # noqa: E501
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
        if not isinstance(other, GetRecipeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
