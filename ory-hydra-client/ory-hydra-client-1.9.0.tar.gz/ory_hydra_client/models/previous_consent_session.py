# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: v1.9.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_hydra_client.configuration import Configuration


class PreviousConsentSession(object):
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
        'consent_request': 'ConsentRequest',
        'grant_access_token_audience': 'list[str]',
        'grant_scope': 'list[str]',
        'handled_at': 'datetime',
        'remember': 'bool',
        'remember_for': 'int',
        'session': 'ConsentRequestSession'
    }

    attribute_map = {
        'consent_request': 'consent_request',
        'grant_access_token_audience': 'grant_access_token_audience',
        'grant_scope': 'grant_scope',
        'handled_at': 'handled_at',
        'remember': 'remember',
        'remember_for': 'remember_for',
        'session': 'session'
    }

    def __init__(self, consent_request=None, grant_access_token_audience=None, grant_scope=None, handled_at=None, remember=None, remember_for=None, session=None, local_vars_configuration=None):  # noqa: E501
        """PreviousConsentSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._consent_request = None
        self._grant_access_token_audience = None
        self._grant_scope = None
        self._handled_at = None
        self._remember = None
        self._remember_for = None
        self._session = None
        self.discriminator = None

        if consent_request is not None:
            self.consent_request = consent_request
        if grant_access_token_audience is not None:
            self.grant_access_token_audience = grant_access_token_audience
        if grant_scope is not None:
            self.grant_scope = grant_scope
        if handled_at is not None:
            self.handled_at = handled_at
        if remember is not None:
            self.remember = remember
        if remember_for is not None:
            self.remember_for = remember_for
        if session is not None:
            self.session = session

    @property
    def consent_request(self):
        """Gets the consent_request of this PreviousConsentSession.  # noqa: E501


        :return: The consent_request of this PreviousConsentSession.  # noqa: E501
        :rtype: ConsentRequest
        """
        return self._consent_request

    @consent_request.setter
    def consent_request(self, consent_request):
        """Sets the consent_request of this PreviousConsentSession.


        :param consent_request: The consent_request of this PreviousConsentSession.  # noqa: E501
        :type: ConsentRequest
        """

        self._consent_request = consent_request

    @property
    def grant_access_token_audience(self):
        """Gets the grant_access_token_audience of this PreviousConsentSession.  # noqa: E501


        :return: The grant_access_token_audience of this PreviousConsentSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._grant_access_token_audience

    @grant_access_token_audience.setter
    def grant_access_token_audience(self, grant_access_token_audience):
        """Sets the grant_access_token_audience of this PreviousConsentSession.


        :param grant_access_token_audience: The grant_access_token_audience of this PreviousConsentSession.  # noqa: E501
        :type: list[str]
        """

        self._grant_access_token_audience = grant_access_token_audience

    @property
    def grant_scope(self):
        """Gets the grant_scope of this PreviousConsentSession.  # noqa: E501


        :return: The grant_scope of this PreviousConsentSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._grant_scope

    @grant_scope.setter
    def grant_scope(self, grant_scope):
        """Sets the grant_scope of this PreviousConsentSession.


        :param grant_scope: The grant_scope of this PreviousConsentSession.  # noqa: E501
        :type: list[str]
        """

        self._grant_scope = grant_scope

    @property
    def handled_at(self):
        """Gets the handled_at of this PreviousConsentSession.  # noqa: E501


        :return: The handled_at of this PreviousConsentSession.  # noqa: E501
        :rtype: datetime
        """
        return self._handled_at

    @handled_at.setter
    def handled_at(self, handled_at):
        """Sets the handled_at of this PreviousConsentSession.


        :param handled_at: The handled_at of this PreviousConsentSession.  # noqa: E501
        :type: datetime
        """

        self._handled_at = handled_at

    @property
    def remember(self):
        """Gets the remember of this PreviousConsentSession.  # noqa: E501

        Remember, if set to true, tells ORY Hydra to remember this consent authorization and reuse it if the same client asks the same user for the same, or a subset of, scope.  # noqa: E501

        :return: The remember of this PreviousConsentSession.  # noqa: E501
        :rtype: bool
        """
        return self._remember

    @remember.setter
    def remember(self, remember):
        """Sets the remember of this PreviousConsentSession.

        Remember, if set to true, tells ORY Hydra to remember this consent authorization and reuse it if the same client asks the same user for the same, or a subset of, scope.  # noqa: E501

        :param remember: The remember of this PreviousConsentSession.  # noqa: E501
        :type: bool
        """

        self._remember = remember

    @property
    def remember_for(self):
        """Gets the remember_for of this PreviousConsentSession.  # noqa: E501

        RememberFor sets how long the consent authorization should be remembered for in seconds. If set to `0`, the authorization will be remembered indefinitely.  # noqa: E501

        :return: The remember_for of this PreviousConsentSession.  # noqa: E501
        :rtype: int
        """
        return self._remember_for

    @remember_for.setter
    def remember_for(self, remember_for):
        """Sets the remember_for of this PreviousConsentSession.

        RememberFor sets how long the consent authorization should be remembered for in seconds. If set to `0`, the authorization will be remembered indefinitely.  # noqa: E501

        :param remember_for: The remember_for of this PreviousConsentSession.  # noqa: E501
        :type: int
        """

        self._remember_for = remember_for

    @property
    def session(self):
        """Gets the session of this PreviousConsentSession.  # noqa: E501


        :return: The session of this PreviousConsentSession.  # noqa: E501
        :rtype: ConsentRequestSession
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this PreviousConsentSession.


        :param session: The session of this PreviousConsentSession.  # noqa: E501
        :type: ConsentRequestSession
        """

        self._session = session

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
        if not isinstance(other, PreviousConsentSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreviousConsentSession):
            return True

        return self.to_dict() != other.to_dict()
