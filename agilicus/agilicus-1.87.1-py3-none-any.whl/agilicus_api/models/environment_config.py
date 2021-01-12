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


class EnvironmentConfig(object):
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
        'id': 'str',
        'app_id': 'str',
        'environment_name': 'str',
        'maintenance_org_id': 'str',
        'config_type': 'str',
        'mount_domain': 'str',
        'mount_username': 'str',
        'mount_password': 'str',
        'mount_hostname': 'str',
        'mount_share': 'str',
        'mount_src_path': 'str',
        'mount_path': 'str',
        'file_store_uri': 'str',
        'env_config_vars': 'list[EnvironmentConfigVar]'
    }

    attribute_map = {
        'id': 'id',
        'app_id': 'app_id',
        'environment_name': 'environment_name',
        'maintenance_org_id': 'maintenance_org_id',
        'config_type': 'config_type',
        'mount_domain': 'mount_domain',
        'mount_username': 'mount_username',
        'mount_password': 'mount_password',
        'mount_hostname': 'mount_hostname',
        'mount_share': 'mount_share',
        'mount_src_path': 'mount_src_path',
        'mount_path': 'mount_path',
        'file_store_uri': 'file_store_uri',
        'env_config_vars': 'env_config_vars'
    }

    def __init__(self, id=None, app_id=None, environment_name=None, maintenance_org_id=None, config_type=None, mount_domain=None, mount_username=None, mount_password=None, mount_hostname=None, mount_share=None, mount_src_path=None, mount_path=None, file_store_uri=None, env_config_vars=None, local_vars_configuration=None):  # noqa: E501
        """EnvironmentConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._app_id = None
        self._environment_name = None
        self._maintenance_org_id = None
        self._config_type = None
        self._mount_domain = None
        self._mount_username = None
        self._mount_password = None
        self._mount_hostname = None
        self._mount_share = None
        self._mount_src_path = None
        self._mount_path = None
        self._file_store_uri = None
        self._env_config_vars = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if environment_name is not None:
            self.environment_name = environment_name
        self.maintenance_org_id = maintenance_org_id
        self.config_type = config_type
        if mount_domain is not None:
            self.mount_domain = mount_domain
        if mount_username is not None:
            self.mount_username = mount_username
        if mount_password is not None:
            self.mount_password = mount_password
        if mount_hostname is not None:
            self.mount_hostname = mount_hostname
        if mount_share is not None:
            self.mount_share = mount_share
        if mount_src_path is not None:
            self.mount_src_path = mount_src_path
        if mount_path is not None:
            self.mount_path = mount_path
        if file_store_uri is not None:
            self.file_store_uri = file_store_uri
        if env_config_vars is not None:
            self.env_config_vars = env_config_vars

    @property
    def id(self):
        """Gets the id of this EnvironmentConfig.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentConfig.

        Unique identifier  # noqa: E501

        :param id: The id of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def app_id(self):
        """Gets the app_id of this EnvironmentConfig.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The app_id of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this EnvironmentConfig.

        Unique identifier  # noqa: E501

        :param app_id: The app_id of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def environment_name(self):
        """Gets the environment_name of this EnvironmentConfig.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The environment_name of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this EnvironmentConfig.

        Unique identifier  # noqa: E501

        :param environment_name: The environment_name of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._environment_name = environment_name

    @property
    def maintenance_org_id(self):
        """Gets the maintenance_org_id of this EnvironmentConfig.  # noqa: E501

        The Organisation which is responsibile for maintaining this Environment.   # noqa: E501

        :return: The maintenance_org_id of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_org_id

    @maintenance_org_id.setter
    def maintenance_org_id(self, maintenance_org_id):
        """Sets the maintenance_org_id of this EnvironmentConfig.

        The Organisation which is responsibile for maintaining this Environment.   # noqa: E501

        :param maintenance_org_id: The maintenance_org_id of this EnvironmentConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and maintenance_org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `maintenance_org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                maintenance_org_id is not None and len(maintenance_org_id) > 40):
            raise ValueError("Invalid value for `maintenance_org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                maintenance_org_id is not None and len(maintenance_org_id) < 1):
            raise ValueError("Invalid value for `maintenance_org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._maintenance_org_id = maintenance_org_id

    @property
    def config_type(self):
        """Gets the config_type of this EnvironmentConfig.  # noqa: E501

        configuration type  # noqa: E501

        :return: The config_type of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """Sets the config_type of this EnvironmentConfig.

        configuration type  # noqa: E501

        :param config_type: The config_type of this EnvironmentConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and config_type is None:  # noqa: E501
            raise ValueError("Invalid value for `config_type`, must not be `None`")  # noqa: E501
        allowed_values = ["configmap_mount", "configmap_env", "secret_mount", "secret_env", "file_mount", "mount_smb", "mount_gcs", "mount_tmpdir"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and config_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `config_type` ({0}), must be one of {1}"  # noqa: E501
                .format(config_type, allowed_values)
            )

        self._config_type = config_type

    @property
    def mount_domain(self):
        """Gets the mount_domain of this EnvironmentConfig.  # noqa: E501

        mount user domain  # noqa: E501

        :return: The mount_domain of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_domain

    @mount_domain.setter
    def mount_domain(self, mount_domain):
        """Sets the mount_domain of this EnvironmentConfig.

        mount user domain  # noqa: E501

        :param mount_domain: The mount_domain of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_domain = mount_domain

    @property
    def mount_username(self):
        """Gets the mount_username of this EnvironmentConfig.  # noqa: E501

        mount username  # noqa: E501

        :return: The mount_username of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_username

    @mount_username.setter
    def mount_username(self, mount_username):
        """Sets the mount_username of this EnvironmentConfig.

        mount username  # noqa: E501

        :param mount_username: The mount_username of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_username = mount_username

    @property
    def mount_password(self):
        """Gets the mount_password of this EnvironmentConfig.  # noqa: E501

        mount password  # noqa: E501

        :return: The mount_password of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_password

    @mount_password.setter
    def mount_password(self, mount_password):
        """Sets the mount_password of this EnvironmentConfig.

        mount password  # noqa: E501

        :param mount_password: The mount_password of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_password = mount_password

    @property
    def mount_hostname(self):
        """Gets the mount_hostname of this EnvironmentConfig.  # noqa: E501

        mount hostname  # noqa: E501

        :return: The mount_hostname of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_hostname

    @mount_hostname.setter
    def mount_hostname(self, mount_hostname):
        """Sets the mount_hostname of this EnvironmentConfig.

        mount hostname  # noqa: E501

        :param mount_hostname: The mount_hostname of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_hostname = mount_hostname

    @property
    def mount_share(self):
        """Gets the mount_share of this EnvironmentConfig.  # noqa: E501

        mount share  # noqa: E501

        :return: The mount_share of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_share

    @mount_share.setter
    def mount_share(self, mount_share):
        """Sets the mount_share of this EnvironmentConfig.

        mount share  # noqa: E501

        :param mount_share: The mount_share of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_share = mount_share

    @property
    def mount_src_path(self):
        """Gets the mount_src_path of this EnvironmentConfig.  # noqa: E501

        source mount path  # noqa: E501

        :return: The mount_src_path of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_src_path

    @mount_src_path.setter
    def mount_src_path(self, mount_src_path):
        """Sets the mount_src_path of this EnvironmentConfig.

        source mount path  # noqa: E501

        :param mount_src_path: The mount_src_path of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_src_path = mount_src_path

    @property
    def mount_path(self):
        """Gets the mount_path of this EnvironmentConfig.  # noqa: E501

        destination mount path  # noqa: E501

        :return: The mount_path of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """Sets the mount_path of this EnvironmentConfig.

        destination mount path  # noqa: E501

        :param mount_path: The mount_path of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._mount_path = mount_path

    @property
    def file_store_uri(self):
        """Gets the file_store_uri of this EnvironmentConfig.  # noqa: E501

        files API URI where configuration is located  # noqa: E501

        :return: The file_store_uri of this EnvironmentConfig.  # noqa: E501
        :rtype: str
        """
        return self._file_store_uri

    @file_store_uri.setter
    def file_store_uri(self, file_store_uri):
        """Sets the file_store_uri of this EnvironmentConfig.

        files API URI where configuration is located  # noqa: E501

        :param file_store_uri: The file_store_uri of this EnvironmentConfig.  # noqa: E501
        :type: str
        """

        self._file_store_uri = file_store_uri

    @property
    def env_config_vars(self):
        """Gets the env_config_vars of this EnvironmentConfig.  # noqa: E501

        It stores an array of env_config_var objects(key & value pairs) in API. It provides environment variables to build configmaps and secrets directly.   # noqa: E501

        :return: The env_config_vars of this EnvironmentConfig.  # noqa: E501
        :rtype: list[EnvironmentConfigVar]
        """
        return self._env_config_vars

    @env_config_vars.setter
    def env_config_vars(self, env_config_vars):
        """Sets the env_config_vars of this EnvironmentConfig.

        It stores an array of env_config_var objects(key & value pairs) in API. It provides environment variables to build configmaps and secrets directly.   # noqa: E501

        :param env_config_vars: The env_config_vars of this EnvironmentConfig.  # noqa: E501
        :type: list[EnvironmentConfigVar]
        """

        self._env_config_vars = env_config_vars

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
        if not isinstance(other, EnvironmentConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvironmentConfig):
            return True

        return self.to_dict() != other.to_dict()
