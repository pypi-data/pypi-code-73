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


class UserApplicationAccessInfoStatus(object):
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
        'user_id': 'str',
        'org_id': 'str',
        'org_name': 'str',
        'parent_org_id': 'str',
        'parent_org_name': 'str',
        'application_name': 'str',
        'application_url': 'str',
        'application_description': 'str',
        'application_category': 'str',
        'icon_url': 'str',
        'access_level': 'str',
        'application_default_role_name': 'str',
        'application_default_role_id': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'org_id': 'org_id',
        'org_name': 'org_name',
        'parent_org_id': 'parent_org_id',
        'parent_org_name': 'parent_org_name',
        'application_name': 'application_name',
        'application_url': 'application_url',
        'application_description': 'application_description',
        'application_category': 'application_category',
        'icon_url': 'icon_url',
        'access_level': 'access_level',
        'application_default_role_name': 'application_default_role_name',
        'application_default_role_id': 'application_default_role_id',
        'roles': 'roles'
    }

    def __init__(self, user_id=None, org_id=None, org_name=None, parent_org_id=None, parent_org_name=None, application_name=None, application_url=None, application_description=None, application_category=None, icon_url='https://storage.googleapis.com/agilicus/logo.svg', access_level=None, application_default_role_name=None, application_default_role_id=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """UserApplicationAccessInfoStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._org_id = None
        self._org_name = None
        self._parent_org_id = None
        self._parent_org_name = None
        self._application_name = None
        self._application_url = None
        self._application_description = None
        self._application_category = None
        self._icon_url = None
        self._access_level = None
        self._application_default_role_name = None
        self._application_default_role_id = None
        self._roles = None
        self.discriminator = None

        self.user_id = user_id
        self.org_id = org_id
        self.org_name = org_name
        if parent_org_id is not None:
            self.parent_org_id = parent_org_id
        if parent_org_name is not None:
            self.parent_org_name = parent_org_name
        self.application_name = application_name
        self.application_url = application_url
        if application_description is not None:
            self.application_description = application_description
        if application_category is not None:
            self.application_category = application_category
        if icon_url is not None:
            self.icon_url = icon_url
        self.access_level = access_level
        self.application_default_role_name = application_default_role_name
        self.application_default_role_id = application_default_role_id
        if roles is not None:
            self.roles = roles

    @property
    def user_id(self):
        """Gets the user_id of this UserApplicationAccessInfoStatus.  # noqa: E501

        The unique id of the User to which this record applies.   # noqa: E501

        :return: The user_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserApplicationAccessInfoStatus.

        The unique id of the User to which this record applies.   # noqa: E501

        :param user_id: The user_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) > 40):
            raise ValueError("Invalid value for `user_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 1):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id = user_id

    @property
    def org_id(self):
        """Gets the org_id of this UserApplicationAccessInfoStatus.  # noqa: E501

        The unique id of the Organisation to which this record applies.   # noqa: E501

        :return: The org_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this UserApplicationAccessInfoStatus.

        The unique id of the Organisation to which this record applies.   # noqa: E501

        :param org_id: The org_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) > 40):
            raise ValueError("Invalid value for `org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) < 1):
            raise ValueError("Invalid value for `org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._org_id = org_id

    @property
    def org_name(self):
        """Gets the org_name of this UserApplicationAccessInfoStatus.  # noqa: E501

        The name of Organisation to which this record applies.   # noqa: E501

        :return: The org_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this UserApplicationAccessInfoStatus.

        The name of Organisation to which this record applies.   # noqa: E501

        :param org_name: The org_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_name is None:  # noqa: E501
            raise ValueError("Invalid value for `org_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_name is not None and len(org_name) > 100):
            raise ValueError("Invalid value for `org_name`, length must be less than or equal to `100`")  # noqa: E501

        self._org_name = org_name

    @property
    def parent_org_id(self):
        """Gets the parent_org_id of this UserApplicationAccessInfoStatus.  # noqa: E501

        The unique id of the parent of the Organisation to which this record applies. Omitted if the Organisation has no parent.   # noqa: E501

        :return: The parent_org_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._parent_org_id

    @parent_org_id.setter
    def parent_org_id(self, parent_org_id):
        """Sets the parent_org_id of this UserApplicationAccessInfoStatus.

        The unique id of the parent of the Organisation to which this record applies. Omitted if the Organisation has no parent.   # noqa: E501

        :param parent_org_id: The parent_org_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                parent_org_id is not None and len(parent_org_id) > 40):
            raise ValueError("Invalid value for `parent_org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                parent_org_id is not None and len(parent_org_id) < 1):
            raise ValueError("Invalid value for `parent_org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._parent_org_id = parent_org_id

    @property
    def parent_org_name(self):
        """Gets the parent_org_name of this UserApplicationAccessInfoStatus.  # noqa: E501

        The name of the parent of the Organisation to which this record applies. Omitted if the Organisation has no parent.   # noqa: E501

        :return: The parent_org_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._parent_org_name

    @parent_org_name.setter
    def parent_org_name(self, parent_org_name):
        """Sets the parent_org_name of this UserApplicationAccessInfoStatus.

        The name of the parent of the Organisation to which this record applies. Omitted if the Organisation has no parent.   # noqa: E501

        :param parent_org_name: The parent_org_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                parent_org_name is not None and len(parent_org_name) > 100):
            raise ValueError("Invalid value for `parent_org_name`, length must be less than or equal to `100`")  # noqa: E501

        self._parent_org_name = parent_org_name

    @property
    def application_name(self):
        """Gets the application_name of this UserApplicationAccessInfoStatus.  # noqa: E501

        The name of the application.   # noqa: E501

        :return: The application_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this UserApplicationAccessInfoStatus.

        The name of the application.   # noqa: E501

        :param application_name: The application_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_name is None:  # noqa: E501
            raise ValueError("Invalid value for `application_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_name is not None and len(application_name) > 128):
            raise ValueError("Invalid value for `application_name`, length must be less than or equal to `128`")  # noqa: E501

        self._application_name = application_name

    @property
    def application_url(self):
        """Gets the application_url of this UserApplicationAccessInfoStatus.  # noqa: E501

        The url of the application   # noqa: E501

        :return: The application_url of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_url

    @application_url.setter
    def application_url(self, application_url):
        """Sets the application_url of this UserApplicationAccessInfoStatus.

        The url of the application   # noqa: E501

        :param application_url: The application_url of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_url is None:  # noqa: E501
            raise ValueError("Invalid value for `application_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_url is not None and len(application_url) > 1024):
            raise ValueError("Invalid value for `application_url`, length must be less than or equal to `1024`")  # noqa: E501

        self._application_url = application_url

    @property
    def application_description(self):
        """Gets the application_description of this UserApplicationAccessInfoStatus.  # noqa: E501

        The description of the application   # noqa: E501

        :return: The application_description of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_description

    @application_description.setter
    def application_description(self, application_description):
        """Sets the application_description of this UserApplicationAccessInfoStatus.

        The description of the application   # noqa: E501

        :param application_description: The application_description of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """

        self._application_description = application_description

    @property
    def application_category(self):
        """Gets the application_category of this UserApplicationAccessInfoStatus.  # noqa: E501

        A category used to group similar applications together   # noqa: E501

        :return: The application_category of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_category

    @application_category.setter
    def application_category(self, application_category):
        """Sets the application_category of this UserApplicationAccessInfoStatus.

        A category used to group similar applications together   # noqa: E501

        :param application_category: The application_category of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                application_category is not None and len(application_category) > 100):
            raise ValueError("Invalid value for `application_category`, length must be less than or equal to `100`")  # noqa: E501

        self._application_category = application_category

    @property
    def icon_url(self):
        """Gets the icon_url of this UserApplicationAccessInfoStatus.  # noqa: E501

        A url pointing to an icon representing this application.   # noqa: E501

        :return: The icon_url of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this UserApplicationAccessInfoStatus.

        A url pointing to an icon representing this application.   # noqa: E501

        :param icon_url: The icon_url of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                icon_url is not None and len(icon_url) > 100):
            raise ValueError("Invalid value for `icon_url`, length must be less than or equal to `100`")  # noqa: E501

        self._icon_url = icon_url

    @property
    def access_level(self):
        """Gets the access_level of this UserApplicationAccessInfoStatus.  # noqa: E501

        Whether the user has access, has requested access, etc. The possible values have the following meanings:   - requested: the user has requested access to this instance.   - granted: the user has access to this instance.   - none: the user has no relation to this application.   # noqa: E501

        :return: The access_level of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this UserApplicationAccessInfoStatus.

        Whether the user has access, has requested access, etc. The possible values have the following meanings:   - requested: the user has requested access to this instance.   - granted: the user has access to this instance.   - none: the user has no relation to this application.   # noqa: E501

        :param access_level: The access_level of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_level is None:  # noqa: E501
            raise ValueError("Invalid value for `access_level`, must not be `None`")  # noqa: E501
        allowed_values = ["requested", "granted", "none"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and access_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `access_level` ({0}), must be one of {1}"  # noqa: E501
                .format(access_level, allowed_values)
            )

        self._access_level = access_level

    @property
    def application_default_role_name(self):
        """Gets the application_default_role_name of this UserApplicationAccessInfoStatus.  # noqa: E501

        The name of the default role of the application. This will be granted to users by default when their access request has been approved.   # noqa: E501

        :return: The application_default_role_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_default_role_name

    @application_default_role_name.setter
    def application_default_role_name(self, application_default_role_name):
        """Sets the application_default_role_name of this UserApplicationAccessInfoStatus.

        The name of the default role of the application. This will be granted to users by default when their access request has been approved.   # noqa: E501

        :param application_default_role_name: The application_default_role_name of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                application_default_role_name is not None and len(application_default_role_name) > 100):
            raise ValueError("Invalid value for `application_default_role_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_default_role_name is not None and len(application_default_role_name) < 1):
            raise ValueError("Invalid value for `application_default_role_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._application_default_role_name = application_default_role_name

    @property
    def application_default_role_id(self):
        """Gets the application_default_role_id of this UserApplicationAccessInfoStatus.  # noqa: E501

        The unique id the default role of the application. This will be granted to users by default when their access request has been approved.   # noqa: E501

        :return: The application_default_role_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: str
        """
        return self._application_default_role_id

    @application_default_role_id.setter
    def application_default_role_id(self, application_default_role_id):
        """Sets the application_default_role_id of this UserApplicationAccessInfoStatus.

        The unique id the default role of the application. This will be granted to users by default when their access request has been approved.   # noqa: E501

        :param application_default_role_id: The application_default_role_id of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                application_default_role_id is not None and len(application_default_role_id) > 40):
            raise ValueError("Invalid value for `application_default_role_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_default_role_id is not None and len(application_default_role_id) < 1):
            raise ValueError("Invalid value for `application_default_role_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._application_default_role_id = application_default_role_id

    @property
    def roles(self):
        """Gets the roles of this UserApplicationAccessInfoStatus.  # noqa: E501

        The list of roles held by the user for the given application  # noqa: E501

        :return: The roles of this UserApplicationAccessInfoStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserApplicationAccessInfoStatus.

        The list of roles held by the user for the given application  # noqa: E501

        :param roles: The roles of this UserApplicationAccessInfoStatus.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

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
        if not isinstance(other, UserApplicationAccessInfoStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserApplicationAccessInfoStatus):
            return True

        return self.to_dict() != other.to_dict()
