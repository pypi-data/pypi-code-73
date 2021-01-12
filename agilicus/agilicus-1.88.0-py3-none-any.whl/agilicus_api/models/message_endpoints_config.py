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


class MessageEndpointsConfig(object):
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
        'sms': 'object',
        'web_push': 'MessageEndpointTypeWebPush'
    }

    attribute_map = {
        'sms': 'sms',
        'web_push': 'web_push'
    }

    def __init__(self, sms=None, web_push=None, local_vars_configuration=None):  # noqa: E501
        """MessageEndpointsConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sms = None
        self._web_push = None
        self.discriminator = None

        if sms is not None:
            self.sms = sms
        if web_push is not None:
            self.web_push = web_push

    @property
    def sms(self):
        """Gets the sms of this MessageEndpointsConfig.  # noqa: E501

        The configuration of the sms endpoint type.   # noqa: E501

        :return: The sms of this MessageEndpointsConfig.  # noqa: E501
        :rtype: object
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this MessageEndpointsConfig.

        The configuration of the sms endpoint type.   # noqa: E501

        :param sms: The sms of this MessageEndpointsConfig.  # noqa: E501
        :type: object
        """

        self._sms = sms

    @property
    def web_push(self):
        """Gets the web_push of this MessageEndpointsConfig.  # noqa: E501


        :return: The web_push of this MessageEndpointsConfig.  # noqa: E501
        :rtype: MessageEndpointTypeWebPush
        """
        return self._web_push

    @web_push.setter
    def web_push(self, web_push):
        """Sets the web_push of this MessageEndpointsConfig.


        :param web_push: The web_push of this MessageEndpointsConfig.  # noqa: E501
        :type: MessageEndpointTypeWebPush
        """

        self._web_push = web_push

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
        if not isinstance(other, MessageEndpointsConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageEndpointsConfig):
            return True

        return self.to_dict() != other.to_dict()
