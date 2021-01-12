# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['DatasetHttp']


class DatasetHttp(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 data_factory_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 linked_service_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 relative_url: Optional[pulumi.Input[str]] = None,
                 request_body: Optional[pulumi.Input[str]] = None,
                 request_method: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetHttpSchemaColumnArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an Azure HTTP Dataset inside an Azure Data Factory.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="northeurope")
        example_factory = azure.datafactory.Factory("exampleFactory",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name)
        example_linked_service_web = azure.datafactory.LinkedServiceWeb("exampleLinkedServiceWeb",
            resource_group_name=example_resource_group.name,
            data_factory_name=example_factory.name,
            authentication_type="Anonymous",
            url="https://www.bing.com")
        example_dataset_http = azure.datafactory.DatasetHttp("exampleDatasetHttp",
            resource_group_name=example_resource_group.name,
            data_factory_name=example_factory.name,
            linked_service_name=example_linked_service_web.name,
            relative_url="http://www.bing.com",
            request_body="foo=bar",
            request_method="POST")
        ```

        ## Import

        Data Factory Datasets can be imported using the `resource id`, e.g.

        ```sh
         $ pulumi import azure:datafactory/datasetHttp:DatasetHttp example /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/example/providers/Microsoft.DataFactory/factories/example/datasets/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: A map of additional properties to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] annotations: List of tags that can be used for describing the Data Factory Dataset.
        :param pulumi.Input[str] data_factory_name: The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.
        :param pulumi.Input[str] description: The description for the Data Factory Dataset.
        :param pulumi.Input[str] folder: The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        :param pulumi.Input[str] linked_service_name: The Data Factory Linked Service name in which to associate the Dataset with.
        :param pulumi.Input[str] name: Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters to associate with the Data Factory Dataset.
        :param pulumi.Input[str] relative_url: The relative URL based on the URL in the HTTP Linked Service.
        :param pulumi.Input[str] request_body: The body for the HTTP request.
        :param pulumi.Input[str] request_method: The HTTP method for the HTTP request. (e.g. GET, POST)
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Data Factory Dataset. Changing this forces a new resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetHttpSchemaColumnArgs']]]] schema_columns: A `schema_column` block as defined below.
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

            __props__['additional_properties'] = additional_properties
            __props__['annotations'] = annotations
            if data_factory_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_factory_name'")
            __props__['data_factory_name'] = data_factory_name
            __props__['description'] = description
            __props__['folder'] = folder
            if linked_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'linked_service_name'")
            __props__['linked_service_name'] = linked_service_name
            __props__['name'] = name
            __props__['parameters'] = parameters
            __props__['relative_url'] = relative_url
            __props__['request_body'] = request_body
            __props__['request_method'] = request_method
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            __props__['schema_columns'] = schema_columns
        super(DatasetHttp, __self__).__init__(
            'azure:datafactory/datasetHttp:DatasetHttp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            additional_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            annotations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            data_factory_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            linked_service_name: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            relative_url: Optional[pulumi.Input[str]] = None,
            request_body: Optional[pulumi.Input[str]] = None,
            request_method: Optional[pulumi.Input[str]] = None,
            resource_group_name: Optional[pulumi.Input[str]] = None,
            schema_columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetHttpSchemaColumnArgs']]]]] = None) -> 'DatasetHttp':
        """
        Get an existing DatasetHttp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_properties: A map of additional properties to associate with the Data Factory Dataset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] annotations: List of tags that can be used for describing the Data Factory Dataset.
        :param pulumi.Input[str] data_factory_name: The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.
        :param pulumi.Input[str] description: The description for the Data Factory Dataset.
        :param pulumi.Input[str] folder: The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        :param pulumi.Input[str] linked_service_name: The Data Factory Linked Service name in which to associate the Dataset with.
        :param pulumi.Input[str] name: Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of parameters to associate with the Data Factory Dataset.
        :param pulumi.Input[str] relative_url: The relative URL based on the URL in the HTTP Linked Service.
        :param pulumi.Input[str] request_body: The body for the HTTP request.
        :param pulumi.Input[str] request_method: The HTTP method for the HTTP request. (e.g. GET, POST)
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Data Factory Dataset. Changing this forces a new resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DatasetHttpSchemaColumnArgs']]]] schema_columns: A `schema_column` block as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["additional_properties"] = additional_properties
        __props__["annotations"] = annotations
        __props__["data_factory_name"] = data_factory_name
        __props__["description"] = description
        __props__["folder"] = folder
        __props__["linked_service_name"] = linked_service_name
        __props__["name"] = name
        __props__["parameters"] = parameters
        __props__["relative_url"] = relative_url
        __props__["request_body"] = request_body
        __props__["request_method"] = request_method
        __props__["resource_group_name"] = resource_group_name
        __props__["schema_columns"] = schema_columns
        return DatasetHttp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of additional properties to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "additional_properties")

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of tags that can be used for describing the Data Factory Dataset.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="dataFactoryName")
    def data_factory_name(self) -> pulumi.Output[str]:
        """
        The Data Factory name in which to associate the Dataset with. Changing this forces a new resource.
        """
        return pulumi.get(self, "data_factory_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for the Data Factory Dataset.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[str]]:
        """
        The folder that this Dataset is in. If not specified, the Dataset will appear at the root level.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter(name="linkedServiceName")
    def linked_service_name(self) -> pulumi.Output[str]:
        """
        The Data Factory Linked Service name in which to associate the Dataset with.
        """
        return pulumi.get(self, "linked_service_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the Data Factory Dataset. Changing this forces a new resource to be created. Must be globally unique. See the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/data-factory/naming-rules) for all restrictions.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of parameters to associate with the Data Factory Dataset.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="relativeUrl")
    def relative_url(self) -> pulumi.Output[Optional[str]]:
        """
        The relative URL based on the URL in the HTTP Linked Service.
        """
        return pulumi.get(self, "relative_url")

    @property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> pulumi.Output[Optional[str]]:
        """
        The body for the HTTP request.
        """
        return pulumi.get(self, "request_body")

    @property
    @pulumi.getter(name="requestMethod")
    def request_method(self) -> pulumi.Output[Optional[str]]:
        """
        The HTTP method for the HTTP request. (e.g. GET, POST)
        """
        return pulumi.get(self, "request_method")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the resource group in which to create the Data Factory Dataset. Changing this forces a new resource
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="schemaColumns")
    def schema_columns(self) -> pulumi.Output[Optional[Sequence['outputs.DatasetHttpSchemaColumn']]]:
        """
        A `schema_column` block as defined below.
        """
        return pulumi.get(self, "schema_columns")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

