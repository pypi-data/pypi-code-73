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


class Environment(object):
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
        'created': 'datetime',
        'name': 'str',
        'maintenance_org_id': 'str',
        'domain_aliases': 'list[str]',
        'version_tag': 'str',
        'config_mount_path': 'str',
        'config_as_mount': 'str',
        'config_as_env': 'str',
        'secrets_mount_path': 'str',
        'secrets_as_mount': 'str',
        'secrets_as_env': 'str',
        'application_services': 'list[ApplicationService]',
        'serverless_image': 'str',
        'status': 'EnvironmentStatus',
        'updated': 'datetime',
        'application_configs': 'ApplicationConfig'
    }

    attribute_map = {
        'created': 'created',
        'name': 'name',
        'maintenance_org_id': 'maintenance_org_id',
        'domain_aliases': 'domain_aliases',
        'version_tag': 'version_tag',
        'config_mount_path': 'config_mount_path',
        'config_as_mount': 'config_as_mount',
        'config_as_env': 'config_as_env',
        'secrets_mount_path': 'secrets_mount_path',
        'secrets_as_mount': 'secrets_as_mount',
        'secrets_as_env': 'secrets_as_env',
        'application_services': 'application_services',
        'serverless_image': 'serverless_image',
        'status': 'status',
        'updated': 'updated',
        'application_configs': 'application_configs'
    }

    def __init__(self, created=None, name=None, maintenance_org_id=None, domain_aliases=None, version_tag=None, config_mount_path=None, config_as_mount=None, config_as_env=None, secrets_mount_path=None, secrets_as_mount=None, secrets_as_env=None, application_services=None, serverless_image=None, status=None, updated=None, application_configs=None, local_vars_configuration=None):  # noqa: E501
        """Environment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._name = None
        self._maintenance_org_id = None
        self._domain_aliases = None
        self._version_tag = None
        self._config_mount_path = None
        self._config_as_mount = None
        self._config_as_env = None
        self._secrets_mount_path = None
        self._secrets_as_mount = None
        self._secrets_as_env = None
        self._application_services = None
        self._serverless_image = None
        self._status = None
        self._updated = None
        self._application_configs = None
        self.discriminator = None

        if created is not None:
            self.created = created
        self.name = name
        if maintenance_org_id is not None:
            self.maintenance_org_id = maintenance_org_id
        if domain_aliases is not None:
            self.domain_aliases = domain_aliases
        if version_tag is not None:
            self.version_tag = version_tag
        if config_mount_path is not None:
            self.config_mount_path = config_mount_path
        if config_as_mount is not None:
            self.config_as_mount = config_as_mount
        if config_as_env is not None:
            self.config_as_env = config_as_env
        if secrets_mount_path is not None:
            self.secrets_mount_path = secrets_mount_path
        if secrets_as_mount is not None:
            self.secrets_as_mount = secrets_as_mount
        if secrets_as_env is not None:
            self.secrets_as_env = secrets_as_env
        if application_services is not None:
            self.application_services = application_services
        if serverless_image is not None:
            self.serverless_image = serverless_image
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated
        if application_configs is not None:
            self.application_configs = application_configs

    @property
    def created(self):
        """Gets the created of this Environment.  # noqa: E501

        Creation time  # noqa: E501

        :return: The created of this Environment.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Environment.

        Creation time  # noqa: E501

        :param created: The created of this Environment.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def name(self):
        """Gets the name of this Environment.  # noqa: E501

        Environment name  # noqa: E501

        :return: The name of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Environment.

        Environment name  # noqa: E501

        :param name: The name of this Environment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 40):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def maintenance_org_id(self):
        """Gets the maintenance_org_id of this Environment.  # noqa: E501

        The Organisation which is responsibile for maintaining this Environment. Often this will be the same Organisation as the owning Application. However, sometimes it makes sense to delegate this responsibility to another Organisation. To do so, set this field to that Organisation's identifier. Users with sufficient permissions in that organisation will be able to modify this Environment. If the maintenance_org_id is not provided, it will populated with that of the parent application's organisation.   # noqa: E501

        :return: The maintenance_org_id of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_org_id

    @maintenance_org_id.setter
    def maintenance_org_id(self, maintenance_org_id):
        """Sets the maintenance_org_id of this Environment.

        The Organisation which is responsibile for maintaining this Environment. Often this will be the same Organisation as the owning Application. However, sometimes it makes sense to delegate this responsibility to another Organisation. To do so, set this field to that Organisation's identifier. Users with sufficient permissions in that organisation will be able to modify this Environment. If the maintenance_org_id is not provided, it will populated with that of the parent application's organisation.   # noqa: E501

        :param maintenance_org_id: The maintenance_org_id of this Environment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                maintenance_org_id is not None and len(maintenance_org_id) > 40):
            raise ValueError("Invalid value for `maintenance_org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                maintenance_org_id is not None and len(maintenance_org_id) < 1):
            raise ValueError("Invalid value for `maintenance_org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._maintenance_org_id = maintenance_org_id

    @property
    def domain_aliases(self):
        """Gets the domain_aliases of this Environment.  # noqa: E501

        A list of alternative domains for an instance. This can be used if you want to use a different FQDN for your application instead of the default `appname.org_subdomain`. Multiple different names can be useful if an application is multi-tenant, that is it can be accessed by multiple organisations and you don't want your users to see it any different to existing web applications. A certificate will be generated for all valid domains.  All aliases entered must have a cname assignment pointing to the FQDN of the cluster hosting your application.   # noqa: E501

        :return: The domain_aliases of this Environment.  # noqa: E501
        :rtype: list[str]
        """
        return self._domain_aliases

    @domain_aliases.setter
    def domain_aliases(self, domain_aliases):
        """Sets the domain_aliases of this Environment.

        A list of alternative domains for an instance. This can be used if you want to use a different FQDN for your application instead of the default `appname.org_subdomain`. Multiple different names can be useful if an application is multi-tenant, that is it can be accessed by multiple organisations and you don't want your users to see it any different to existing web applications. A certificate will be generated for all valid domains.  All aliases entered must have a cname assignment pointing to the FQDN of the cluster hosting your application.   # noqa: E501

        :param domain_aliases: The domain_aliases of this Environment.  # noqa: E501
        :type: list[str]
        """

        self._domain_aliases = domain_aliases

    @property
    def version_tag(self):
        """Gets the version_tag of this Environment.  # noqa: E501

        The version of the container to run. Required if the owning application is hosted.   # noqa: E501

        :return: The version_tag of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._version_tag

    @version_tag.setter
    def version_tag(self, version_tag):
        """Sets the version_tag of this Environment.

        The version of the container to run. Required if the owning application is hosted.   # noqa: E501

        :param version_tag: The version_tag of this Environment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version_tag is not None and len(version_tag) > 40):
            raise ValueError("Invalid value for `version_tag`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version_tag is not None and len(version_tag) < 1):
            raise ValueError("Invalid value for `version_tag`, length must be greater than or equal to `1`")  # noqa: E501

        self._version_tag = version_tag

    @property
    def config_mount_path(self):
        """Gets the config_mount_path of this Environment.  # noqa: E501

        config_as_mount file path  # noqa: E501

        :return: The config_mount_path of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._config_mount_path

    @config_mount_path.setter
    def config_mount_path(self, config_mount_path):
        """Sets the config_mount_path of this Environment.

        config_as_mount file path  # noqa: E501

        :param config_mount_path: The config_mount_path of this Environment.  # noqa: E501
        :type: str
        """

        self._config_mount_path = config_mount_path

    @property
    def config_as_mount(self):
        """Gets the config_as_mount of this Environment.  # noqa: E501

        A json object of config applied as file mounted  # noqa: E501

        :return: The config_as_mount of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._config_as_mount

    @config_as_mount.setter
    def config_as_mount(self, config_as_mount):
        """Sets the config_as_mount of this Environment.

        A json object of config applied as file mounted  # noqa: E501

        :param config_as_mount: The config_as_mount of this Environment.  # noqa: E501
        :type: str
        """

        self._config_as_mount = config_as_mount

    @property
    def config_as_env(self):
        """Gets the config_as_env of this Environment.  # noqa: E501

        A json object of config applied as environment  # noqa: E501

        :return: The config_as_env of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._config_as_env

    @config_as_env.setter
    def config_as_env(self, config_as_env):
        """Sets the config_as_env of this Environment.

        A json object of config applied as environment  # noqa: E501

        :param config_as_env: The config_as_env of this Environment.  # noqa: E501
        :type: str
        """

        self._config_as_env = config_as_env

    @property
    def secrets_mount_path(self):
        """Gets the secrets_mount_path of this Environment.  # noqa: E501

        secret_as_mount file path  # noqa: E501

        :return: The secrets_mount_path of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._secrets_mount_path

    @secrets_mount_path.setter
    def secrets_mount_path(self, secrets_mount_path):
        """Sets the secrets_mount_path of this Environment.

        secret_as_mount file path  # noqa: E501

        :param secrets_mount_path: The secrets_mount_path of this Environment.  # noqa: E501
        :type: str
        """

        self._secrets_mount_path = secrets_mount_path

    @property
    def secrets_as_mount(self):
        """Gets the secrets_as_mount of this Environment.  # noqa: E501

        A json object of secrets applied as file mounted  # noqa: E501

        :return: The secrets_as_mount of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._secrets_as_mount

    @secrets_as_mount.setter
    def secrets_as_mount(self, secrets_as_mount):
        """Sets the secrets_as_mount of this Environment.

        A json object of secrets applied as file mounted  # noqa: E501

        :param secrets_as_mount: The secrets_as_mount of this Environment.  # noqa: E501
        :type: str
        """

        self._secrets_as_mount = secrets_as_mount

    @property
    def secrets_as_env(self):
        """Gets the secrets_as_env of this Environment.  # noqa: E501

        A json object of secrets applied as environment  # noqa: E501

        :return: The secrets_as_env of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._secrets_as_env

    @secrets_as_env.setter
    def secrets_as_env(self, secrets_as_env):
        """Sets the secrets_as_env of this Environment.

        A json object of secrets applied as environment  # noqa: E501

        :param secrets_as_env: The secrets_as_env of this Environment.  # noqa: E501
        :type: str
        """

        self._secrets_as_env = secrets_as_env

    @property
    def application_services(self):
        """Gets the application_services of this Environment.  # noqa: E501

        The services used by the application for this environment. Note that in order to add a service to the environment, this environment must be added to the list of assignments for that service in the ApplicationService collection for the organisation.   # noqa: E501

        :return: The application_services of this Environment.  # noqa: E501
        :rtype: list[ApplicationService]
        """
        return self._application_services

    @application_services.setter
    def application_services(self, application_services):
        """Sets the application_services of this Environment.

        The services used by the application for this environment. Note that in order to add a service to the environment, this environment must be added to the list of assignments for that service in the ApplicationService collection for the organisation.   # noqa: E501

        :param application_services: The application_services of this Environment.  # noqa: E501
        :type: list[ApplicationService]
        """

        self._application_services = application_services

    @property
    def serverless_image(self):
        """Gets the serverless_image of this Environment.  # noqa: E501

        serverless image path  # noqa: E501

        :return: The serverless_image of this Environment.  # noqa: E501
        :rtype: str
        """
        return self._serverless_image

    @serverless_image.setter
    def serverless_image(self, serverless_image):
        """Sets the serverless_image of this Environment.

        serverless image path  # noqa: E501

        :param serverless_image: The serverless_image of this Environment.  # noqa: E501
        :type: str
        """

        self._serverless_image = serverless_image

    @property
    def status(self):
        """Gets the status of this Environment.  # noqa: E501


        :return: The status of this Environment.  # noqa: E501
        :rtype: EnvironmentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Environment.


        :param status: The status of this Environment.  # noqa: E501
        :type: EnvironmentStatus
        """

        self._status = status

    @property
    def updated(self):
        """Gets the updated of this Environment.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this Environment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Environment.

        Update time  # noqa: E501

        :param updated: The updated of this Environment.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def application_configs(self):
        """Gets the application_configs of this Environment.  # noqa: E501


        :return: The application_configs of this Environment.  # noqa: E501
        :rtype: ApplicationConfig
        """
        return self._application_configs

    @application_configs.setter
    def application_configs(self, application_configs):
        """Sets the application_configs of this Environment.


        :param application_configs: The application_configs of this Environment.  # noqa: E501
        :type: ApplicationConfig
        """

        self._application_configs = application_configs

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
        if not isinstance(other, Environment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Environment):
            return True

        return self.to_dict() != other.to_dict()
