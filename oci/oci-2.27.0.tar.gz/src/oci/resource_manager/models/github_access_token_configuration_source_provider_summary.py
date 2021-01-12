# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .configuration_source_provider_summary import ConfigurationSourceProviderSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GithubAccessTokenConfigurationSourceProviderSummary(ConfigurationSourceProviderSummary):
    """
    Summary information for a configuration source provider of the type `GITHUB_ACCESS_TOKEN`.
    This type corresponds to a configuration source provider in GitHub that is authenticated with a personal access token.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GithubAccessTokenConfigurationSourceProviderSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.GithubAccessTokenConfigurationSourceProviderSummary.config_source_provider_type` attribute
        of this class is ``GITHUB_ACCESS_TOKEN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type lifecycle_state: str

        :param config_source_provider_type:
            The value to assign to the config_source_provider_type property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type config_source_provider_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param api_endpoint:
            The value to assign to the api_endpoint property of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type api_endpoint: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'config_source_provider_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'api_endpoint': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'config_source_provider_type': 'configSourceProviderType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'api_endpoint': 'apiEndpoint'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._config_source_provider_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._api_endpoint = None
        self._config_source_provider_type = 'GITHUB_ACCESS_TOKEN'

    @property
    def api_endpoint(self):
        """
        Gets the api_endpoint of this GithubAccessTokenConfigurationSourceProviderSummary.
        The GitHub service endpoint.
        Example: `https://github.com/`


        :return: The api_endpoint of this GithubAccessTokenConfigurationSourceProviderSummary.
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        """
        Sets the api_endpoint of this GithubAccessTokenConfigurationSourceProviderSummary.
        The GitHub service endpoint.
        Example: `https://github.com/`


        :param api_endpoint: The api_endpoint of this GithubAccessTokenConfigurationSourceProviderSummary.
        :type: str
        """
        self._api_endpoint = api_endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
