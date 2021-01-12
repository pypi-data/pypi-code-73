# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['ServiceEndpointAzureRM']


class ServiceEndpointAzureRM(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 azurerm_spn_tenantid: Optional[pulumi.Input[str]] = None,
                 azurerm_subscription_id: Optional[pulumi.Input[str]] = None,
                 azurerm_subscription_name: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['ServiceEndpointAzureRMCredentialsArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 service_endpoint_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages Manual or Automatic AzureRM service endpoint within Azure DevOps.

        ## Requirements (Manual AzureRM Service Endpoint)

        Before to create a service end point in Azure DevOps, you need to create a Service Principal in your Azure subscription.

        For detailed steps to create a service principal with Azure cli see the [documentation](https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest)

        ## Example Usage
        ### Manual AzureRM Service Endpoint

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.Project("project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        endpointazure = azuredevops.ServiceEndpointAzureRM("endpointazure",
            project_id=project.id,
            service_endpoint_name="Sample AzureRM",
            description="Managed by Terraform",
            credentials=azuredevops.ServiceEndpointAzureRMCredentialsArgs(
                serviceprincipalid="00000000-0000-0000-0000-000000000000",
                serviceprincipalkey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            ),
            azurerm_spn_tenantid="00000000-0000-0000-0000-000000000000",
            azurerm_subscription_id="00000000-0000-0000-0000-000000000000",
            azurerm_subscription_name="Sample Subscription")
        ```
        ### Automatic AzureRM Service Endpoint

        ```python
        import pulumi
        import pulumi_azuredevops as azuredevops

        project = azuredevops.Project("project",
            visibility="private",
            version_control="Git",
            work_item_template="Agile")
        endpointazure = azuredevops.ServiceEndpointAzureRM("endpointazure",
            project_id=project.id,
            service_endpoint_name="Sample AzureRM",
            description="Managed by Terraform",
            azurerm_spn_tenantid="00000000-0000-0000-0000-000000000000",
            azurerm_subscription_id="00000000-0000-0000-0000-000000000000",
            azurerm_subscription_name="Microsoft Azure DEMO")
        ```
        ## Relevant Links

        - [Azure DevOps Service REST API 5.1 - Service End points](https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1)

        ## Import

        Azure DevOps Service Endpoint Azure Resource Manage can be imported using **projectID/serviceEndpointID** or **projectName/serviceEndpointID**

        ```sh
         $ pulumi import azuredevops:index/serviceEndpointAzureRM:ServiceEndpointAzureRM serviceendpoint 00000000-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azurerm_spn_tenantid: The tenant id if the service principal.
        :param pulumi.Input[str] azurerm_subscription_id: The subscription Id of the Azure targets.
        :param pulumi.Input[str] azurerm_subscription_name: The subscription Name of the targets.
        :param pulumi.Input[pulumi.InputType['ServiceEndpointAzureRMCredentialsArgs']] credentials: A `credentials` block.
        :param pulumi.Input[str] description: Service connection description.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] resource_group: The resource group used for scope of automatic service endpoint.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['authorization'] = authorization
            if azurerm_spn_tenantid is None and not opts.urn:
                raise TypeError("Missing required property 'azurerm_spn_tenantid'")
            __props__['azurerm_spn_tenantid'] = azurerm_spn_tenantid
            if azurerm_subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'azurerm_subscription_id'")
            __props__['azurerm_subscription_id'] = azurerm_subscription_id
            if azurerm_subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'azurerm_subscription_name'")
            __props__['azurerm_subscription_name'] = azurerm_subscription_name
            __props__['credentials'] = credentials
            __props__['description'] = description
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['resource_group'] = resource_group
            if service_endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_endpoint_name'")
            __props__['service_endpoint_name'] = service_endpoint_name
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azuredevops:ServiceEndpoint/azureRM:AzureRM")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServiceEndpointAzureRM, __self__).__init__(
            'azuredevops:index/serviceEndpointAzureRM:ServiceEndpointAzureRM',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authorization: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            azurerm_spn_tenantid: Optional[pulumi.Input[str]] = None,
            azurerm_subscription_id: Optional[pulumi.Input[str]] = None,
            azurerm_subscription_name: Optional[pulumi.Input[str]] = None,
            credentials: Optional[pulumi.Input[pulumi.InputType['ServiceEndpointAzureRMCredentialsArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            resource_group: Optional[pulumi.Input[str]] = None,
            service_endpoint_name: Optional[pulumi.Input[str]] = None) -> 'ServiceEndpointAzureRM':
        """
        Get an existing ServiceEndpointAzureRM resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azurerm_spn_tenantid: The tenant id if the service principal.
        :param pulumi.Input[str] azurerm_subscription_id: The subscription Id of the Azure targets.
        :param pulumi.Input[str] azurerm_subscription_name: The subscription Name of the targets.
        :param pulumi.Input[pulumi.InputType['ServiceEndpointAzureRMCredentialsArgs']] credentials: A `credentials` block.
        :param pulumi.Input[str] description: Service connection description.
        :param pulumi.Input[str] project_id: The project ID or project name.
        :param pulumi.Input[str] resource_group: The resource group used for scope of automatic service endpoint.
        :param pulumi.Input[str] service_endpoint_name: The Service Endpoint name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["authorization"] = authorization
        __props__["azurerm_spn_tenantid"] = azurerm_spn_tenantid
        __props__["azurerm_subscription_id"] = azurerm_subscription_id
        __props__["azurerm_subscription_name"] = azurerm_subscription_name
        __props__["credentials"] = credentials
        __props__["description"] = description
        __props__["project_id"] = project_id
        __props__["resource_group"] = resource_group
        __props__["service_endpoint_name"] = service_endpoint_name
        return ServiceEndpointAzureRM(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authorization(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="azurermSpnTenantid")
    def azurerm_spn_tenantid(self) -> pulumi.Output[str]:
        """
        The tenant id if the service principal.
        """
        return pulumi.get(self, "azurerm_spn_tenantid")

    @property
    @pulumi.getter(name="azurermSubscriptionId")
    def azurerm_subscription_id(self) -> pulumi.Output[str]:
        """
        The subscription Id of the Azure targets.
        """
        return pulumi.get(self, "azurerm_subscription_id")

    @property
    @pulumi.getter(name="azurermSubscriptionName")
    def azurerm_subscription_name(self) -> pulumi.Output[str]:
        """
        The subscription Name of the targets.
        """
        return pulumi.get(self, "azurerm_subscription_name")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.ServiceEndpointAzureRMCredentials']]:
        """
        A `credentials` block.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Service connection description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The project ID or project name.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[Optional[str]]:
        """
        The resource group used for scope of automatic service endpoint.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="serviceEndpointName")
    def service_endpoint_name(self) -> pulumi.Output[str]:
        """
        The Service Endpoint name.
        """
        return pulumi.get(self, "service_endpoint_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

