import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

import constructs
from .. import (
    CfnResource as _CfnResource_e0a482dc,
    CfnTag as _CfnTag_95fbdc29,
    Construct as _Construct_e78e779f,
    Expiration as _Expiration_505df041,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    IResource as _IResource_8c1dbbbd,
    Resource as _Resource_abff4495,
    ResourceProps as _ResourceProps_9b554c0f,
    TagManager as _TagManager_0b7ab120,
    TreeInspector as _TreeInspector_1cd1894e,
)
from ..aws_cognito import IUserPool as _IUserPool_5e500460
from ..aws_dynamodb import ITable as _ITable_24826f7e
from ..aws_iam import (
    Grant as _Grant_bcb5eae7,
    IGrantable as _IGrantable_4c5a91d1,
    IPrincipal as _IPrincipal_93b48231,
    IRole as _IRole_59af6f50,
)
from ..aws_lambda import IFunction as _IFunction_6e14f09e
from ..aws_rds import IDatabaseCluster as _IDatabaseCluster_2d93b7f0
from ..aws_secretsmanager import ISecret as _ISecret_22fb8757


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.AddFieldOptions",
    jsii_struct_bases=[],
    name_mapping={"field": "field", "field_name": "fieldName"},
)
class AddFieldOptions:
    def __init__(
        self,
        *,
        field: typing.Optional["IField"] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) The options to add a field to an Intermediate Type.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if field is not None:
            self._values["field"] = field
        if field_name is not None:
            self._values["field_name"] = field_name

    @builtins.property
    def field(self) -> typing.Optional["IField"]:
        """(experimental) The resolvable field to add.

        This option must be configured for Object, Interface,
        Input and Union Types.

        :default: - no IField

        :stability: experimental
        """
        result = self._values.get("field")
        return result

    @builtins.property
    def field_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the field.

        This option must be configured for Object, Interface,
        Input and Enum Types.

        :default: - no fieldName

        :stability: experimental
        """
        result = self._values.get("field_name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddFieldOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.ApiKeyConfig",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "expires": "expires", "name": "name"},
)
class ApiKeyConfig:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[_Expiration_505df041] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Configuration for API Key authorization in AppSync.

        :param description: (experimental) Description of API key. Default: - 'Default API Key created by CDK'
        :param expires: (experimental) The time from creation time after which the API key expires. It must be a minimum of 1 day and a maximum of 365 days from date of creation. Rounded down to the nearest hour. Default: - 7 days rounded down to nearest hour
        :param name: (experimental) Unique name of the API Key. Default: - 'DefaultAPIKey'

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) Description of API key.

        :default: - 'Default API Key created by CDK'

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def expires(self) -> typing.Optional[_Expiration_505df041]:
        """(experimental) The time from creation time after which the API key expires.

        It must be a minimum of 1 day and a maximum of 365 days from date of creation.
        Rounded down to the nearest hour.

        :default: - 7 days rounded down to nearest hour

        :stability: experimental
        """
        result = self._values.get("expires")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) Unique name of the API Key.

        :default: - 'DefaultAPIKey'

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.AppsyncFunctionAttributes",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class AppsyncFunctionAttributes:
    def __init__(self, *, function_arn: builtins.str) -> None:
        """(experimental) The attributes for imported AppSync Functions.

        :param function_arn: (experimental) the ARN of the AppSync function.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        """(experimental) the ARN of the AppSync function.

        :stability: experimental
        """
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Assign(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.Assign"):
    """(experimental) Utility class representing the assigment of a value to an attribute.

    :stability: experimental
    """

    def __init__(self, attr: builtins.str, arg: builtins.str) -> None:
        """
        :param attr: -
        :param arg: -

        :stability: experimental
        """
        jsii.create(Assign, self, [attr, arg])

    @jsii.member(jsii_name="putInMap")
    def put_in_map(self, map: builtins.str) -> builtins.str:
        """(experimental) Renders the assignment as a map element.

        :param map: -

        :stability: experimental
        """
        return jsii.invoke(self, "putInMap", [map])

    @jsii.member(jsii_name="renderAsAssignment")
    def render_as_assignment(self) -> builtins.str:
        """(experimental) Renders the assignment as a VTL string.

        :stability: experimental
        """
        return jsii.invoke(self, "renderAsAssignment", [])


class AttributeValues(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.AttributeValues",
):
    """(experimental) Specifies the attribute value assignments.

    :stability: experimental
    """

    def __init__(
        self,
        container: builtins.str,
        assignments: typing.Optional[typing.List[Assign]] = None,
    ) -> None:
        """
        :param container: -
        :param assignments: -

        :stability: experimental
        """
        jsii.create(AttributeValues, self, [container, assignments])

    @jsii.member(jsii_name="attribute")
    def attribute(self, attr: builtins.str) -> "AttributeValuesStep":
        """(experimental) Allows assigning a value to the specified attribute.

        :param attr: -

        :stability: experimental
        """
        return jsii.invoke(self, "attribute", [attr])

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        """(experimental) Renders the attribute value assingments to a VTL string.

        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])

    @jsii.member(jsii_name="renderVariables")
    def render_variables(self) -> builtins.str:
        """(experimental) Renders the variables required for ``renderTemplate``.

        :stability: experimental
        """
        return jsii.invoke(self, "renderVariables", [])


class AttributeValuesStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.AttributeValuesStep",
):
    """(experimental) Utility class to allow assigning a value to an attribute.

    :stability: experimental
    """

    def __init__(
        self,
        attr: builtins.str,
        container: builtins.str,
        assignments: typing.List[Assign],
    ) -> None:
        """
        :param attr: -
        :param container: -
        :param assignments: -

        :stability: experimental
        """
        jsii.create(AttributeValuesStep, self, [attr, container, assignments])

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> AttributeValues:
        """(experimental) Assign the value to the current attribute.

        :param val: -

        :stability: experimental
        """
        return jsii.invoke(self, "is", [val])


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.AuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_authorization_modes": "additionalAuthorizationModes",
        "default_authorization": "defaultAuthorization",
    },
)
class AuthorizationConfig:
    def __init__(
        self,
        *,
        additional_authorization_modes: typing.Optional[typing.List["AuthorizationMode"]] = None,
        default_authorization: typing.Optional["AuthorizationMode"] = None,
    ) -> None:
        """(experimental) Configuration of the API authorization modes.

        :param additional_authorization_modes: (experimental) Additional authorization modes. Default: - No other modes
        :param default_authorization: (experimental) Optional authorization configuration. Default: - API Key authorization

        :stability: experimental
        """
        if isinstance(default_authorization, dict):
            default_authorization = AuthorizationMode(**default_authorization)
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_authorization_modes is not None:
            self._values["additional_authorization_modes"] = additional_authorization_modes
        if default_authorization is not None:
            self._values["default_authorization"] = default_authorization

    @builtins.property
    def additional_authorization_modes(
        self,
    ) -> typing.Optional[typing.List["AuthorizationMode"]]:
        """(experimental) Additional authorization modes.

        :default: - No other modes

        :stability: experimental
        """
        result = self._values.get("additional_authorization_modes")
        return result

    @builtins.property
    def default_authorization(self) -> typing.Optional["AuthorizationMode"]:
        """(experimental) Optional authorization configuration.

        :default: - API Key authorization

        :stability: experimental
        """
        result = self._values.get("default_authorization")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.AuthorizationMode",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "api_key_config": "apiKeyConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "user_pool_config": "userPoolConfig",
    },
)
class AuthorizationMode:
    def __init__(
        self,
        *,
        authorization_type: "AuthorizationType",
        api_key_config: typing.Optional[ApiKeyConfig] = None,
        open_id_connect_config: typing.Optional["OpenIdConnectConfig"] = None,
        user_pool_config: typing.Optional["UserPoolConfig"] = None,
    ) -> None:
        """(experimental) Interface to specify default or additional authorization(s).

        :param authorization_type: (experimental) One of possible four values AppSync supports. Default: - ``AuthorizationType.API_KEY``
        :param api_key_config: (experimental) If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured. Default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'
        :param open_id_connect_config: (experimental) If authorizationType is ``AuthorizationType.OIDC``, this option is required. Default: - none
        :param user_pool_config: (experimental) If authorizationType is ``AuthorizationType.USER_POOL``, this option is required. Default: - none

        :stability: experimental
        """
        if isinstance(api_key_config, dict):
            api_key_config = ApiKeyConfig(**api_key_config)
        if isinstance(open_id_connect_config, dict):
            open_id_connect_config = OpenIdConnectConfig(**open_id_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = UserPoolConfig(**user_pool_config)
        self._values: typing.Dict[str, typing.Any] = {
            "authorization_type": authorization_type,
        }
        if api_key_config is not None:
            self._values["api_key_config"] = api_key_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config

    @builtins.property
    def authorization_type(self) -> "AuthorizationType":
        """(experimental) One of possible four values AppSync supports.

        :default: - ``AuthorizationType.API_KEY``

        :see: https://docs.aws.amazon.com/appsync/latest/devguide/security.html
        :stability: experimental
        """
        result = self._values.get("authorization_type")
        assert result is not None, "Required property 'authorization_type' is missing"
        return result

    @builtins.property
    def api_key_config(self) -> typing.Optional[ApiKeyConfig]:
        """(experimental) If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured.

        :default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'

        :stability: experimental
        """
        result = self._values.get("api_key_config")
        return result

    @builtins.property
    def open_id_connect_config(self) -> typing.Optional["OpenIdConnectConfig"]:
        """(experimental) If authorizationType is ``AuthorizationType.OIDC``, this option is required.

        :default: - none

        :stability: experimental
        """
        result = self._values.get("open_id_connect_config")
        return result

    @builtins.property
    def user_pool_config(self) -> typing.Optional["UserPoolConfig"]:
        """(experimental) If authorizationType is ``AuthorizationType.USER_POOL``, this option is required.

        :default: - none

        :stability: experimental
        """
        result = self._values.get("user_pool_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationMode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_appsync.AuthorizationType")
class AuthorizationType(enum.Enum):
    """(experimental) enum with all possible values for AppSync authorization type.

    :stability: experimental
    """

    API_KEY = "API_KEY"
    """(experimental) API Key authorization type.

    :stability: experimental
    """
    IAM = "IAM"
    """(experimental) AWS IAM authorization type.

    Can be used with Cognito Identity Pool federated credentials

    :stability: experimental
    """
    USER_POOL = "USER_POOL"
    """(experimental) Cognito User Pool authorization type.

    :stability: experimental
    """
    OIDC = "OIDC"
    """(experimental) OpenID Connect authorization type.

    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.AwsIamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "signing_region": "signingRegion",
        "signing_service_name": "signingServiceName",
    },
)
class AwsIamConfig:
    def __init__(
        self,
        *,
        signing_region: builtins.str,
        signing_service_name: builtins.str,
    ) -> None:
        """(experimental) The authorization config in case the HTTP endpoint requires authorization.

        :param signing_region: (experimental) The signing region for AWS IAM authorization.
        :param signing_service_name: (experimental) The signing service name for AWS IAM authorization.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "signing_region": signing_region,
            "signing_service_name": signing_service_name,
        }

    @builtins.property
    def signing_region(self) -> builtins.str:
        """(experimental) The signing region for AWS IAM authorization.

        :stability: experimental
        """
        result = self._values.get("signing_region")
        assert result is not None, "Required property 'signing_region' is missing"
        return result

    @builtins.property
    def signing_service_name(self) -> builtins.str:
        """(experimental) The signing service name for AWS IAM authorization.

        :stability: experimental
        """
        result = self._values.get("signing_service_name")
        assert result is not None, "Required property 'signing_service_name' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsIamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.BaseAppsyncFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
    },
)
class BaseAppsyncFunctionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> None:
        """(experimental) the base properties for AppSync Functions.

        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def name(self) -> builtins.str:
        """(experimental) the name of the AppSync Function.

        :stability: experimental
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description for this AppSync Function.

        :default: - no description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """(experimental) the request mapping template for the AppSync Function.

        :default: - no request mapping template

        :stability: experimental
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """(experimental) the response mapping template for the AppSync Function.

        :default: - no response mapping template

        :stability: experimental
        """
        result = self._values.get("response_mapping_template")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseAppsyncFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BaseDataSource(
    _Construct_e78e779f,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_appsync.BaseDataSource",
):
    """(experimental) Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for concrete datasources

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _BaseDataSourceProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        props: "BackedDataSourceProps",
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_a771d0ef]] = None,
        elasticsearch_config: typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_a771d0ef]] = None,
        http_config: typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_a771d0ef]] = None,
        lambda_config: typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_a771d0ef]] = None,
        relational_database_config: typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param type: (experimental) the type of the AppSync datasource.
        :param dynamo_db_config: (experimental) configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (experimental) configuration for Elasticsearch Datasource. Default: - No config
        :param http_config: (experimental) configuration for HTTP Datasource. Default: - No config
        :param lambda_config: (experimental) configuration for Lambda Datasource. Default: - No config
        :param relational_database_config: (experimental) configuration for RDS Datasource. Default: - No config

        :stability: experimental
        """
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(BaseDataSource, self, [scope, id, props, extended])

    @jsii.member(jsii_name="createFunction")
    def create_function(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "AppsyncFunction":
        """(experimental) creates a new appsync function for this datasource and API using the given properties.

        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template

        :stability: experimental
        """
        props = BaseAppsyncFunctionProps(
            name=name,
            description=description,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return jsii.invoke(self, "createFunction", [props])

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        """(experimental) creates a new resolver for this datasource and API using the given properties.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        """
        props = BaseResolverProps(
            field_name=field_name,
            type_name=type_name,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return jsii.invoke(self, "createResolver", [props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="ds")
    def ds(self) -> "CfnDataSource":
        """(experimental) the underlying CFN data source resource.

        :stability: experimental
        """
        return jsii.get(self, "ds")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of the data source.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="api")
    def _api(self) -> "IGraphqlApi":
        """
        :stability: experimental
        """
        return jsii.get(self, "api")

    @_api.setter # type: ignore
    def _api(self, value: "IGraphqlApi") -> None:
        jsii.set(self, "api", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serviceRole")
    def _service_role(self) -> typing.Optional[_IRole_59af6f50]:
        """
        :stability: experimental
        """
        return jsii.get(self, "serviceRole")

    @_service_role.setter # type: ignore
    def _service_role(self, value: typing.Optional[_IRole_59af6f50]) -> None:
        jsii.set(self, "serviceRole", value)


class _BaseDataSourceProxy(BaseDataSource):
    pass


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.BaseDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={"api": "api", "description": "description", "name": "name"},
)
class BaseDataSourceProps:
    def __init__(
        self,
        *,
        api: "IGraphqlApi",
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Base properties for an AppSync datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def api(self) -> "IGraphqlApi":
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.BaseResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
    },
)
class BaseResolverProps:
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> None:
        """(experimental) Basic properties for an AppSync resolver.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def field_name(self) -> builtins.str:
        """(experimental) name of the GraphQL field in the given type this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return result

    @builtins.property
    def type_name(self) -> builtins.str:
        """(experimental) name of the GraphQL type this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return result

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List["IAppsyncFunction"]]:
        """(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit

        :stability: experimental
        """
        result = self._values.get("pipeline_config")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("response_mapping_template")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.BaseTypeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "is_list": "isList",
        "is_required": "isRequired",
        "is_required_list": "isRequiredList",
    },
)
class BaseTypeOptions:
    def __init__(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> None:
        """(experimental) Base options for GraphQL Types.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        :option: isRequiredList - is this attribute a non-nullable list
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if is_list is not None:
            self._values["is_list"] = is_list
        if is_required is not None:
            self._values["is_required"] = is_required
        if is_required_list is not None:
            self._values["is_required_list"] = is_required_list

    @builtins.property
    def is_list(self) -> typing.Optional[builtins.bool]:
        """(experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type].

        :default: - false

        :stability: experimental
        """
        result = self._values.get("is_list")
        return result

    @builtins.property
    def is_required(self) -> typing.Optional[builtins.bool]:
        """(experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type!

        :default: - false

        :stability: experimental
        """
        result = self._values.get("is_required")
        return result

    @builtins.property
    def is_required_list(self) -> typing.Optional[builtins.bool]:
        """(experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]!

        :default: - false

        :stability: experimental
        """
        result = self._values.get("is_required_list")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnApiCache(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnApiCache",
):
    """A CloudFormation ``AWS::AppSync::ApiCache``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
    :cloudformationResource: AWS::AppSync::ApiCache
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::ApiCache``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_caching_behavior: ``AWS::AppSync::ApiCache.ApiCachingBehavior``.
        :param api_id: ``AWS::AppSync::ApiCache.ApiId``.
        :param ttl: ``AWS::AppSync::ApiCache.Ttl``.
        :param type: ``AWS::AppSync::ApiCache.Type``.
        :param at_rest_encryption_enabled: ``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.
        :param transit_encryption_enabled: ``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.
        """
        props = CfnApiCacheProps(
            api_caching_behavior=api_caching_behavior,
            api_id=api_id,
            ttl=ttl,
            type=type,
            at_rest_encryption_enabled=at_rest_encryption_enabled,
            transit_encryption_enabled=transit_encryption_enabled,
        )

        jsii.create(CfnApiCache, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiCachingBehavior")
    def api_caching_behavior(self) -> builtins.str:
        """``AWS::AppSync::ApiCache.ApiCachingBehavior``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        """
        return jsii.get(self, "apiCachingBehavior")

    @api_caching_behavior.setter # type: ignore
    def api_caching_behavior(self, value: builtins.str) -> None:
        jsii.set(self, "apiCachingBehavior", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::ApiCache.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter # type: ignore
    def api_id(self, value: builtins.str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        """``AWS::AppSync::ApiCache.Ttl``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        """
        return jsii.get(self, "ttl")

    @ttl.setter # type: ignore
    def ttl(self, value: jsii.Number) -> None:
        jsii.set(self, "ttl", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        """``AWS::AppSync::ApiCache.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        """
        return jsii.get(self, "type")

    @type.setter # type: ignore
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        """
        return jsii.get(self, "atRestEncryptionEnabled")

    @at_rest_encryption_enabled.setter # type: ignore
    def at_rest_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "atRestEncryptionEnabled", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="transitEncryptionEnabled")
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        """
        return jsii.get(self, "transitEncryptionEnabled")

    @transit_encryption_enabled.setter # type: ignore
    def transit_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "transitEncryptionEnabled", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnApiCacheProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_caching_behavior": "apiCachingBehavior",
        "api_id": "apiId",
        "ttl": "ttl",
        "type": "type",
        "at_rest_encryption_enabled": "atRestEncryptionEnabled",
        "transit_encryption_enabled": "transitEncryptionEnabled",
    },
)
class CfnApiCacheProps:
    def __init__(
        self,
        *,
        api_caching_behavior: builtins.str,
        api_id: builtins.str,
        ttl: jsii.Number,
        type: builtins.str,
        at_rest_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        transit_encryption_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::ApiCache``.

        :param api_caching_behavior: ``AWS::AppSync::ApiCache.ApiCachingBehavior``.
        :param api_id: ``AWS::AppSync::ApiCache.ApiId``.
        :param ttl: ``AWS::AppSync::ApiCache.Ttl``.
        :param type: ``AWS::AppSync::ApiCache.Type``.
        :param at_rest_encryption_enabled: ``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.
        :param transit_encryption_enabled: ``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api_caching_behavior": api_caching_behavior,
            "api_id": api_id,
            "ttl": ttl,
            "type": type,
        }
        if at_rest_encryption_enabled is not None:
            self._values["at_rest_encryption_enabled"] = at_rest_encryption_enabled
        if transit_encryption_enabled is not None:
            self._values["transit_encryption_enabled"] = transit_encryption_enabled

    @builtins.property
    def api_caching_behavior(self) -> builtins.str:
        """``AWS::AppSync::ApiCache.ApiCachingBehavior``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apicachingbehavior
        """
        result = self._values.get("api_caching_behavior")
        assert result is not None, "Required property 'api_caching_behavior' is missing"
        return result

    @builtins.property
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::ApiCache.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-apiid
        """
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return result

    @builtins.property
    def ttl(self) -> jsii.Number:
        """``AWS::AppSync::ApiCache.Ttl``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-ttl
        """
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return result

    @builtins.property
    def type(self) -> builtins.str:
        """``AWS::AppSync::ApiCache.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-type
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    @builtins.property
    def at_rest_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::ApiCache.AtRestEncryptionEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-atrestencryptionenabled
        """
        result = self._values.get("at_rest_encryption_enabled")
        return result

    @builtins.property
    def transit_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::ApiCache.TransitEncryptionEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html#cfn-appsync-apicache-transitencryptionenabled
        """
        result = self._values.get("transit_encryption_enabled")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiCacheProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnApiKey(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnApiKey",
):
    """A CloudFormation ``AWS::AppSync::ApiKey``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
    :cloudformationResource: AWS::AppSync::ApiKey
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        api_id: builtins.str,
        api_key_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::ApiKey``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::ApiKey.ApiId``.
        :param api_key_id: ``AWS::AppSync::ApiKey.ApiKeyId``.
        :param description: ``AWS::AppSync::ApiKey.Description``.
        :param expires: ``AWS::AppSync::ApiKey.Expires``.
        """
        props = CfnApiKeyProps(
            api_id=api_id,
            api_key_id=api_key_id,
            description=description,
            expires=expires,
        )

        jsii.create(CfnApiKey, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrApiKey")
    def attr_api_key(self) -> builtins.str:
        """
        :cloudformationAttribute: ApiKey
        """
        return jsii.get(self, "attrApiKey")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::ApiKey.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter # type: ignore
    def api_id(self, value: builtins.str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiKeyId")
    def api_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::ApiKey.ApiKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid
        """
        return jsii.get(self, "apiKeyId")

    @api_key_id.setter # type: ignore
    def api_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "apiKeyId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::ApiKey.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="expires")
    def expires(self) -> typing.Optional[jsii.Number]:
        """``AWS::AppSync::ApiKey.Expires``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        """
        return jsii.get(self, "expires")

    @expires.setter # type: ignore
    def expires(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "expires", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnApiKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "api_key_id": "apiKeyId",
        "description": "description",
        "expires": "expires",
    },
)
class CfnApiKeyProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        api_key_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[jsii.Number] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::ApiKey``.

        :param api_id: ``AWS::AppSync::ApiKey.ApiId``.
        :param api_key_id: ``AWS::AppSync::ApiKey.ApiKeyId``.
        :param description: ``AWS::AppSync::ApiKey.Description``.
        :param expires: ``AWS::AppSync::ApiKey.Expires``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
        }
        if api_key_id is not None:
            self._values["api_key_id"] = api_key_id
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires

    @builtins.property
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::ApiKey.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apiid
        """
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return result

    @builtins.property
    def api_key_id(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::ApiKey.ApiKeyId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-apikeyid
        """
        result = self._values.get("api_key_id")
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::ApiKey.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def expires(self) -> typing.Optional[jsii.Number]:
        """``AWS::AppSync::ApiKey.Expires``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html#cfn-appsync-apikey-expires
        """
        result = self._values.get("expires")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnDataSource(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnDataSource",
):
    """A CloudFormation ``AWS::AppSync::DataSource``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
    :cloudformationResource: AWS::AppSync::DataSource
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamo_db_config: typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_a771d0ef]] = None,
        elasticsearch_config: typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_a771d0ef]] = None,
        http_config: typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_a771d0ef]] = None,
        lambda_config: typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_a771d0ef]] = None,
        relational_database_config: typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_a771d0ef]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::DataSource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::DataSource.ApiId``.
        :param name: ``AWS::AppSync::DataSource.Name``.
        :param type: ``AWS::AppSync::DataSource.Type``.
        :param description: ``AWS::AppSync::DataSource.Description``.
        :param dynamo_db_config: ``AWS::AppSync::DataSource.DynamoDBConfig``.
        :param elasticsearch_config: ``AWS::AppSync::DataSource.ElasticsearchConfig``.
        :param http_config: ``AWS::AppSync::DataSource.HttpConfig``.
        :param lambda_config: ``AWS::AppSync::DataSource.LambdaConfig``.
        :param relational_database_config: ``AWS::AppSync::DataSource.RelationalDatabaseConfig``.
        :param service_role_arn: ``AWS::AppSync::DataSource.ServiceRoleArn``.
        """
        props = CfnDataSourceProps(
            api_id=api_id,
            name=name,
            type=type,
            description=description,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
            service_role_arn=service_role_arn,
        )

        jsii.create(CfnDataSource, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrDataSourceArn")
    def attr_data_source_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: DataSourceArn
        """
        return jsii.get(self, "attrDataSourceArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        """
        :cloudformationAttribute: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::DataSource.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter # type: ignore
    def api_id(self, value: builtins.str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::AppSync::DataSource.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        """``AWS::AppSync::DataSource.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        """
        return jsii.get(self, "type")

    @type.setter # type: ignore
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::DataSource.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dynamoDbConfig")
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.DynamoDBConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        """
        return jsii.get(self, "dynamoDbConfig")

    @dynamo_db_config.setter # type: ignore
    def dynamo_db_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.DynamoDBConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "dynamoDbConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="elasticsearchConfig")
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.ElasticsearchConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        """
        return jsii.get(self, "elasticsearchConfig")

    @elasticsearch_config.setter # type: ignore
    def elasticsearch_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.ElasticsearchConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "elasticsearchConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="httpConfig")
    def http_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.HttpConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        """
        return jsii.get(self, "httpConfig")

    @http_config.setter # type: ignore
    def http_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.HttpConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "httpConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.LambdaConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        """
        return jsii.get(self, "lambdaConfig")

    @lambda_config.setter # type: ignore
    def lambda_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.LambdaConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "lambdaConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="relationalDatabaseConfig")
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.RelationalDatabaseConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        """
        return jsii.get(self, "relationalDatabaseConfig")

    @relational_database_config.setter # type: ignore
    def relational_database_config(
        self,
        value: typing.Optional[typing.Union["CfnDataSource.RelationalDatabaseConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "relationalDatabaseConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::DataSource.ServiceRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        """
        return jsii.get(self, "serviceRoleArn")

    @service_role_arn.setter # type: ignore
    def service_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "serviceRoleArn", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.AuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_type": "authorizationType",
            "aws_iam_config": "awsIamConfig",
        },
    )
    class AuthorizationConfigProperty:
        def __init__(
            self,
            *,
            authorization_type: builtins.str,
            aws_iam_config: typing.Optional[typing.Union["CfnDataSource.AwsIamConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param authorization_type: ``CfnDataSource.AuthorizationConfigProperty.AuthorizationType``.
            :param aws_iam_config: ``CfnDataSource.AuthorizationConfigProperty.AwsIamConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "authorization_type": authorization_type,
            }
            if aws_iam_config is not None:
                self._values["aws_iam_config"] = aws_iam_config

        @builtins.property
        def authorization_type(self) -> builtins.str:
            """``CfnDataSource.AuthorizationConfigProperty.AuthorizationType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-authorizationtype
            """
            result = self._values.get("authorization_type")
            assert result is not None, "Required property 'authorization_type' is missing"
            return result

        @builtins.property
        def aws_iam_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.AwsIamConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnDataSource.AuthorizationConfigProperty.AwsIamConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-authorizationconfig.html#cfn-appsync-datasource-authorizationconfig-awsiamconfig
            """
            result = self._values.get("aws_iam_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.AwsIamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "signing_region": "signingRegion",
            "signing_service_name": "signingServiceName",
        },
    )
    class AwsIamConfigProperty:
        def __init__(
            self,
            *,
            signing_region: typing.Optional[builtins.str] = None,
            signing_service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param signing_region: ``CfnDataSource.AwsIamConfigProperty.SigningRegion``.
            :param signing_service_name: ``CfnDataSource.AwsIamConfigProperty.SigningServiceName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if signing_region is not None:
                self._values["signing_region"] = signing_region
            if signing_service_name is not None:
                self._values["signing_service_name"] = signing_service_name

        @builtins.property
        def signing_region(self) -> typing.Optional[builtins.str]:
            """``CfnDataSource.AwsIamConfigProperty.SigningRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingregion
            """
            result = self._values.get("signing_region")
            return result

        @builtins.property
        def signing_service_name(self) -> typing.Optional[builtins.str]:
            """``CfnDataSource.AwsIamConfigProperty.SigningServiceName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-awsiamconfig.html#cfn-appsync-datasource-awsiamconfig-signingservicename
            """
            result = self._values.get("signing_service_name")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsIamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.DeltaSyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_table_ttl": "baseTableTtl",
            "delta_sync_table_name": "deltaSyncTableName",
            "delta_sync_table_ttl": "deltaSyncTableTtl",
        },
    )
    class DeltaSyncConfigProperty:
        def __init__(
            self,
            *,
            base_table_ttl: builtins.str,
            delta_sync_table_name: builtins.str,
            delta_sync_table_ttl: builtins.str,
        ) -> None:
            """
            :param base_table_ttl: ``CfnDataSource.DeltaSyncConfigProperty.BaseTableTTL``.
            :param delta_sync_table_name: ``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableName``.
            :param delta_sync_table_ttl: ``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableTTL``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "base_table_ttl": base_table_ttl,
                "delta_sync_table_name": delta_sync_table_name,
                "delta_sync_table_ttl": delta_sync_table_ttl,
            }

        @builtins.property
        def base_table_ttl(self) -> builtins.str:
            """``CfnDataSource.DeltaSyncConfigProperty.BaseTableTTL``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-basetablettl
            """
            result = self._values.get("base_table_ttl")
            assert result is not None, "Required property 'base_table_ttl' is missing"
            return result

        @builtins.property
        def delta_sync_table_name(self) -> builtins.str:
            """``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablename
            """
            result = self._values.get("delta_sync_table_name")
            assert result is not None, "Required property 'delta_sync_table_name' is missing"
            return result

        @builtins.property
        def delta_sync_table_ttl(self) -> builtins.str:
            """``CfnDataSource.DeltaSyncConfigProperty.DeltaSyncTableTTL``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.html#cfn-appsync-datasource-deltasyncconfig-deltasynctablettl
            """
            result = self._values.get("delta_sync_table_ttl")
            assert result is not None, "Required property 'delta_sync_table_ttl' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaSyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.DynamoDBConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "table_name": "tableName",
            "delta_sync_config": "deltaSyncConfig",
            "use_caller_credentials": "useCallerCredentials",
            "versioned": "versioned",
        },
    )
    class DynamoDBConfigProperty:
        def __init__(
            self,
            *,
            aws_region: builtins.str,
            table_name: builtins.str,
            delta_sync_config: typing.Optional[typing.Union["CfnDataSource.DeltaSyncConfigProperty", _IResolvable_a771d0ef]] = None,
            use_caller_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            versioned: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param aws_region: ``CfnDataSource.DynamoDBConfigProperty.AwsRegion``.
            :param table_name: ``CfnDataSource.DynamoDBConfigProperty.TableName``.
            :param delta_sync_config: ``CfnDataSource.DynamoDBConfigProperty.DeltaSyncConfig``.
            :param use_caller_credentials: ``CfnDataSource.DynamoDBConfigProperty.UseCallerCredentials``.
            :param versioned: ``CfnDataSource.DynamoDBConfigProperty.Versioned``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "aws_region": aws_region,
                "table_name": table_name,
            }
            if delta_sync_config is not None:
                self._values["delta_sync_config"] = delta_sync_config
            if use_caller_credentials is not None:
                self._values["use_caller_credentials"] = use_caller_credentials
            if versioned is not None:
                self._values["versioned"] = versioned

        @builtins.property
        def aws_region(self) -> builtins.str:
            """``CfnDataSource.DynamoDBConfigProperty.AwsRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-awsregion
            """
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return result

        @builtins.property
        def table_name(self) -> builtins.str:
            """``CfnDataSource.DynamoDBConfigProperty.TableName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-tablename
            """
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return result

        @builtins.property
        def delta_sync_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.DeltaSyncConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnDataSource.DynamoDBConfigProperty.DeltaSyncConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-deltasyncconfig
            """
            result = self._values.get("delta_sync_config")
            return result

        @builtins.property
        def use_caller_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnDataSource.DynamoDBConfigProperty.UseCallerCredentials``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-usecallercredentials
            """
            result = self._values.get("use_caller_credentials")
            return result

        @builtins.property
        def versioned(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnDataSource.DynamoDBConfigProperty.Versioned``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-dynamodbconfig.html#cfn-appsync-datasource-dynamodbconfig-versioned
            """
            result = self._values.get("versioned")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.ElasticsearchConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"aws_region": "awsRegion", "endpoint": "endpoint"},
    )
    class ElasticsearchConfigProperty:
        def __init__(self, *, aws_region: builtins.str, endpoint: builtins.str) -> None:
            """
            :param aws_region: ``CfnDataSource.ElasticsearchConfigProperty.AwsRegion``.
            :param endpoint: ``CfnDataSource.ElasticsearchConfigProperty.Endpoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "aws_region": aws_region,
                "endpoint": endpoint,
            }

        @builtins.property
        def aws_region(self) -> builtins.str:
            """``CfnDataSource.ElasticsearchConfigProperty.AwsRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-awsregion
            """
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return result

        @builtins.property
        def endpoint(self) -> builtins.str:
            """``CfnDataSource.ElasticsearchConfigProperty.Endpoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-elasticsearchconfig.html#cfn-appsync-datasource-elasticsearchconfig-endpoint
            """
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.HttpConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "authorization_config": "authorizationConfig",
        },
    )
    class HttpConfigProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            authorization_config: typing.Optional[typing.Union["CfnDataSource.AuthorizationConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param endpoint: ``CfnDataSource.HttpConfigProperty.Endpoint``.
            :param authorization_config: ``CfnDataSource.HttpConfigProperty.AuthorizationConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint": endpoint,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config

        @builtins.property
        def endpoint(self) -> builtins.str:
            """``CfnDataSource.HttpConfigProperty.Endpoint``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-endpoint
            """
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return result

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.AuthorizationConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnDataSource.HttpConfigProperty.AuthorizationConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-httpconfig.html#cfn-appsync-datasource-httpconfig-authorizationconfig
            """
            result = self._values.get("authorization_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.LambdaConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_function_arn": "lambdaFunctionArn"},
    )
    class LambdaConfigProperty:
        def __init__(self, *, lambda_function_arn: builtins.str) -> None:
            """
            :param lambda_function_arn: ``CfnDataSource.LambdaConfigProperty.LambdaFunctionArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "lambda_function_arn": lambda_function_arn,
            }

        @builtins.property
        def lambda_function_arn(self) -> builtins.str:
            """``CfnDataSource.LambdaConfigProperty.LambdaFunctionArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-lambdaconfig.html#cfn-appsync-datasource-lambdaconfig-lambdafunctionarn
            """
            result = self._values.get("lambda_function_arn")
            assert result is not None, "Required property 'lambda_function_arn' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.RdsHttpEndpointConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "aws_secret_store_arn": "awsSecretStoreArn",
            "db_cluster_identifier": "dbClusterIdentifier",
            "database_name": "databaseName",
            "schema": "schema",
        },
    )
    class RdsHttpEndpointConfigProperty:
        def __init__(
            self,
            *,
            aws_region: builtins.str,
            aws_secret_store_arn: builtins.str,
            db_cluster_identifier: builtins.str,
            database_name: typing.Optional[builtins.str] = None,
            schema: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param aws_region: ``CfnDataSource.RdsHttpEndpointConfigProperty.AwsRegion``.
            :param aws_secret_store_arn: ``CfnDataSource.RdsHttpEndpointConfigProperty.AwsSecretStoreArn``.
            :param db_cluster_identifier: ``CfnDataSource.RdsHttpEndpointConfigProperty.DbClusterIdentifier``.
            :param database_name: ``CfnDataSource.RdsHttpEndpointConfigProperty.DatabaseName``.
            :param schema: ``CfnDataSource.RdsHttpEndpointConfigProperty.Schema``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "aws_region": aws_region,
                "aws_secret_store_arn": aws_secret_store_arn,
                "db_cluster_identifier": db_cluster_identifier,
            }
            if database_name is not None:
                self._values["database_name"] = database_name
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def aws_region(self) -> builtins.str:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.AwsRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awsregion
            """
            result = self._values.get("aws_region")
            assert result is not None, "Required property 'aws_region' is missing"
            return result

        @builtins.property
        def aws_secret_store_arn(self) -> builtins.str:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.AwsSecretStoreArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-awssecretstorearn
            """
            result = self._values.get("aws_secret_store_arn")
            assert result is not None, "Required property 'aws_secret_store_arn' is missing"
            return result

        @builtins.property
        def db_cluster_identifier(self) -> builtins.str:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.DbClusterIdentifier``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-dbclusteridentifier
            """
            result = self._values.get("db_cluster_identifier")
            assert result is not None, "Required property 'db_cluster_identifier' is missing"
            return result

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.DatabaseName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-databasename
            """
            result = self._values.get("database_name")
            return result

        @builtins.property
        def schema(self) -> typing.Optional[builtins.str]:
            """``CfnDataSource.RdsHttpEndpointConfigProperty.Schema``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-rdshttpendpointconfig.html#cfn-appsync-datasource-rdshttpendpointconfig-schema
            """
            result = self._values.get("schema")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsHttpEndpointConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnDataSource.RelationalDatabaseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_database_source_type": "relationalDatabaseSourceType",
            "rds_http_endpoint_config": "rdsHttpEndpointConfig",
        },
    )
    class RelationalDatabaseConfigProperty:
        def __init__(
            self,
            *,
            relational_database_source_type: builtins.str,
            rds_http_endpoint_config: typing.Optional[typing.Union["CfnDataSource.RdsHttpEndpointConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param relational_database_source_type: ``CfnDataSource.RelationalDatabaseConfigProperty.RelationalDatabaseSourceType``.
            :param rds_http_endpoint_config: ``CfnDataSource.RelationalDatabaseConfigProperty.RdsHttpEndpointConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "relational_database_source_type": relational_database_source_type,
            }
            if rds_http_endpoint_config is not None:
                self._values["rds_http_endpoint_config"] = rds_http_endpoint_config

        @builtins.property
        def relational_database_source_type(self) -> builtins.str:
            """``CfnDataSource.RelationalDatabaseConfigProperty.RelationalDatabaseSourceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-relationaldatabasesourcetype
            """
            result = self._values.get("relational_database_source_type")
            assert result is not None, "Required property 'relational_database_source_type' is missing"
            return result

        @builtins.property
        def rds_http_endpoint_config(
            self,
        ) -> typing.Optional[typing.Union["CfnDataSource.RdsHttpEndpointConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnDataSource.RelationalDatabaseConfigProperty.RdsHttpEndpointConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-relationaldatabaseconfig.html#cfn-appsync-datasource-relationaldatabaseconfig-rdshttpendpointconfig
            """
            result = self._values.get("rds_http_endpoint_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalDatabaseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "name": "name",
        "type": "type",
        "description": "description",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
        "service_role_arn": "serviceRoleArn",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dynamo_db_config: typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_a771d0ef]] = None,
        elasticsearch_config: typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_a771d0ef]] = None,
        http_config: typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_a771d0ef]] = None,
        lambda_config: typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_a771d0ef]] = None,
        relational_database_config: typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_a771d0ef]] = None,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::DataSource``.

        :param api_id: ``AWS::AppSync::DataSource.ApiId``.
        :param name: ``AWS::AppSync::DataSource.Name``.
        :param type: ``AWS::AppSync::DataSource.Type``.
        :param description: ``AWS::AppSync::DataSource.Description``.
        :param dynamo_db_config: ``AWS::AppSync::DataSource.DynamoDBConfig``.
        :param elasticsearch_config: ``AWS::AppSync::DataSource.ElasticsearchConfig``.
        :param http_config: ``AWS::AppSync::DataSource.HttpConfig``.
        :param lambda_config: ``AWS::AppSync::DataSource.LambdaConfig``.
        :param relational_database_config: ``AWS::AppSync::DataSource.RelationalDatabaseConfig``.
        :param service_role_arn: ``AWS::AppSync::DataSource.ServiceRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

    @builtins.property
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::DataSource.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-apiid
        """
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::AppSync::DataSource.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def type(self) -> builtins.str:
        """``AWS::AppSync::DataSource.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-type
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::DataSource.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.DynamoDBConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-dynamodbconfig
        """
        result = self._values.get("dynamo_db_config")
        return result

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.ElasticsearchConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-elasticsearchconfig
        """
        result = self._values.get("elasticsearch_config")
        return result

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.HttpConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-httpconfig
        """
        result = self._values.get("http_config")
        return result

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.LambdaConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-lambdaconfig
        """
        result = self._values.get("lambda_config")
        return result

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::DataSource.RelationalDatabaseConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-relationaldatabaseconfig
        """
        result = self._values.get("relational_database_config")
        return result

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::DataSource.ServiceRoleArn``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html#cfn-appsync-datasource-servicerolearn
        """
        result = self._values.get("service_role_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnFunctionConfiguration(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnFunctionConfiguration",
):
    """A CloudFormation ``AWS::AppSync::FunctionConfiguration``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
    :cloudformationResource: AWS::AppSync::FunctionConfiguration
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        api_id: builtins.str,
        data_source_name: builtins.str,
        function_version: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        sync_config: typing.Optional[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::FunctionConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::FunctionConfiguration.ApiId``.
        :param data_source_name: ``AWS::AppSync::FunctionConfiguration.DataSourceName``.
        :param function_version: ``AWS::AppSync::FunctionConfiguration.FunctionVersion``.
        :param name: ``AWS::AppSync::FunctionConfiguration.Name``.
        :param description: ``AWS::AppSync::FunctionConfiguration.Description``.
        :param request_mapping_template: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.
        :param sync_config: ``AWS::AppSync::FunctionConfiguration.SyncConfig``.
        """
        props = CfnFunctionConfigurationProps(
            api_id=api_id,
            data_source_name=data_source_name,
            function_version=function_version,
            name=name,
            description=description,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            sync_config=sync_config,
        )

        jsii.create(CfnFunctionConfiguration, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrDataSourceName")
    def attr_data_source_name(self) -> builtins.str:
        """
        :cloudformationAttribute: DataSourceName
        """
        return jsii.get(self, "attrDataSourceName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrFunctionArn")
    def attr_function_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: FunctionArn
        """
        return jsii.get(self, "attrFunctionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrFunctionId")
    def attr_function_id(self) -> builtins.str:
        """
        :cloudformationAttribute: FunctionId
        """
        return jsii.get(self, "attrFunctionId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        """
        :cloudformationAttribute: Name
        """
        return jsii.get(self, "attrName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter # type: ignore
    def api_id(self, value: builtins.str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.DataSourceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        """
        return jsii.get(self, "dataSourceName")

    @data_source_name.setter # type: ignore
    def data_source_name(self, value: builtins.str) -> None:
        jsii.set(self, "dataSourceName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionVersion")
    def function_version(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.FunctionVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        """
        return jsii.get(self, "functionVersion")

    @function_version.setter # type: ignore
    def function_version(self, value: builtins.str) -> None:
        jsii.set(self, "functionVersion", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        """
        return jsii.get(self, "description")

    @description.setter # type: ignore
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        """
        return jsii.get(self, "requestMappingTemplate")

    @request_mapping_template.setter # type: ignore
    def request_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        """
        return jsii.get(self, "requestMappingTemplateS3Location")

    @request_mapping_template_s3_location.setter # type: ignore
    def request_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        """
        return jsii.get(self, "responseMappingTemplate")

    @response_mapping_template.setter # type: ignore
    def response_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        """
        return jsii.get(self, "responseMappingTemplateS3Location")

    @response_mapping_template_s3_location.setter # type: ignore
    def response_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::FunctionConfiguration.SyncConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig
        """
        return jsii.get(self, "syncConfig")

    @sync_config.setter # type: ignore
    def sync_config(
        self,
        value: typing.Optional[typing.Union["CfnFunctionConfiguration.SyncConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self,
            *,
            lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param lambda_conflict_handler_arn: ``CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty.LambdaConflictHandlerArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if lambda_conflict_handler_arn is not None:
                self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
            """``CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty.LambdaConflictHandlerArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-lambdaconflicthandlerconfig.html#cfn-appsync-functionconfiguration-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            """
            result = self._values.get("lambda_conflict_handler_arn")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnFunctionConfiguration.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: builtins.str,
            conflict_handler: typing.Optional[builtins.str] = None,
            lambda_conflict_handler_config: typing.Optional[typing.Union["CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param conflict_detection: ``CfnFunctionConfiguration.SyncConfigProperty.ConflictDetection``.
            :param conflict_handler: ``CfnFunctionConfiguration.SyncConfigProperty.ConflictHandler``.
            :param lambda_conflict_handler_config: ``CfnFunctionConfiguration.SyncConfigProperty.LambdaConflictHandlerConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> builtins.str:
            """``CfnFunctionConfiguration.SyncConfigProperty.ConflictDetection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflictdetection
            """
            result = self._values.get("conflict_detection")
            assert result is not None, "Required property 'conflict_detection' is missing"
            return result

        @builtins.property
        def conflict_handler(self) -> typing.Optional[builtins.str]:
            """``CfnFunctionConfiguration.SyncConfigProperty.ConflictHandler``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-conflicthandler
            """
            result = self._values.get("conflict_handler")
            return result

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[typing.Union["CfnFunctionConfiguration.LambdaConflictHandlerConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnFunctionConfiguration.SyncConfigProperty.LambdaConflictHandlerConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.html#cfn-appsync-functionconfiguration-syncconfig-lambdaconflicthandlerconfig
            """
            result = self._values.get("lambda_conflict_handler_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnFunctionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "data_source_name": "dataSourceName",
        "function_version": "functionVersion",
        "name": "name",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "sync_config": "syncConfig",
    },
)
class CfnFunctionConfigurationProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        data_source_name: builtins.str,
        function_version: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        sync_config: typing.Optional[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::FunctionConfiguration``.

        :param api_id: ``AWS::AppSync::FunctionConfiguration.ApiId``.
        :param data_source_name: ``AWS::AppSync::FunctionConfiguration.DataSourceName``.
        :param function_version: ``AWS::AppSync::FunctionConfiguration.FunctionVersion``.
        :param name: ``AWS::AppSync::FunctionConfiguration.Name``.
        :param description: ``AWS::AppSync::FunctionConfiguration.Description``.
        :param request_mapping_template: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.
        :param sync_config: ``AWS::AppSync::FunctionConfiguration.SyncConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "data_source_name": data_source_name,
            "function_version": function_version,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values["request_mapping_template_s3_location"] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values["response_mapping_template_s3_location"] = response_mapping_template_s3_location
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-apiid
        """
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return result

    @builtins.property
    def data_source_name(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.DataSourceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-datasourcename
        """
        result = self._values.get("data_source_name")
        assert result is not None, "Required property 'data_source_name' is missing"
        return result

    @builtins.property
    def function_version(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.FunctionVersion``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-functionversion
        """
        result = self._values.get("function_version")
        assert result is not None, "Required property 'function_version' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::AppSync::FunctionConfiguration.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.Description``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-description
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplate
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.RequestMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-requestmappingtemplates3location
        """
        result = self._values.get("request_mapping_template_s3_location")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplate
        """
        result = self._values.get("response_mapping_template")
        return result

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::FunctionConfiguration.ResponseMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-responsemappingtemplates3location
        """
        result = self._values.get("response_mapping_template_s3_location")
        return result

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[CfnFunctionConfiguration.SyncConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::FunctionConfiguration.SyncConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html#cfn-appsync-functionconfiguration-syncconfig
        """
        result = self._values.get("sync_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnGraphQLApi(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnGraphQLApi",
):
    """A CloudFormation ``AWS::AppSync::GraphQLApi``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
    :cloudformationResource: AWS::AppSync::GraphQLApi
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", _IResolvable_a771d0ef]]]] = None,
        log_config: typing.Optional[typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_a771d0ef]] = None,
        open_id_connect_config: typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]] = None,
        user_pool_config: typing.Optional[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_a771d0ef]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::GraphQLApi``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_type: ``AWS::AppSync::GraphQLApi.AuthenticationType``.
        :param name: ``AWS::AppSync::GraphQLApi.Name``.
        :param additional_authentication_providers: ``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.
        :param log_config: ``AWS::AppSync::GraphQLApi.LogConfig``.
        :param open_id_connect_config: ``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.
        :param tags: ``AWS::AppSync::GraphQLApi.Tags``.
        :param user_pool_config: ``AWS::AppSync::GraphQLApi.UserPoolConfig``.
        :param xray_enabled: ``AWS::AppSync::GraphQLApi.XrayEnabled``.
        """
        props = CfnGraphQLApiProps(
            authentication_type=authentication_type,
            name=name,
            additional_authentication_providers=additional_authentication_providers,
            log_config=log_config,
            open_id_connect_config=open_id_connect_config,
            tags=tags,
            user_pool_config=user_pool_config,
            xray_enabled=xray_enabled,
        )

        jsii.create(CfnGraphQLApi, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrApiId")
    def attr_api_id(self) -> builtins.str:
        """
        :cloudformationAttribute: ApiId
        """
        return jsii.get(self, "attrApiId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrGraphQlUrl")
    def attr_graph_ql_url(self) -> builtins.str:
        """
        :cloudformationAttribute: GraphQLUrl
        """
        return jsii.get(self, "attrGraphQlUrl")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0b7ab120:
        """``AWS::AppSync::GraphQLApi.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        """
        return jsii.get(self, "tags")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        """``AWS::AppSync::GraphQLApi.AuthenticationType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        """
        return jsii.get(self, "authenticationType")

    @authentication_type.setter # type: ignore
    def authentication_type(self, value: builtins.str) -> None:
        jsii.set(self, "authenticationType", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """``AWS::AppSync::GraphQLApi.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        """
        return jsii.get(self, "name")

    @name.setter # type: ignore
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="additionalAuthenticationProviders")
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        """
        return jsii.get(self, "additionalAuthenticationProviders")

    @additional_authentication_providers.setter # type: ignore
    def additional_authentication_providers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnGraphQLApi.AdditionalAuthenticationProviderProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "additionalAuthenticationProviders", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="logConfig")
    def log_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.LogConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        """
        return jsii.get(self, "logConfig")

    @log_config.setter # type: ignore
    def log_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.LogConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "logConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="openIdConnectConfig")
    def open_id_connect_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        """
        return jsii.get(self, "openIdConnectConfig")

    @open_id_connect_config.setter # type: ignore
    def open_id_connect_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "openIdConnectConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="userPoolConfig")
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.UserPoolConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        """
        return jsii.get(self, "userPoolConfig")

    @user_pool_config.setter # type: ignore
    def user_pool_config(
        self,
        value: typing.Optional[typing.Union["CfnGraphQLApi.UserPoolConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "userPoolConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="xrayEnabled")
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.XrayEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        """
        return jsii.get(self, "xrayEnabled")

    @xray_enabled.setter # type: ignore
    def xray_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "xrayEnabled", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnGraphQLApi.AdditionalAuthenticationProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "open_id_connect_config": "openIdConnectConfig",
            "user_pool_config": "userPoolConfig",
        },
    )
    class AdditionalAuthenticationProviderProperty:
        def __init__(
            self,
            *,
            authentication_type: builtins.str,
            open_id_connect_config: typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_a771d0ef]] = None,
            user_pool_config: typing.Optional[typing.Union["CfnGraphQLApi.CognitoUserPoolConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param authentication_type: ``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.AuthenticationType``.
            :param open_id_connect_config: ``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.OpenIDConnectConfig``.
            :param user_pool_config: ``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.UserPoolConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "authentication_type": authentication_type,
            }
            if open_id_connect_config is not None:
                self._values["open_id_connect_config"] = open_id_connect_config
            if user_pool_config is not None:
                self._values["user_pool_config"] = user_pool_config

        @builtins.property
        def authentication_type(self) -> builtins.str:
            """``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.AuthenticationType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-authenticationtype
            """
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return result

        @builtins.property
        def open_id_connect_config(
            self,
        ) -> typing.Optional[typing.Union["CfnGraphQLApi.OpenIDConnectConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.OpenIDConnectConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-openidconnectconfig
            """
            result = self._values.get("open_id_connect_config")
            return result

        @builtins.property
        def user_pool_config(
            self,
        ) -> typing.Optional[typing.Union["CfnGraphQLApi.CognitoUserPoolConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnGraphQLApi.AdditionalAuthenticationProviderProperty.UserPoolConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-additionalauthenticationprovider.html#cfn-appsync-graphqlapi-additionalauthenticationprovider-userpoolconfig
            """
            result = self._values.get("user_pool_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalAuthenticationProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnGraphQLApi.CognitoUserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "user_pool_id": "userPoolId",
        },
    )
    class CognitoUserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param app_id_client_regex: ``CfnGraphQLApi.CognitoUserPoolConfigProperty.AppIdClientRegex``.
            :param aws_region: ``CfnGraphQLApi.CognitoUserPoolConfigProperty.AwsRegion``.
            :param user_pool_id: ``CfnGraphQLApi.CognitoUserPoolConfigProperty.UserPoolId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.CognitoUserPoolConfigProperty.AppIdClientRegex``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex
            """
            result = self._values.get("app_id_client_regex")
            return result

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.CognitoUserPoolConfigProperty.AwsRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion
            """
            result = self._values.get("aws_region")
            return result

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.CognitoUserPoolConfigProperty.UserPoolId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid
            """
            result = self._values.get("user_pool_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoUserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnGraphQLApi.LogConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
            "exclude_verbose_content": "excludeVerboseContent",
            "field_log_level": "fieldLogLevel",
        },
    )
    class LogConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
            exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            field_log_level: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param cloud_watch_logs_role_arn: ``CfnGraphQLApi.LogConfigProperty.CloudWatchLogsRoleArn``.
            :param exclude_verbose_content: ``CfnGraphQLApi.LogConfigProperty.ExcludeVerboseContent``.
            :param field_log_level: ``CfnGraphQLApi.LogConfigProperty.FieldLogLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_logs_role_arn is not None:
                self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
            if exclude_verbose_content is not None:
                self._values["exclude_verbose_content"] = exclude_verbose_content
            if field_log_level is not None:
                self._values["field_log_level"] = field_log_level

        @builtins.property
        def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.LogConfigProperty.CloudWatchLogsRoleArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-cloudwatchlogsrolearn
            """
            result = self._values.get("cloud_watch_logs_role_arn")
            return result

        @builtins.property
        def exclude_verbose_content(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnGraphQLApi.LogConfigProperty.ExcludeVerboseContent``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-excludeverbosecontent
            """
            result = self._values.get("exclude_verbose_content")
            return result

        @builtins.property
        def field_log_level(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.LogConfigProperty.FieldLogLevel``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html#cfn-appsync-graphqlapi-logconfig-fieldloglevel
            """
            result = self._values.get("field_log_level")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnGraphQLApi.OpenIDConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_ttl": "authTtl",
            "client_id": "clientId",
            "iat_ttl": "iatTtl",
            "issuer": "issuer",
        },
    )
    class OpenIDConnectConfigProperty:
        def __init__(
            self,
            *,
            auth_ttl: typing.Optional[jsii.Number] = None,
            client_id: typing.Optional[builtins.str] = None,
            iat_ttl: typing.Optional[jsii.Number] = None,
            issuer: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param auth_ttl: ``CfnGraphQLApi.OpenIDConnectConfigProperty.AuthTTL``.
            :param client_id: ``CfnGraphQLApi.OpenIDConnectConfigProperty.ClientId``.
            :param iat_ttl: ``CfnGraphQLApi.OpenIDConnectConfigProperty.IatTTL``.
            :param issuer: ``CfnGraphQLApi.OpenIDConnectConfigProperty.Issuer``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if auth_ttl is not None:
                self._values["auth_ttl"] = auth_ttl
            if client_id is not None:
                self._values["client_id"] = client_id
            if iat_ttl is not None:
                self._values["iat_ttl"] = iat_ttl
            if issuer is not None:
                self._values["issuer"] = issuer

        @builtins.property
        def auth_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.AuthTTL``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-authttl
            """
            result = self._values.get("auth_ttl")
            return result

        @builtins.property
        def client_id(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.ClientId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-clientid
            """
            result = self._values.get("client_id")
            return result

        @builtins.property
        def iat_ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.IatTTL``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-iatttl
            """
            result = self._values.get("iat_ttl")
            return result

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.OpenIDConnectConfigProperty.Issuer``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-openidconnectconfig.html#cfn-appsync-graphqlapi-openidconnectconfig-issuer
            """
            result = self._values.get("issuer")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenIDConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnGraphQLApi.UserPoolConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_id_client_regex": "appIdClientRegex",
            "aws_region": "awsRegion",
            "default_action": "defaultAction",
            "user_pool_id": "userPoolId",
        },
    )
    class UserPoolConfigProperty:
        def __init__(
            self,
            *,
            app_id_client_regex: typing.Optional[builtins.str] = None,
            aws_region: typing.Optional[builtins.str] = None,
            default_action: typing.Optional[builtins.str] = None,
            user_pool_id: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param app_id_client_regex: ``CfnGraphQLApi.UserPoolConfigProperty.AppIdClientRegex``.
            :param aws_region: ``CfnGraphQLApi.UserPoolConfigProperty.AwsRegion``.
            :param default_action: ``CfnGraphQLApi.UserPoolConfigProperty.DefaultAction``.
            :param user_pool_id: ``CfnGraphQLApi.UserPoolConfigProperty.UserPoolId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if app_id_client_regex is not None:
                self._values["app_id_client_regex"] = app_id_client_regex
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if default_action is not None:
                self._values["default_action"] = default_action
            if user_pool_id is not None:
                self._values["user_pool_id"] = user_pool_id

        @builtins.property
        def app_id_client_regex(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.AppIdClientRegex``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-appidclientregex
            """
            result = self._values.get("app_id_client_regex")
            return result

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.AwsRegion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-awsregion
            """
            result = self._values.get("aws_region")
            return result

        @builtins.property
        def default_action(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.DefaultAction``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-defaultaction
            """
            result = self._values.get("default_action")
            return result

        @builtins.property
        def user_pool_id(self) -> typing.Optional[builtins.str]:
            """``CfnGraphQLApi.UserPoolConfigProperty.UserPoolId``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-userpoolconfig.html#cfn-appsync-graphqlapi-userpoolconfig-userpoolid
            """
            result = self._values.get("user_pool_id")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPoolConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnGraphQLApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_type": "authenticationType",
        "name": "name",
        "additional_authentication_providers": "additionalAuthenticationProviders",
        "log_config": "logConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "tags": "tags",
        "user_pool_config": "userPoolConfig",
        "xray_enabled": "xrayEnabled",
    },
)
class CfnGraphQLApiProps:
    def __init__(
        self,
        *,
        authentication_type: builtins.str,
        name: builtins.str,
        additional_authentication_providers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, _IResolvable_a771d0ef]]]] = None,
        log_config: typing.Optional[typing.Union[CfnGraphQLApi.LogConfigProperty, _IResolvable_a771d0ef]] = None,
        open_id_connect_config: typing.Optional[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, _IResolvable_a771d0ef]] = None,
        tags: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]] = None,
        user_pool_config: typing.Optional[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, _IResolvable_a771d0ef]] = None,
        xray_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::GraphQLApi``.

        :param authentication_type: ``AWS::AppSync::GraphQLApi.AuthenticationType``.
        :param name: ``AWS::AppSync::GraphQLApi.Name``.
        :param additional_authentication_providers: ``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.
        :param log_config: ``AWS::AppSync::GraphQLApi.LogConfig``.
        :param open_id_connect_config: ``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.
        :param tags: ``AWS::AppSync::GraphQLApi.Tags``.
        :param user_pool_config: ``AWS::AppSync::GraphQLApi.UserPoolConfig``.
        :param xray_enabled: ``AWS::AppSync::GraphQLApi.XrayEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_type": authentication_type,
            "name": name,
        }
        if additional_authentication_providers is not None:
            self._values["additional_authentication_providers"] = additional_authentication_providers
        if log_config is not None:
            self._values["log_config"] = log_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if tags is not None:
            self._values["tags"] = tags
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def authentication_type(self) -> builtins.str:
        """``AWS::AppSync::GraphQLApi.AuthenticationType``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-authenticationtype
        """
        result = self._values.get("authentication_type")
        assert result is not None, "Required property 'authentication_type' is missing"
        return result

    @builtins.property
    def name(self) -> builtins.str:
        """``AWS::AppSync::GraphQLApi.Name``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def additional_authentication_providers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnGraphQLApi.AdditionalAuthenticationProviderProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::AppSync::GraphQLApi.AdditionalAuthenticationProviders``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-additionalauthenticationproviders
        """
        result = self._values.get("additional_authentication_providers")
        return result

    @builtins.property
    def log_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.LogConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.LogConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig
        """
        result = self._values.get("log_config")
        return result

    @builtins.property
    def open_id_connect_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.OpenIDConnectConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.OpenIDConnectConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-openidconnectconfig
        """
        result = self._values.get("open_id_connect_config")
        return result

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[_IResolvable_a771d0ef, _CfnTag_95fbdc29]]]]:
        """``AWS::AppSync::GraphQLApi.Tags``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags
        """
        result = self._values.get("tags")
        return result

    @builtins.property
    def user_pool_config(
        self,
    ) -> typing.Optional[typing.Union[CfnGraphQLApi.UserPoolConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.UserPoolConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-userpoolconfig
        """
        result = self._values.get("user_pool_config")
        return result

    @builtins.property
    def xray_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::GraphQLApi.XrayEnabled``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled
        """
        result = self._values.get("xray_enabled")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnGraphQLSchema(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnGraphQLSchema",
):
    """A CloudFormation ``AWS::AppSync::GraphQLSchema``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
    :cloudformationResource: AWS::AppSync::GraphQLSchema
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        api_id: builtins.str,
        definition: typing.Optional[builtins.str] = None,
        definition_s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::GraphQLSchema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::GraphQLSchema.ApiId``.
        :param definition: ``AWS::AppSync::GraphQLSchema.Definition``.
        :param definition_s3_location: ``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.
        """
        props = CfnGraphQLSchemaProps(
            api_id=api_id,
            definition=definition,
            definition_s3_location=definition_s3_location,
        )

        jsii.create(CfnGraphQLSchema, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::GraphQLSchema.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter # type: ignore
    def api_id(self, value: builtins.str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::GraphQLSchema.Definition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        """
        return jsii.get(self, "definition")

    @definition.setter # type: ignore
    def definition(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "definition", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definitionS3Location")
    def definition_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        """
        return jsii.get(self, "definitionS3Location")

    @definition_s3_location.setter # type: ignore
    def definition_s3_location(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "definitionS3Location", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnGraphQLSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "definition": "definition",
        "definition_s3_location": "definitionS3Location",
    },
)
class CfnGraphQLSchemaProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        definition: typing.Optional[builtins.str] = None,
        definition_s3_location: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::GraphQLSchema``.

        :param api_id: ``AWS::AppSync::GraphQLSchema.ApiId``.
        :param definition: ``AWS::AppSync::GraphQLSchema.Definition``.
        :param definition_s3_location: ``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
        }
        if definition is not None:
            self._values["definition"] = definition
        if definition_s3_location is not None:
            self._values["definition_s3_location"] = definition_s3_location

    @builtins.property
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::GraphQLSchema.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-apiid
        """
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return result

    @builtins.property
    def definition(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::GraphQLSchema.Definition``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition
        """
        result = self._values.get("definition")
        return result

    @builtins.property
    def definition_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::GraphQLSchema.DefinitionS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location
        """
        result = self._values.get("definition_s3_location")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGraphQLSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnResolver(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.CfnResolver",
):
    """A CloudFormation ``AWS::AppSync::Resolver``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
    :cloudformationResource: AWS::AppSync::Resolver
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        api_id: builtins.str,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_a771d0ef]] = None,
        data_source_name: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        pipeline_config: typing.Optional[typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_a771d0ef]] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        sync_config: typing.Optional[typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Create a new ``AWS::AppSync::Resolver``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::AppSync::Resolver.ApiId``.
        :param field_name: ``AWS::AppSync::Resolver.FieldName``.
        :param type_name: ``AWS::AppSync::Resolver.TypeName``.
        :param caching_config: ``AWS::AppSync::Resolver.CachingConfig``.
        :param data_source_name: ``AWS::AppSync::Resolver.DataSourceName``.
        :param kind: ``AWS::AppSync::Resolver.Kind``.
        :param pipeline_config: ``AWS::AppSync::Resolver.PipelineConfig``.
        :param request_mapping_template: ``AWS::AppSync::Resolver.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::Resolver.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.
        :param sync_config: ``AWS::AppSync::Resolver.SyncConfig``.
        """
        props = CfnResolverProps(
            api_id=api_id,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            data_source_name=data_source_name,
            kind=kind,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            request_mapping_template_s3_location=request_mapping_template_s3_location,
            response_mapping_template=response_mapping_template,
            response_mapping_template_s3_location=response_mapping_template_s3_location,
            sync_config=sync_config,
        )

        jsii.create(CfnResolver, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        """(experimental) Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty # type: ignore
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrFieldName")
    def attr_field_name(self) -> builtins.str:
        """
        :cloudformationAttribute: FieldName
        """
        return jsii.get(self, "attrFieldName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrResolverArn")
    def attr_resolver_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: ResolverArn
        """
        return jsii.get(self, "attrResolverArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrTypeName")
    def attr_type_name(self) -> builtins.str:
        """
        :cloudformationAttribute: TypeName
        """
        return jsii.get(self, "attrTypeName")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::Resolver.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter # type: ignore
    def api_id(self, value: builtins.str) -> None:
        jsii.set(self, "apiId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="fieldName")
    def field_name(self) -> builtins.str:
        """``AWS::AppSync::Resolver.FieldName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        """
        return jsii.get(self, "fieldName")

    @field_name.setter # type: ignore
    def field_name(self, value: builtins.str) -> None:
        jsii.set(self, "fieldName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        """``AWS::AppSync::Resolver.TypeName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        """
        return jsii.get(self, "typeName")

    @type_name.setter # type: ignore
    def type_name(self, value: builtins.str) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cachingConfig")
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::Resolver.CachingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        """
        return jsii.get(self, "cachingConfig")

    @caching_config.setter # type: ignore
    def caching_config(
        self,
        value: typing.Optional[typing.Union["CfnResolver.CachingConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "cachingConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.DataSourceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        """
        return jsii.get(self, "dataSourceName")

    @data_source_name.setter # type: ignore
    def data_source_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "dataSourceName", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="kind")
    def kind(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.Kind``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        """
        return jsii.get(self, "kind")

    @kind.setter # type: ignore
    def kind(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kind", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pipelineConfig")
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::Resolver.PipelineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        """
        return jsii.get(self, "pipelineConfig")

    @pipeline_config.setter # type: ignore
    def pipeline_config(
        self,
        value: typing.Optional[typing.Union["CfnResolver.PipelineConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "pipelineConfig", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="requestMappingTemplate")
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        """
        return jsii.get(self, "requestMappingTemplate")

    @request_mapping_template.setter # type: ignore
    def request_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "requestMappingTemplate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="requestMappingTemplateS3Location")
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        """
        return jsii.get(self, "requestMappingTemplateS3Location")

    @request_mapping_template_s3_location.setter # type: ignore
    def request_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "requestMappingTemplateS3Location", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="responseMappingTemplate")
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        """
        return jsii.get(self, "responseMappingTemplate")

    @response_mapping_template.setter # type: ignore
    def response_mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "responseMappingTemplate", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="responseMappingTemplateS3Location")
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        """
        return jsii.get(self, "responseMappingTemplateS3Location")

    @response_mapping_template_s3_location.setter # type: ignore
    def response_mapping_template_s3_location(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "responseMappingTemplateS3Location", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="syncConfig")
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_a771d0ef]]:
        """``AWS::AppSync::Resolver.SyncConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        """
        return jsii.get(self, "syncConfig")

    @sync_config.setter # type: ignore
    def sync_config(
        self,
        value: typing.Optional[typing.Union["CfnResolver.SyncConfigProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "syncConfig", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnResolver.CachingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"caching_keys": "cachingKeys", "ttl": "ttl"},
    )
    class CachingConfigProperty:
        def __init__(
            self,
            *,
            caching_keys: typing.Optional[typing.List[builtins.str]] = None,
            ttl: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param caching_keys: ``CfnResolver.CachingConfigProperty.CachingKeys``.
            :param ttl: ``CfnResolver.CachingConfigProperty.Ttl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if caching_keys is not None:
                self._values["caching_keys"] = caching_keys
            if ttl is not None:
                self._values["ttl"] = ttl

        @builtins.property
        def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnResolver.CachingConfigProperty.CachingKeys``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-cachingkeys
            """
            result = self._values.get("caching_keys")
            return result

        @builtins.property
        def ttl(self) -> typing.Optional[jsii.Number]:
            """``CfnResolver.CachingConfigProperty.Ttl``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.html#cfn-appsync-resolver-cachingconfig-ttl
            """
            result = self._values.get("ttl")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CachingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnResolver.LambdaConflictHandlerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_conflict_handler_arn": "lambdaConflictHandlerArn"},
    )
    class LambdaConflictHandlerConfigProperty:
        def __init__(
            self,
            *,
            lambda_conflict_handler_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param lambda_conflict_handler_arn: ``CfnResolver.LambdaConflictHandlerConfigProperty.LambdaConflictHandlerArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if lambda_conflict_handler_arn is not None:
                self._values["lambda_conflict_handler_arn"] = lambda_conflict_handler_arn

        @builtins.property
        def lambda_conflict_handler_arn(self) -> typing.Optional[builtins.str]:
            """``CfnResolver.LambdaConflictHandlerConfigProperty.LambdaConflictHandlerArn``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-lambdaconflicthandlerconfig.html#cfn-appsync-resolver-lambdaconflicthandlerconfig-lambdaconflicthandlerarn
            """
            result = self._values.get("lambda_conflict_handler_arn")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConflictHandlerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnResolver.PipelineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"functions": "functions"},
    )
    class PipelineConfigProperty:
        def __init__(
            self,
            *,
            functions: typing.Optional[typing.List[builtins.str]] = None,
        ) -> None:
            """
            :param functions: ``CfnResolver.PipelineConfigProperty.Functions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if functions is not None:
                self._values["functions"] = functions

        @builtins.property
        def functions(self) -> typing.Optional[typing.List[builtins.str]]:
            """``CfnResolver.PipelineConfigProperty.Functions``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-pipelineconfig.html#cfn-appsync-resolver-pipelineconfig-functions
            """
            result = self._values.get("functions")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PipelineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_appsync.CfnResolver.SyncConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_detection": "conflictDetection",
            "conflict_handler": "conflictHandler",
            "lambda_conflict_handler_config": "lambdaConflictHandlerConfig",
        },
    )
    class SyncConfigProperty:
        def __init__(
            self,
            *,
            conflict_detection: builtins.str,
            conflict_handler: typing.Optional[builtins.str] = None,
            lambda_conflict_handler_config: typing.Optional[typing.Union["CfnResolver.LambdaConflictHandlerConfigProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param conflict_detection: ``CfnResolver.SyncConfigProperty.ConflictDetection``.
            :param conflict_handler: ``CfnResolver.SyncConfigProperty.ConflictHandler``.
            :param lambda_conflict_handler_config: ``CfnResolver.SyncConfigProperty.LambdaConflictHandlerConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "conflict_detection": conflict_detection,
            }
            if conflict_handler is not None:
                self._values["conflict_handler"] = conflict_handler
            if lambda_conflict_handler_config is not None:
                self._values["lambda_conflict_handler_config"] = lambda_conflict_handler_config

        @builtins.property
        def conflict_detection(self) -> builtins.str:
            """``CfnResolver.SyncConfigProperty.ConflictDetection``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflictdetection
            """
            result = self._values.get("conflict_detection")
            assert result is not None, "Required property 'conflict_detection' is missing"
            return result

        @builtins.property
        def conflict_handler(self) -> typing.Optional[builtins.str]:
            """``CfnResolver.SyncConfigProperty.ConflictHandler``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-conflicthandler
            """
            result = self._values.get("conflict_handler")
            return result

        @builtins.property
        def lambda_conflict_handler_config(
            self,
        ) -> typing.Optional[typing.Union["CfnResolver.LambdaConflictHandlerConfigProperty", _IResolvable_a771d0ef]]:
            """``CfnResolver.SyncConfigProperty.LambdaConflictHandlerConfig``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.html#cfn-appsync-resolver-syncconfig-lambdaconflicthandlerconfig
            """
            result = self._values.get("lambda_conflict_handler_config")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SyncConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.CfnResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "data_source_name": "dataSourceName",
        "kind": "kind",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "request_mapping_template_s3_location": "requestMappingTemplateS3Location",
        "response_mapping_template": "responseMappingTemplate",
        "response_mapping_template_s3_location": "responseMappingTemplateS3Location",
        "sync_config": "syncConfig",
    },
)
class CfnResolverProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CfnResolver.CachingConfigProperty, _IResolvable_a771d0ef]] = None,
        data_source_name: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        pipeline_config: typing.Optional[typing.Union[CfnResolver.PipelineConfigProperty, _IResolvable_a771d0ef]] = None,
        request_mapping_template: typing.Optional[builtins.str] = None,
        request_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        response_mapping_template: typing.Optional[builtins.str] = None,
        response_mapping_template_s3_location: typing.Optional[builtins.str] = None,
        sync_config: typing.Optional[typing.Union[CfnResolver.SyncConfigProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """Properties for defining a ``AWS::AppSync::Resolver``.

        :param api_id: ``AWS::AppSync::Resolver.ApiId``.
        :param field_name: ``AWS::AppSync::Resolver.FieldName``.
        :param type_name: ``AWS::AppSync::Resolver.TypeName``.
        :param caching_config: ``AWS::AppSync::Resolver.CachingConfig``.
        :param data_source_name: ``AWS::AppSync::Resolver.DataSourceName``.
        :param kind: ``AWS::AppSync::Resolver.Kind``.
        :param pipeline_config: ``AWS::AppSync::Resolver.PipelineConfig``.
        :param request_mapping_template: ``AWS::AppSync::Resolver.RequestMappingTemplate``.
        :param request_mapping_template_s3_location: ``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.
        :param response_mapping_template: ``AWS::AppSync::Resolver.ResponseMappingTemplate``.
        :param response_mapping_template_s3_location: ``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.
        :param sync_config: ``AWS::AppSync::Resolver.SyncConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api_id": api_id,
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if data_source_name is not None:
            self._values["data_source_name"] = data_source_name
        if kind is not None:
            self._values["kind"] = kind
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if request_mapping_template_s3_location is not None:
            self._values["request_mapping_template_s3_location"] = request_mapping_template_s3_location
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if response_mapping_template_s3_location is not None:
            self._values["response_mapping_template_s3_location"] = response_mapping_template_s3_location
        if sync_config is not None:
            self._values["sync_config"] = sync_config

    @builtins.property
    def api_id(self) -> builtins.str:
        """``AWS::AppSync::Resolver.ApiId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-apiid
        """
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return result

    @builtins.property
    def field_name(self) -> builtins.str:
        """``AWS::AppSync::Resolver.FieldName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-fieldname
        """
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return result

    @builtins.property
    def type_name(self) -> builtins.str:
        """``AWS::AppSync::Resolver.TypeName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-typename
        """
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return result

    @builtins.property
    def caching_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.CachingConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::Resolver.CachingConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-cachingconfig
        """
        result = self._values.get("caching_config")
        return result

    @builtins.property
    def data_source_name(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.DataSourceName``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-datasourcename
        """
        result = self._values.get("data_source_name")
        return result

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.Kind``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-kind
        """
        result = self._values.get("kind")
        return result

    @builtins.property
    def pipeline_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.PipelineConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::Resolver.PipelineConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-pipelineconfig
        """
        result = self._values.get("pipeline_config")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplate
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def request_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.RequestMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-requestmappingtemplates3location
        """
        result = self._values.get("request_mapping_template_s3_location")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplate``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplate
        """
        result = self._values.get("response_mapping_template")
        return result

    @builtins.property
    def response_mapping_template_s3_location(self) -> typing.Optional[builtins.str]:
        """``AWS::AppSync::Resolver.ResponseMappingTemplateS3Location``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-responsemappingtemplates3location
        """
        result = self._values.get("response_mapping_template_s3_location")
        return result

    @builtins.property
    def sync_config(
        self,
    ) -> typing.Optional[typing.Union[CfnResolver.SyncConfigProperty, _IResolvable_a771d0ef]]:
        """``AWS::AppSync::Resolver.SyncConfig``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html#cfn-appsync-resolver-syncconfig
        """
        result = self._values.get("sync_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.DataSourceOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "name": "name"},
)
class DataSourceOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Optional configuration for data sources.

        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) The description of the data source.

        :default: - No description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source, overrides the id given by cdk.

        :default: - generated by cdk given the id

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Directive(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.Directive"):
    """(experimental) Directives for types.

    i.e. @aws_iam or @aws_subscribe

    :stability: experimental
    """

    @jsii.member(jsii_name="apiKey")
    @builtins.classmethod
    def api_key(cls) -> "Directive":
        """(experimental) Add the @aws_api_key directive.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "apiKey", [])

    @jsii.member(jsii_name="cognito")
    @builtins.classmethod
    def cognito(cls, *groups: builtins.str) -> "Directive":
        """(experimental) Add the @aws_auth or @aws_cognito_user_pools directive.

        :param groups: the groups to allow access to.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "cognito", [*groups])

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, statement: builtins.str) -> "Directive":
        """(experimental) Add a custom directive.

        :param statement: - the directive statement to append.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "custom", [statement])

    @jsii.member(jsii_name="iam")
    @builtins.classmethod
    def iam(cls) -> "Directive":
        """(experimental) Add the @aws_iam directive.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "iam", [])

    @jsii.member(jsii_name="oidc")
    @builtins.classmethod
    def oidc(cls) -> "Directive":
        """(experimental) Add the @aws_oidc directive.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "oidc", [])

    @jsii.member(jsii_name="subscribe")
    @builtins.classmethod
    def subscribe(cls, *mutations: builtins.str) -> "Directive":
        """(experimental) Add the @aws_subscribe directive.

        Only use for top level Subscription type.

        :param mutations: the mutation fields to link to.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "subscribe", [*mutations])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the directive statement.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="mode")
    def mode(self) -> typing.Optional[AuthorizationType]:
        """(experimental) The authorization type of this directive.

        :default: - not an authorization directive

        :stability: experimental
        """
        return jsii.get(self, "mode")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="mutationFields")
    def mutation_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        """(experimental) Mutation fields for a subscription directive.

        :default: - not a subscription directive

        :stability: experimental
        """
        return jsii.get(self, "mutationFields")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modes")
    def _modes(self) -> typing.Optional[typing.List[AuthorizationType]]:
        """(experimental) the authorization modes for this intermediate type.

        :stability: experimental
        """
        return jsii.get(self, "modes")

    @_modes.setter # type: ignore
    def _modes(self, value: typing.Optional[typing.List[AuthorizationType]]) -> None:
        jsii.set(self, "modes", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.EnumTypeOptions",
    jsii_struct_bases=[],
    name_mapping={"definition": "definition"},
)
class EnumTypeOptions:
    def __init__(self, *, definition: typing.List[builtins.str]) -> None:
        """(experimental) Properties for configuring an Enum Type.

        :param definition: (experimental) the attributes of this type.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "definition": definition,
        }

    @builtins.property
    def definition(self) -> typing.List[builtins.str]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnumTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.ExtendedDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "relational_database_config": "relationalDatabaseConfig",
    },
)
class ExtendedDataSourceProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_a771d0ef]] = None,
        elasticsearch_config: typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_a771d0ef]] = None,
        http_config: typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_a771d0ef]] = None,
        lambda_config: typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_a771d0ef]] = None,
        relational_database_config: typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """(experimental) props used by implementations of BaseDataSource to provide configuration.

        Should not be used directly.

        :param type: (experimental) the type of the AppSync datasource.
        :param dynamo_db_config: (experimental) configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (experimental) configuration for Elasticsearch Datasource. Default: - No config
        :param http_config: (experimental) configuration for HTTP Datasource. Default: - No config
        :param lambda_config: (experimental) configuration for Lambda Datasource. Default: - No config
        :param relational_database_config: (experimental) configuration for RDS Datasource. Default: - No config

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config

    @builtins.property
    def type(self) -> builtins.str:
        """(experimental) the type of the AppSync datasource.

        :stability: experimental
        """
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return result

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_a771d0ef]]:
        """(experimental) configuration for DynamoDB Datasource.

        :default: - No config

        :stability: experimental
        """
        result = self._values.get("dynamo_db_config")
        return result

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_a771d0ef]]:
        """(experimental) configuration for Elasticsearch Datasource.

        :default: - No config

        :stability: experimental
        """
        result = self._values.get("elasticsearch_config")
        return result

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_a771d0ef]]:
        """(experimental) configuration for HTTP Datasource.

        :default: - No config

        :stability: experimental
        """
        result = self._values.get("http_config")
        return result

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_a771d0ef]]:
        """(experimental) configuration for Lambda Datasource.

        :default: - No config

        :stability: experimental
        """
        result = self._values.get("lambda_config")
        return result

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_a771d0ef]]:
        """(experimental) configuration for RDS Datasource.

        :default: - No config

        :stability: experimental
        """
        result = self._values.get("relational_database_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.ExtendedResolverProps",
    jsii_struct_bases=[BaseResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "data_source": "dataSource",
    },
)
class ExtendedResolverProps(BaseResolverProps):
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        data_source: typing.Optional[BaseDataSource] = None,
    ) -> None:
        """(experimental) Additional property for an AppSync resolver for data source reference.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> builtins.str:
        """(experimental) name of the GraphQL field in the given type this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return result

    @builtins.property
    def type_name(self) -> builtins.str:
        """(experimental) name of the GraphQL type this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return result

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List["IAppsyncFunction"]]:
        """(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit

        :stability: experimental
        """
        result = self._values.get("pipeline_config")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        """(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("response_mapping_template")
        return result

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        """(experimental) The data source this resolver is using.

        :default: - No datasource

        :stability: experimental
        """
        result = self._values.get("data_source")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_appsync.FieldLogLevel")
class FieldLogLevel(enum.Enum):
    """(experimental) log-level for fields in AppSync.

    :stability: experimental
    """

    NONE = "NONE"
    """(experimental) No logging.

    :stability: experimental
    """
    ERROR = "ERROR"
    """(experimental) Error logging.

    :stability: experimental
    """
    ALL = "ALL"
    """(experimental) All logging.

    :stability: experimental
    """


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.FieldOptions",
    jsii_struct_bases=[],
    name_mapping={
        "return_type": "returnType",
        "args": "args",
        "directives": "directives",
    },
)
class FieldOptions:
    def __init__(
        self,
        *,
        return_type: "GraphqlType",
        args: typing.Optional[typing.Mapping[builtins.str, "GraphqlType"]] = None,
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """(experimental) Properties for configuring a field.

        :param return_type: (experimental) The return type for this field.
        :param args: (experimental) The arguments for this field. i.e. type Example (first: String second: String) {} - where 'first' and 'second' are key values for args and 'String' is the GraphqlType Default: - no arguments
        :param directives: (experimental) the directives for this field. Default: - no directives

        :stability: experimental
        :options:

        args - the variables and types that define the arguments

        i.e. { string: GraphqlType, string: GraphqlType }
        """
        self._values: typing.Dict[str, typing.Any] = {
            "return_type": return_type,
        }
        if args is not None:
            self._values["args"] = args
        if directives is not None:
            self._values["directives"] = directives

    @builtins.property
    def return_type(self) -> "GraphqlType":
        """(experimental) The return type for this field.

        :stability: experimental
        """
        result = self._values.get("return_type")
        assert result is not None, "Required property 'return_type' is missing"
        return result

    @builtins.property
    def args(self) -> typing.Optional[typing.Mapping[builtins.str, "GraphqlType"]]:
        """(experimental) The arguments for this field.

        i.e. type Example (first: String second: String) {}

        - where 'first' and 'second' are key values for args
          and 'String' is the GraphqlType

        :default: - no arguments

        :stability: experimental
        """
        result = self._values.get("args")
        return result

    @builtins.property
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this field.

        :default: - no directives

        :stability: experimental
        """
        result = self._values.get("directives")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FieldOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.GraphqlApiAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "graphql_api_id": "graphqlApiId",
        "graphql_api_arn": "graphqlApiArn",
    },
)
class GraphqlApiAttributes:
    def __init__(
        self,
        *,
        graphql_api_id: builtins.str,
        graphql_api_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Attributes for GraphQL imports.

        :param graphql_api_id: (experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.
        :param graphql_api_arn: (experimental) the arn for the GraphQL Api. Default: - autogenerated arn

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "graphql_api_id": graphql_api_id,
        }
        if graphql_api_arn is not None:
            self._values["graphql_api_arn"] = graphql_api_arn

    @builtins.property
    def graphql_api_id(self) -> builtins.str:
        """(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        """
        result = self._values.get("graphql_api_id")
        assert result is not None, "Required property 'graphql_api_id' is missing"
        return result

    @builtins.property
    def graphql_api_arn(self) -> typing.Optional[builtins.str]:
        """(experimental) the arn for the GraphQL Api.

        :default: - autogenerated arn

        :stability: experimental
        """
        result = self._values.get("graphql_api_arn")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlApiAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.GraphqlApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "authorization_config": "authorizationConfig",
        "log_config": "logConfig",
        "schema": "schema",
        "xray_enabled": "xrayEnabled",
    },
)
class GraphqlApiProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        authorization_config: typing.Optional[AuthorizationConfig] = None,
        log_config: typing.Optional["LogConfig"] = None,
        schema: typing.Optional["Schema"] = None,
        xray_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        """(experimental) Properties for an AppSync GraphQL API.

        :param name: (experimental) the name of the GraphQL API.
        :param authorization_config: (experimental) Optional authorization configuration. Default: - API Key authorization
        :param log_config: (experimental) Logging configuration for this api. Default: - None
        :param schema: (experimental) GraphQL schema definition. Specify how you want to define your schema. Schema.fromFile(filePath: string) allows schema definition through schema.graphql file Default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        :param xray_enabled: (experimental) A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        :stability: experimental
        """
        if isinstance(authorization_config, dict):
            authorization_config = AuthorizationConfig(**authorization_config)
        if isinstance(log_config, dict):
            log_config = LogConfig(**log_config)
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config
        if log_config is not None:
            self._values["log_config"] = log_config
        if schema is not None:
            self._values["schema"] = schema
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def name(self) -> builtins.str:
        """(experimental) the name of the GraphQL API.

        :stability: experimental
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def authorization_config(self) -> typing.Optional[AuthorizationConfig]:
        """(experimental) Optional authorization configuration.

        :default: - API Key authorization

        :stability: experimental
        """
        result = self._values.get("authorization_config")
        return result

    @builtins.property
    def log_config(self) -> typing.Optional["LogConfig"]:
        """(experimental) Logging configuration for this api.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("log_config")
        return result

    @builtins.property
    def schema(self) -> typing.Optional["Schema"]:
        """(experimental) GraphQL schema definition. Specify how you want to define your schema.

        Schema.fromFile(filePath: string) allows schema definition through schema.graphql file

        :default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)

        :stability: experimental
        """
        result = self._values.get("schema")
        return result

    @builtins.property
    def xray_enabled(self) -> typing.Optional[builtins.bool]:
        """(experimental) A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API.

        :default: - false

        :stability: experimental
        """
        result = self._values.get("xray_enabled")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.GraphqlTypeOptions",
    jsii_struct_bases=[BaseTypeOptions],
    name_mapping={
        "is_list": "isList",
        "is_required": "isRequired",
        "is_required_list": "isRequiredList",
        "intermediate_type": "intermediateType",
    },
)
class GraphqlTypeOptions(BaseTypeOptions):
    def __init__(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
        intermediate_type: typing.Optional["IIntermediateType"] = None,
    ) -> None:
        """(experimental) Options for GraphQL Types.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false
        :param intermediate_type: (experimental) the intermediate type linked to this attribute. Default: - no intermediate type

        :stability: experimental
        :option: objectType - the object type linked to this attribute
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if is_list is not None:
            self._values["is_list"] = is_list
        if is_required is not None:
            self._values["is_required"] = is_required
        if is_required_list is not None:
            self._values["is_required_list"] = is_required_list
        if intermediate_type is not None:
            self._values["intermediate_type"] = intermediate_type

    @builtins.property
    def is_list(self) -> typing.Optional[builtins.bool]:
        """(experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type].

        :default: - false

        :stability: experimental
        """
        result = self._values.get("is_list")
        return result

    @builtins.property
    def is_required(self) -> typing.Optional[builtins.bool]:
        """(experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type!

        :default: - false

        :stability: experimental
        """
        result = self._values.get("is_required")
        return result

    @builtins.property
    def is_required_list(self) -> typing.Optional[builtins.bool]:
        """(experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]!

        :default: - false

        :stability: experimental
        """
        result = self._values.get("is_required_list")
        return result

    @builtins.property
    def intermediate_type(self) -> typing.Optional["IIntermediateType"]:
        """(experimental) the intermediate type linked to this attribute.

        :default: - no intermediate type

        :stability: experimental
        """
        result = self._values.get("intermediate_type")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.HttpDataSourceOptions",
    jsii_struct_bases=[DataSourceOptions],
    name_mapping={
        "description": "description",
        "name": "name",
        "authorization_config": "authorizationConfig",
    },
)
class HttpDataSourceOptions(DataSourceOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        authorization_config: typing.Optional[AwsIamConfig] = None,
    ) -> None:
        """(experimental) Optional configuration for Http data sources.

        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none

        :stability: experimental
        """
        if isinstance(authorization_config, dict):
            authorization_config = AwsIamConfig(**authorization_config)
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) The description of the data source.

        :default: - No description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source, overrides the id given by cdk.

        :default: - generated by cdk given the id

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def authorization_config(self) -> typing.Optional[AwsIamConfig]:
        """(experimental) The authorization config in case the HTTP endpoint requires authorization.

        :default: - none

        :stability: experimental
        """
        result = self._values.get("authorization_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.HttpDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "endpoint": "endpoint",
        "authorization_config": "authorizationConfig",
    },
)
class HttpDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: "IGraphqlApi",
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        endpoint: builtins.str,
        authorization_config: typing.Optional[AwsIamConfig] = None,
    ) -> None:
        """(experimental) Properties for an AppSync http datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param endpoint: (experimental) The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none

        :stability: experimental
        """
        if isinstance(authorization_config, dict):
            authorization_config = AwsIamConfig(**authorization_config)
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
            "endpoint": endpoint,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def api(self) -> "IGraphqlApi":
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def endpoint(self) -> builtins.str:
        """(experimental) The http endpoint.

        :stability: experimental
        """
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return result

    @builtins.property
    def authorization_config(self) -> typing.Optional[AwsIamConfig]:
        """(experimental) The authorization config in case the HTTP endpoint requires authorization.

        :default: - none

        :stability: experimental
        """
        result = self._values.get("authorization_config")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="monocdk.aws_appsync.IAppsyncFunction")
class IAppsyncFunction(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) Interface for AppSync Functions.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IAppsyncFunctionProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) the ARN of the AppSync function.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        """(experimental) the name of this AppSync Function.

        :stability: experimental
        :attribute: true
        """
        ...


class _IAppsyncFunctionProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) Interface for AppSync Functions.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_appsync.IAppsyncFunction"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) the ARN of the AppSync function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        """(experimental) the name of this AppSync Function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "functionId")


@jsii.interface(jsii_type="monocdk.aws_appsync.IField")
class IField(typing_extensions.Protocol):
    """(experimental) A Graphql Field.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IFieldProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isList")
    def is_list(self) -> builtins.bool:
        """(experimental) property determining if this attribute is a list i.e. if true, attribute would be ``[Type]``.

        :default: false

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isRequired")
    def is_required(self) -> builtins.bool:
        """(experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be ``Type!`` and this attribute must always have a value.

        :default: false

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isRequiredList")
    def is_required_list(self) -> builtins.bool:
        """(experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be ``[ Type ]!`` and this attribute's list must always have a value.

        :default: false

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> "Type":
        """(experimental) the type of attribute.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="fieldOptions")
    def field_options(self) -> typing.Optional["ResolvableFieldOptions"]:
        """(experimental) The options to make this field resolvable.

        :default: - not a resolvable field

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="intermediateType")
    def intermediate_type(self) -> typing.Optional["IIntermediateType"]:
        """(experimental) the intermediate type linked to this attribute (i.e. an interface or an object).

        :default: - no intermediate type

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="argsToString")
    def args_to_string(self) -> builtins.str:
        """(experimental) Generate the arguments for this field.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="directivesToString")
    def directives_to_string(
        self,
        modes: typing.Optional[typing.List[AuthorizationType]] = None,
    ) -> builtins.str:
        """(experimental) Generate the directives for this field.

        :param modes: the authorization modes of the graphql api.

        :default: - no authorization modes

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string for this attribute.

        :stability: experimental
        """
        ...


class _IFieldProxy:
    """(experimental) A Graphql Field.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_appsync.IField"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isList")
    def is_list(self) -> builtins.bool:
        """(experimental) property determining if this attribute is a list i.e. if true, attribute would be ``[Type]``.

        :default: false

        :stability: experimental
        """
        return jsii.get(self, "isList")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isRequired")
    def is_required(self) -> builtins.bool:
        """(experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be ``Type!`` and this attribute must always have a value.

        :default: false

        :stability: experimental
        """
        return jsii.get(self, "isRequired")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isRequiredList")
    def is_required_list(self) -> builtins.bool:
        """(experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be ``[ Type ]!`` and this attribute's list must always have a value.

        :default: false

        :stability: experimental
        """
        return jsii.get(self, "isRequiredList")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> "Type":
        """(experimental) the type of attribute.

        :stability: experimental
        """
        return jsii.get(self, "type")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="fieldOptions")
    def field_options(self) -> typing.Optional["ResolvableFieldOptions"]:
        """(experimental) The options to make this field resolvable.

        :default: - not a resolvable field

        :stability: experimental
        """
        return jsii.get(self, "fieldOptions")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="intermediateType")
    def intermediate_type(self) -> typing.Optional["IIntermediateType"]:
        """(experimental) the intermediate type linked to this attribute (i.e. an interface or an object).

        :default: - no intermediate type

        :stability: experimental
        """
        return jsii.get(self, "intermediateType")

    @jsii.member(jsii_name="argsToString")
    def args_to_string(self) -> builtins.str:
        """(experimental) Generate the arguments for this field.

        :stability: experimental
        """
        return jsii.invoke(self, "argsToString", [])

    @jsii.member(jsii_name="directivesToString")
    def directives_to_string(
        self,
        modes: typing.Optional[typing.List[AuthorizationType]] = None,
    ) -> builtins.str:
        """(experimental) Generate the directives for this field.

        :param modes: the authorization modes of the graphql api.

        :default: - no authorization modes

        :stability: experimental
        """
        return jsii.invoke(self, "directivesToString", [modes])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string for this attribute.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])


@jsii.interface(jsii_type="monocdk.aws_appsync.IGraphqlApi")
class IGraphqlApi(_IResource_8c1dbbbd, typing_extensions.Protocol):
    """(experimental) Interface for GraphQL.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IGraphqlApiProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        :attribute: true
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        """(experimental) the ARN of the API.

        :stability: experimental
        :attribute: true
        """
        ...

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _ITable_24826f7e,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "DynamoDbDataSource":
        """(experimental) add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[AwsIamConfig] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        """(experimental) add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _IFunction_6e14f09e,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        """(experimental) add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "NoneDataSource":
        """(experimental) add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        database_cluster: _IDatabaseCluster_2d93b7f0,
        secret_store: _ISecret_22fb8757,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        """(experimental) add a new Rds data source to this API.

        :param id: The data source's id.
        :param database_cluster: The database cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the database cluster.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_e0a482dc) -> builtins.bool:
        """(experimental) Add schema dependency if not imported.

        :param construct: the dependee.

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        """(experimental) creates a new resolver for this datasource and API using the given properties.

        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        """
        ...


class _IGraphqlApiProxy(
    jsii.proxy_for(_IResource_8c1dbbbd) # type: ignore
):
    """(experimental) Interface for GraphQL.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_appsync.IGraphqlApi"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "apiId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        """(experimental) the ARN of the API.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "arn")

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _ITable_24826f7e,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "DynamoDbDataSource":
        """(experimental) add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addDynamoDbDataSource", [id, table, options])

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[AwsIamConfig] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        """(experimental) add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = HttpDataSourceOptions(
            authorization_config=authorization_config,
            description=description,
            name=name,
        )

        return jsii.invoke(self, "addHttpDataSource", [id, endpoint, options])

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _IFunction_6e14f09e,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        """(experimental) add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addLambdaDataSource", [id, lambda_function, options])

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "NoneDataSource":
        """(experimental) add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addNoneDataSource", [id, options])

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        database_cluster: _IDatabaseCluster_2d93b7f0,
        secret_store: _ISecret_22fb8757,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        """(experimental) add a new Rds data source to this API.

        :param id: The data source's id.
        :param database_cluster: The database cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the database cluster.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addRdsDataSource", [id, database_cluster, secret_store, options])

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_e0a482dc) -> builtins.bool:
        """(experimental) Add schema dependency if not imported.

        :param construct: the dependee.

        :stability: experimental
        """
        return jsii.invoke(self, "addSchemaDependency", [construct])

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        """(experimental) creates a new resolver for this datasource and API using the given properties.

        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        """
        props = ExtendedResolverProps(
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return jsii.invoke(self, "createResolver", [props])


@jsii.interface(jsii_type="monocdk.aws_appsync.IIntermediateType")
class IIntermediateType(typing_extensions.Protocol):
    """(experimental) Intermediate Types are types that includes a certain set of fields that define the entirety of your schema.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _IIntermediateTypeProxy

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of this type.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="directives")
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this object type.

        :default: - no directives

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="interfaceTypes")
    def interface_types(self) -> typing.Optional[typing.List["InterfaceType"]]:
        """(experimental) The Interface Types this Intermediate Type implements.

        :default: - no interface types

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="intermediateType")
    def intermediate_type(self) -> typing.Optional["IIntermediateType"]:
        """(experimental) the intermediate type linked to this attribute (i.e. an interface or an object).

        :default: - no intermediate type

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resolvers")
    def resolvers(self) -> typing.Optional[typing.List["Resolver"]]:
        """(experimental) The resolvers linked to this data source.

        :stability: experimental
        """
        ...

    @resolvers.setter # type: ignore
    def resolvers(self, value: typing.Optional[typing.List["Resolver"]]) -> None:
        ...

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Intermediate Type.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="attribute")
    def attribute(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) Create an GraphQL Type representing this Intermediate Type.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        ...

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this object type.

        :stability: experimental
        """
        ...


class _IIntermediateTypeProxy:
    """(experimental) Intermediate Types are types that includes a certain set of fields that define the entirety of your schema.

    :stability: experimental
    """

    __jsii_type__: typing.ClassVar[str] = "monocdk.aws_appsync.IIntermediateType"

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        return jsii.get(self, "definition")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of this type.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="directives")
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this object type.

        :default: - no directives

        :stability: experimental
        """
        return jsii.get(self, "directives")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="interfaceTypes")
    def interface_types(self) -> typing.Optional[typing.List["InterfaceType"]]:
        """(experimental) The Interface Types this Intermediate Type implements.

        :default: - no interface types

        :stability: experimental
        """
        return jsii.get(self, "interfaceTypes")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="intermediateType")
    def intermediate_type(self) -> typing.Optional[IIntermediateType]:
        """(experimental) the intermediate type linked to this attribute (i.e. an interface or an object).

        :default: - no intermediate type

        :stability: experimental
        """
        return jsii.get(self, "intermediateType")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resolvers")
    def resolvers(self) -> typing.Optional[typing.List["Resolver"]]:
        """(experimental) The resolvers linked to this data source.

        :stability: experimental
        """
        return jsii.get(self, "resolvers")

    @resolvers.setter # type: ignore
    def resolvers(self, value: typing.Optional[typing.List["Resolver"]]) -> None:
        jsii.set(self, "resolvers", value)

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Intermediate Type.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        options = AddFieldOptions(field=field, field_name=field_name)

        return jsii.invoke(self, "addField", [options])

    @jsii.member(jsii_name="attribute")
    def attribute(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) Create an GraphQL Type representing this Intermediate Type.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.invoke(self, "attribute", [options])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this object type.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])


class IamResource(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.IamResource"):
    """(experimental) A class used to generate resource arns for AppSync.

    :stability: experimental
    """

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls) -> "IamResource":
        """(experimental) Generate the resource names that accepts all types: ``*``.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "all", [])

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, *arns: builtins.str) -> "IamResource":
        """(experimental) Generate the resource names given custom arns.

        :param arns: The custom arns that need to be permissioned. Example: custom('/types/Query/fields/getExample')

        :stability: experimental
        """
        return jsii.sinvoke(cls, "custom", [*arns])

    @jsii.member(jsii_name="ofType")
    @builtins.classmethod
    def of_type(cls, type: builtins.str, *fields: builtins.str) -> "IamResource":
        """(experimental) Generate the resource names given a type and fields.

        :param type: The type that needs to be allowed.
        :param fields: The fields that need to be allowed, if empty grant permissions to ALL fields. Example: ofType('Query', 'GetExample')

        :stability: experimental
        """
        return jsii.sinvoke(cls, "ofType", [type, *fields])

    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self, api: "GraphqlApi") -> typing.List[builtins.str]:
        """(experimental) Return the Resource ARN.

        :param api: The GraphQL API to give permissions.

        :stability: experimental
        """
        return jsii.invoke(self, "resourceArns", [api])


@jsii.implements(IIntermediateType)
class InputType(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.InputType"):
    """(experimental) Input Types are abstract types that define complex objects.

    They are used in arguments to represent

    :stability: experimental
    """

    def __init__(
        self,
        name: builtins.str,
        *,
        definition: typing.Mapping[builtins.str, IField],
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """
        :param name: -
        :param definition: (experimental) the attributes of this type.
        :param directives: (experimental) the directives for this object type. Default: - no directives

        :stability: experimental
        """
        props = IntermediateTypeOptions(definition=definition, directives=directives)

        jsii.create(InputType, self, [name, props])

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Input Type.

        Input Types must have both fieldName and field options.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        options = AddFieldOptions(field=field, field_name=field_name)

        return jsii.invoke(self, "addField", [options])

    @jsii.member(jsii_name="attribute")
    def attribute(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) Create a GraphQL Type representing this Input Type.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.invoke(self, "attribute", [options])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this input type.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        return jsii.get(self, "definition")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of this type.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modes")
    def _modes(self) -> typing.Optional[typing.List[AuthorizationType]]:
        """(experimental) the authorization modes for this intermediate type.

        :stability: experimental
        """
        return jsii.get(self, "modes")

    @_modes.setter # type: ignore
    def _modes(self, value: typing.Optional[typing.List[AuthorizationType]]) -> None:
        jsii.set(self, "modes", value)


@jsii.implements(IIntermediateType)
class InterfaceType(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.InterfaceType",
):
    """(experimental) Interface Types are abstract types that includes a certain set of fields that other types must include if they implement the interface.

    :stability: experimental
    """

    def __init__(
        self,
        name: builtins.str,
        *,
        definition: typing.Mapping[builtins.str, IField],
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """
        :param name: -
        :param definition: (experimental) the attributes of this type.
        :param directives: (experimental) the directives for this object type. Default: - no directives

        :stability: experimental
        """
        props = IntermediateTypeOptions(definition=definition, directives=directives)

        jsii.create(InterfaceType, self, [name, props])

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Interface Type.

        Interface Types must have both fieldName and field options.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        options = AddFieldOptions(field=field, field_name=field_name)

        return jsii.invoke(self, "addField", [options])

    @jsii.member(jsii_name="attribute")
    def attribute(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) Create a GraphQL Type representing this Intermediate Type.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.invoke(self, "attribute", [options])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this object type.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        return jsii.get(self, "definition")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of this type.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="directives")
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this object type.

        :default: - no directives

        :stability: experimental
        """
        return jsii.get(self, "directives")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modes")
    def _modes(self) -> typing.Optional[typing.List[AuthorizationType]]:
        """(experimental) the authorization modes for this intermediate type.

        :stability: experimental
        """
        return jsii.get(self, "modes")

    @_modes.setter # type: ignore
    def _modes(self, value: typing.Optional[typing.List[AuthorizationType]]) -> None:
        jsii.set(self, "modes", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.IntermediateTypeOptions",
    jsii_struct_bases=[],
    name_mapping={"definition": "definition", "directives": "directives"},
)
class IntermediateTypeOptions:
    def __init__(
        self,
        *,
        definition: typing.Mapping[builtins.str, IField],
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """(experimental) Properties for configuring an Intermediate Type.

        :param definition: (experimental) the attributes of this type.
        :param directives: (experimental) the directives for this object type. Default: - no directives

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "definition": definition,
        }
        if directives is not None:
            self._values["directives"] = directives

    @builtins.property
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return result

    @builtins.property
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this object type.

        :default: - no directives

        :stability: experimental
        """
        result = self._values.get("directives")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntermediateTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KeyCondition(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.KeyCondition",
):
    """(experimental) Factory class for DynamoDB key conditions.

    :stability: experimental
    """

    @jsii.member(jsii_name="beginsWith")
    @builtins.classmethod
    def begins_with(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        """(experimental) Condition (k, arg).

        True if the key attribute k begins with the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "beginsWith", [key_name, arg])

    @jsii.member(jsii_name="between")
    @builtins.classmethod
    def between(
        cls,
        key_name: builtins.str,
        arg1: builtins.str,
        arg2: builtins.str,
    ) -> "KeyCondition":
        """(experimental) Condition k BETWEEN arg1 AND arg2, true if k >= arg1 and k <= arg2.

        :param key_name: -
        :param arg1: -
        :param arg2: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "between", [key_name, arg1, arg2])

    @jsii.member(jsii_name="eq")
    @builtins.classmethod
    def eq(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        """(experimental) Condition k = arg, true if the key attribute k is equal to the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "eq", [key_name, arg])

    @jsii.member(jsii_name="ge")
    @builtins.classmethod
    def ge(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        """(experimental) Condition k >= arg, true if the key attribute k is greater or equal to the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "ge", [key_name, arg])

    @jsii.member(jsii_name="gt")
    @builtins.classmethod
    def gt(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        """(experimental) Condition k > arg, true if the key attribute k is greater than the the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "gt", [key_name, arg])

    @jsii.member(jsii_name="le")
    @builtins.classmethod
    def le(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        """(experimental) Condition k <= arg, true if the key attribute k is less than or equal to the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "le", [key_name, arg])

    @jsii.member(jsii_name="lt")
    @builtins.classmethod
    def lt(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        """(experimental) Condition k < arg, true if the key attribute k is less than the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "lt", [key_name, arg])

    @jsii.member(jsii_name="and")
    def and_(self, key_cond: "KeyCondition") -> "KeyCondition":
        """(experimental) Conjunction between two conditions.

        :param key_cond: -

        :stability: experimental
        """
        return jsii.invoke(self, "and", [key_cond])

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        """(experimental) Renders the key condition to a VTL string.

        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.LogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_verbose_content": "excludeVerboseContent",
        "field_log_level": "fieldLogLevel",
        "role": "role",
    },
)
class LogConfig:
    def __init__(
        self,
        *,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        field_log_level: typing.Optional[FieldLogLevel] = None,
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        """(experimental) Logging configuration for AppSync.

        :param exclude_verbose_content: (experimental) exclude verbose content. Default: false
        :param field_log_level: (experimental) log level for fields. Default: - Use AppSync default
        :param role: (experimental) The role for CloudWatch Logs. Default: - None

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude_verbose_content is not None:
            self._values["exclude_verbose_content"] = exclude_verbose_content
        if field_log_level is not None:
            self._values["field_log_level"] = field_log_level
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def exclude_verbose_content(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
        """(experimental) exclude verbose content.

        :default: false

        :stability: experimental
        """
        result = self._values.get("exclude_verbose_content")
        return result

    @builtins.property
    def field_log_level(self) -> typing.Optional[FieldLogLevel]:
        """(experimental) log level for fields.

        :default: - Use AppSync default

        :stability: experimental
        """
        result = self._values.get("field_log_level")
        return result

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The role for CloudWatch Logs.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("role")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MappingTemplate(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_appsync.MappingTemplate",
):
    """(experimental) MappingTemplates for AppSync resolvers.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _MappingTemplateProxy

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(MappingTemplate, self, [])

    @jsii.member(jsii_name="dynamoDbDeleteItem")
    @builtins.classmethod
    def dynamo_db_delete_item(
        cls,
        key_name: builtins.str,
        id_arg: builtins.str,
    ) -> "MappingTemplate":
        """(experimental) Mapping template to delete a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Mutation argument.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbDeleteItem", [key_name, id_arg])

    @jsii.member(jsii_name="dynamoDbGetItem")
    @builtins.classmethod
    def dynamo_db_get_item(
        cls,
        key_name: builtins.str,
        id_arg: builtins.str,
    ) -> "MappingTemplate":
        """(experimental) Mapping template to get a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Query argument.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbGetItem", [key_name, id_arg])

    @jsii.member(jsii_name="dynamoDbPutItem")
    @builtins.classmethod
    def dynamo_db_put_item(
        cls,
        key: "PrimaryKey",
        values: AttributeValues,
    ) -> "MappingTemplate":
        """(experimental) Mapping template to save a single item to a DynamoDB table.

        :param key: the assigment of Mutation values to the primary key.
        :param values: the assignment of Mutation values to the table attributes.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbPutItem", [key, values])

    @jsii.member(jsii_name="dynamoDbQuery")
    @builtins.classmethod
    def dynamo_db_query(
        cls,
        cond: KeyCondition,
        index_name: typing.Optional[builtins.str] = None,
    ) -> "MappingTemplate":
        """(experimental) Mapping template to query a set of items from a DynamoDB table.

        :param cond: the key condition for the query.
        :param index_name: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbQuery", [cond, index_name])

    @jsii.member(jsii_name="dynamoDbResultItem")
    @builtins.classmethod
    def dynamo_db_result_item(cls) -> "MappingTemplate":
        """(experimental) Mapping template for a single result item from DynamoDB.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbResultItem", [])

    @jsii.member(jsii_name="dynamoDbResultList")
    @builtins.classmethod
    def dynamo_db_result_list(cls) -> "MappingTemplate":
        """(experimental) Mapping template for a result list from DynamoDB.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbResultList", [])

    @jsii.member(jsii_name="dynamoDbScanTable")
    @builtins.classmethod
    def dynamo_db_scan_table(cls) -> "MappingTemplate":
        """(experimental) Mapping template to scan a DynamoDB table to fetch all entries.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "dynamoDbScanTable", [])

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(cls, file_name: builtins.str) -> "MappingTemplate":
        """(experimental) Create a mapping template from the given file.

        :param file_name: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromFile", [file_name])

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, template: builtins.str) -> "MappingTemplate":
        """(experimental) Create a mapping template from the given string.

        :param template: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromString", [template])

    @jsii.member(jsii_name="lambdaRequest")
    @builtins.classmethod
    def lambda_request(
        cls,
        payload: typing.Optional[builtins.str] = None,
    ) -> "MappingTemplate":
        """(experimental) Mapping template to invoke a Lambda function.

        :param payload: the VTL template snippet of the payload to send to the lambda. If no payload is provided all available context fields are sent to the Lambda function

        :stability: experimental
        """
        return jsii.sinvoke(cls, "lambdaRequest", [payload])

    @jsii.member(jsii_name="lambdaResult")
    @builtins.classmethod
    def lambda_result(cls) -> "MappingTemplate":
        """(experimental) Mapping template to return the Lambda result to the caller.

        :stability: experimental
        """
        return jsii.sinvoke(cls, "lambdaResult", [])

    @jsii.member(jsii_name="renderTemplate")
    @abc.abstractmethod
    def render_template(self) -> builtins.str:
        """(experimental) this is called to render the mapping template to a VTL string.

        :stability: experimental
        """
        ...


class _MappingTemplateProxy(MappingTemplate):
    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        """(experimental) this is called to render the mapping template to a VTL string.

        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])


class NoneDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.NoneDataSource",
):
    """(experimental) An AppSync dummy datasource.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        props = NoneDataSourceProps(api=api, description=description, name=name)

        jsii.create(NoneDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.NoneDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={"api": "api", "description": "description", "name": "name"},
)
class NoneDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Properties for an AppSync dummy datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NoneDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IIntermediateType)
class ObjectType(
    InterfaceType,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.ObjectType",
):
    """(experimental) Object Types are types declared by you.

    :stability: experimental
    """

    def __init__(
        self,
        name: builtins.str,
        *,
        interface_types: typing.Optional[typing.List[InterfaceType]] = None,
        definition: typing.Mapping[builtins.str, IField],
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """
        :param name: -
        :param interface_types: (experimental) The Interface Types this Object Type implements. Default: - no interface types
        :param definition: (experimental) the attributes of this type.
        :param directives: (experimental) the directives for this object type. Default: - no directives

        :stability: experimental
        """
        props = ObjectTypeOptions(
            interface_types=interface_types,
            definition=definition,
            directives=directives,
        )

        jsii.create(ObjectType, self, [name, props])

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Object Type.

        Object Types must have both fieldName and field options.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        options = AddFieldOptions(field=field, field_name=field_name)

        return jsii.invoke(self, "addField", [options])

    @jsii.member(jsii_name="generateResolver")
    def _generate_resolver(
        self,
        api: IGraphqlApi,
        field_name: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        return_type: "GraphqlType",
        args: typing.Optional[typing.Mapping[builtins.str, "GraphqlType"]] = None,
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> "Resolver":
        """(experimental) Generate the resolvers linked to this Object Type.

        :param api: -
        :param field_name: -
        :param data_source: (experimental) The data source creating linked to this resolvable field. Default: - no data source
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array or undefined prop will set resolver to be of type unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template
        :param return_type: (experimental) The return type for this field.
        :param args: (experimental) The arguments for this field. i.e. type Example (first: String second: String) {} - where 'first' and 'second' are key values for args and 'String' is the GraphqlType Default: - no arguments
        :param directives: (experimental) the directives for this field. Default: - no directives

        :stability: experimental
        """
        options = ResolvableFieldOptions(
            data_source=data_source,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            return_type=return_type,
            args=args,
            directives=directives,
        )

        return jsii.invoke(self, "generateResolver", [api, field_name, options])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this object type.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="interfaceTypes")
    def interface_types(self) -> typing.Optional[typing.List[InterfaceType]]:
        """(experimental) The Interface Types this Object Type implements.

        :default: - no interface types

        :stability: experimental
        """
        return jsii.get(self, "interfaceTypes")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="resolvers")
    def resolvers(self) -> typing.Optional[typing.List["Resolver"]]:
        """(experimental) The resolvers linked to this data source.

        :stability: experimental
        """
        return jsii.get(self, "resolvers")

    @resolvers.setter # type: ignore
    def resolvers(self, value: typing.Optional[typing.List["Resolver"]]) -> None:
        jsii.set(self, "resolvers", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.ObjectTypeOptions",
    jsii_struct_bases=[IntermediateTypeOptions],
    name_mapping={
        "definition": "definition",
        "directives": "directives",
        "interface_types": "interfaceTypes",
    },
)
class ObjectTypeOptions(IntermediateTypeOptions):
    def __init__(
        self,
        *,
        definition: typing.Mapping[builtins.str, IField],
        directives: typing.Optional[typing.List[Directive]] = None,
        interface_types: typing.Optional[typing.List[InterfaceType]] = None,
    ) -> None:
        """(experimental) Properties for configuring an Object Type.

        :param definition: (experimental) the attributes of this type.
        :param directives: (experimental) the directives for this object type. Default: - no directives
        :param interface_types: (experimental) The Interface Types this Object Type implements. Default: - no interface types

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "definition": definition,
        }
        if directives is not None:
            self._values["directives"] = directives
        if interface_types is not None:
            self._values["interface_types"] = interface_types

    @builtins.property
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return result

    @builtins.property
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this object type.

        :default: - no directives

        :stability: experimental
        """
        result = self._values.get("directives")
        return result

    @builtins.property
    def interface_types(self) -> typing.Optional[typing.List[InterfaceType]]:
        """(experimental) The Interface Types this Object Type implements.

        :default: - no interface types

        :stability: experimental
        """
        result = self._values.get("interface_types")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ObjectTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.OpenIdConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "oidc_provider": "oidcProvider",
        "client_id": "clientId",
        "token_expiry_from_auth": "tokenExpiryFromAuth",
        "token_expiry_from_issue": "tokenExpiryFromIssue",
    },
)
class OpenIdConnectConfig:
    def __init__(
        self,
        *,
        oidc_provider: builtins.str,
        client_id: typing.Optional[builtins.str] = None,
        token_expiry_from_auth: typing.Optional[jsii.Number] = None,
        token_expiry_from_issue: typing.Optional[jsii.Number] = None,
    ) -> None:
        """(experimental) Configuration for OpenID Connect authorization in AppSync.

        :param oidc_provider: (experimental) The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.
        :param client_id: (experimental) The client identifier of the Relying party at the OpenID identity provider. A regular expression can be specified so AppSync can validate against multiple client identifiers at a time. Default: - - (All)
        :param token_expiry_from_auth: (experimental) The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider. ``auth_time`` claim in OIDC token is required for this validation to work. Default: - no validation
        :param token_expiry_from_issue: (experimental) The number of milliseconds an OIDC token is valid after being issued to a user. This validation uses ``iat`` claim of OIDC token. Default: - no validation

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "oidc_provider": oidc_provider,
        }
        if client_id is not None:
            self._values["client_id"] = client_id
        if token_expiry_from_auth is not None:
            self._values["token_expiry_from_auth"] = token_expiry_from_auth
        if token_expiry_from_issue is not None:
            self._values["token_expiry_from_issue"] = token_expiry_from_issue

    @builtins.property
    def oidc_provider(self) -> builtins.str:
        """(experimental) The issuer for the OIDC configuration.

        The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.

        :stability: experimental
        """
        result = self._values.get("oidc_provider")
        assert result is not None, "Required property 'oidc_provider' is missing"
        return result

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        """(experimental) The client identifier of the Relying party at the OpenID identity provider.

        A regular expression can be specified so AppSync can validate against multiple client identifiers at a time.

        :default:

        -
        - (All)

        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            -"ABCD|CDEF"whereABCDandCDEFaretwodifferentclient_id
        """
        result = self._values.get("client_id")
        return result

    @builtins.property
    def token_expiry_from_auth(self) -> typing.Optional[jsii.Number]:
        """(experimental) The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider.

        ``auth_time`` claim in OIDC token is required for this validation to work.

        :default: - no validation

        :stability: experimental
        """
        result = self._values.get("token_expiry_from_auth")
        return result

    @builtins.property
    def token_expiry_from_issue(self) -> typing.Optional[jsii.Number]:
        """(experimental) The number of milliseconds an OIDC token is valid after being issued to a user.

        This validation uses ``iat`` claim of OIDC token.

        :default: - no validation

        :stability: experimental
        """
        result = self._values.get("token_expiry_from_issue")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKeyStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.PartitionKeyStep",
):
    """(experimental) Utility class to allow assigning a value or an auto-generated id to a partition key.

    :stability: experimental
    """

    def __init__(self, key: builtins.str) -> None:
        """
        :param key: -

        :stability: experimental
        """
        jsii.create(PartitionKeyStep, self, [key])

    @jsii.member(jsii_name="auto")
    def auto(self) -> "PartitionKey":
        """(experimental) Assign an auto-generated value to the partition key.

        :stability: experimental
        """
        return jsii.invoke(self, "auto", [])

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> "PartitionKey":
        """(experimental) Assign an auto-generated value to the partition key.

        :param val: -

        :stability: experimental
        """
        return jsii.invoke(self, "is", [val])


class PrimaryKey(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.PrimaryKey"):
    """(experimental) Specifies the assignment to the primary key.

    It either
    contains the full primary key or only the partition key.

    :stability: experimental
    """

    def __init__(self, pkey: Assign, skey: typing.Optional[Assign] = None) -> None:
        """
        :param pkey: -
        :param skey: -

        :stability: experimental
        """
        jsii.create(PrimaryKey, self, [pkey, skey])

    @jsii.member(jsii_name="partition")
    @builtins.classmethod
    def partition(cls, key: builtins.str) -> PartitionKeyStep:
        """(experimental) Allows assigning a value to the partition key.

        :param key: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "partition", [key])

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        """(experimental) Renders the key assignment to a VTL string.

        :stability: experimental
        """
        return jsii.invoke(self, "renderTemplate", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="pkey")
    def _pkey(self) -> Assign:
        """
        :stability: experimental
        """
        return jsii.get(self, "pkey")


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.ResolvableFieldOptions",
    jsii_struct_bases=[FieldOptions],
    name_mapping={
        "return_type": "returnType",
        "args": "args",
        "directives": "directives",
        "data_source": "dataSource",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
    },
)
class ResolvableFieldOptions(FieldOptions):
    def __init__(
        self,
        *,
        return_type: "GraphqlType",
        args: typing.Optional[typing.Mapping[builtins.str, "GraphqlType"]] = None,
        directives: typing.Optional[typing.List[Directive]] = None,
        data_source: typing.Optional[BaseDataSource] = None,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> None:
        """(experimental) Properties for configuring a resolvable field.

        :param return_type: (experimental) The return type for this field.
        :param args: (experimental) The arguments for this field. i.e. type Example (first: String second: String) {} - where 'first' and 'second' are key values for args and 'String' is the GraphqlType Default: - no arguments
        :param directives: (experimental) the directives for this field. Default: - no directives
        :param data_source: (experimental) The data source creating linked to this resolvable field. Default: - no data source
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array or undefined prop will set resolver to be of type unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        :options: responseMappingTemplate - the mapping template for responses from this resolver
        """
        self._values: typing.Dict[str, typing.Any] = {
            "return_type": return_type,
        }
        if args is not None:
            self._values["args"] = args
        if directives is not None:
            self._values["directives"] = directives
        if data_source is not None:
            self._values["data_source"] = data_source
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def return_type(self) -> "GraphqlType":
        """(experimental) The return type for this field.

        :stability: experimental
        """
        result = self._values.get("return_type")
        assert result is not None, "Required property 'return_type' is missing"
        return result

    @builtins.property
    def args(self) -> typing.Optional[typing.Mapping[builtins.str, "GraphqlType"]]:
        """(experimental) The arguments for this field.

        i.e. type Example (first: String second: String) {}

        - where 'first' and 'second' are key values for args
          and 'String' is the GraphqlType

        :default: - no arguments

        :stability: experimental
        """
        result = self._values.get("args")
        return result

    @builtins.property
    def directives(self) -> typing.Optional[typing.List[Directive]]:
        """(experimental) the directives for this field.

        :default: - no directives

        :stability: experimental
        """
        result = self._values.get("directives")
        return result

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        """(experimental) The data source creating linked to this resolvable field.

        :default: - no data source

        :stability: experimental
        """
        result = self._values.get("data_source")
        return result

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List[IAppsyncFunction]]:
        """(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array or undefined prop will set resolver to be of type unit

        :stability: experimental
        """
        result = self._values.get("pipeline_config")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        """(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        """(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("response_mapping_template")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolvableFieldOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Resolver(
    _Construct_e78e779f,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.Resolver",
):
    """(experimental) An AppSync resolver.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param api: (experimental) The API this resolver is attached to.
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        """
        props = ResolverProps(
            api=api,
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        jsii.create(Resolver, self, [scope, id, props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        """(experimental) the ARN of the resolver.

        :stability: experimental
        """
        return jsii.get(self, "arn")


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.ResolverProps",
    jsii_struct_bases=[ExtendedResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "data_source": "dataSource",
        "api": "api",
    },
)
class ResolverProps(ExtendedResolverProps):
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        data_source: typing.Optional[BaseDataSource] = None,
        api: IGraphqlApi,
    ) -> None:
        """(experimental) Additional property for an AppSync resolver for GraphQL API reference.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param api: (experimental) The API this resolver is attached to.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
            "api": api,
        }
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> builtins.str:
        """(experimental) name of the GraphQL field in the given type this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return result

    @builtins.property
    def type_name(self) -> builtins.str:
        """(experimental) name of the GraphQL type this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return result

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List[IAppsyncFunction]]:
        """(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit

        :stability: experimental
        """
        result = self._values.get("pipeline_config")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        """(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        """(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        """
        result = self._values.get("response_mapping_template")
        return result

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        """(experimental) The data source this resolver is using.

        :default: - No datasource

        :stability: experimental
        """
        result = self._values.get("data_source")
        return result

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) The API this resolver is attached to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Schema(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.Schema"):
    """(experimental) The Schema for a GraphQL Api.

    If no options are configured, schema will be generated
    code-first.

    :stability: experimental
    """

    def __init__(self, *, file_path: typing.Optional[builtins.str] = None) -> None:
        """
        :param file_path: (experimental) The file path for the schema. When this option is configured, then the schema will be generated from an existing file from disk. Default: - schema not configured through disk asset

        :stability: experimental
        """
        options = SchemaOptions(file_path=file_path)

        jsii.create(Schema, self, [options])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(cls, file_path: builtins.str) -> "Schema":
        """(experimental) Generate a Schema from file.

        :param file_path: the file path of the schema file.

        :return: ``SchemaAsset`` with immutable schema defintion

        :stability: experimental
        """
        return jsii.sinvoke(cls, "fromAsset", [file_path])

    @jsii.member(jsii_name="addMutation")
    def add_mutation(
        self,
        field_name: builtins.str,
        field: "ResolvableField",
    ) -> ObjectType:
        """(experimental) Add a mutation field to the schema's Mutation. CDK will create an Object Type called 'Mutation'. For example,.

        type Mutation {
        fieldName: Field.returnType
        }

        :param field_name: the name of the Mutation.
        :param field: the resolvable field to for this Mutation.

        :stability: experimental
        """
        return jsii.invoke(self, "addMutation", [field_name, field])

    @jsii.member(jsii_name="addQuery")
    def add_query(
        self,
        field_name: builtins.str,
        field: "ResolvableField",
    ) -> ObjectType:
        """(experimental) Add a query field to the schema's Query. CDK will create an Object Type called 'Query'. For example,.

        type Query {
        fieldName: Field.returnType
        }

        :param field_name: the name of the query.
        :param field: the resolvable field to for this query.

        :stability: experimental
        """
        return jsii.invoke(self, "addQuery", [field_name, field])

    @jsii.member(jsii_name="addSubscription")
    def add_subscription(
        self,
        field_name: builtins.str,
        field: "ResolvableField",
    ) -> ObjectType:
        """(experimental) Add a subscription field to the schema's Subscription. CDK will create an Object Type called 'Subscription'. For example,.

        type Subscription {
        fieldName: Field.returnType
        }

        :param field_name: the name of the Subscription.
        :param field: the resolvable field to for this Subscription.

        :stability: experimental
        """
        return jsii.invoke(self, "addSubscription", [field_name, field])

    @jsii.member(jsii_name="addToSchema")
    def add_to_schema(
        self,
        addition: builtins.str,
        delimiter: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Escape hatch to add to Schema as desired.

        Will always result
        in a newline.

        :param addition: the addition to add to schema.
        :param delimiter: the delimiter between schema and addition.

        :default: - ''

        :stability: experimental
        """
        return jsii.invoke(self, "addToSchema", [addition, delimiter])

    @jsii.member(jsii_name="addType")
    def add_type(self, type: IIntermediateType) -> IIntermediateType:
        """(experimental) Add type to the schema.

        :param type: the intermediate type to add to the schema.

        :stability: experimental
        """
        return jsii.invoke(self, "addType", [type])

    @jsii.member(jsii_name="bind")
    def bind(self, api: "GraphqlApi") -> CfnGraphQLSchema:
        """(experimental) Called when the GraphQL Api is initialized to allow this object to bind to the stack.

        :param api: The binding GraphQL Api.

        :stability: experimental
        """
        return jsii.invoke(self, "bind", [api])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        """(experimental) The definition for this schema.

        :stability: experimental
        """
        return jsii.get(self, "definition")

    @definition.setter # type: ignore
    def definition(self, value: builtins.str) -> None:
        jsii.set(self, "definition", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.SchemaOptions",
    jsii_struct_bases=[],
    name_mapping={"file_path": "filePath"},
)
class SchemaOptions:
    def __init__(self, *, file_path: typing.Optional[builtins.str] = None) -> None:
        """(experimental) The options for configuring a schema.

        If no options are specified, then the schema will
        be generated code-first.

        :param file_path: (experimental) The file path for the schema. When this option is configured, then the schema will be generated from an existing file from disk. Default: - schema not configured through disk asset

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if file_path is not None:
            self._values["file_path"] = file_path

    @builtins.property
    def file_path(self) -> typing.Optional[builtins.str]:
        """(experimental) The file path for the schema.

        When this option is
        configured, then the schema will be generated from an
        existing file from disk.

        :default: - schema not configured through disk asset

        :stability: experimental
        """
        result = self._values.get("file_path")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SortKeyStep(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.SortKeyStep"):
    """(experimental) Utility class to allow assigning a value or an auto-generated id to a sort key.

    :stability: experimental
    """

    def __init__(self, pkey: Assign, skey: builtins.str) -> None:
        """
        :param pkey: -
        :param skey: -

        :stability: experimental
        """
        jsii.create(SortKeyStep, self, [pkey, skey])

    @jsii.member(jsii_name="auto")
    def auto(self) -> PrimaryKey:
        """(experimental) Assign an auto-generated value to the sort key.

        :stability: experimental
        """
        return jsii.invoke(self, "auto", [])

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> PrimaryKey:
        """(experimental) Assign an auto-generated value to the sort key.

        :param val: -

        :stability: experimental
        """
        return jsii.invoke(self, "is", [val])


@jsii.enum(jsii_type="monocdk.aws_appsync.Type")
class Type(enum.Enum):
    """(experimental) Enum containing the Types that can be used to define ObjectTypes.

    :stability: experimental
    """

    ID = "ID"
    """(experimental) ``ID`` scalar type is a unique identifier. ``ID`` type is serialized similar to ``String``.

    Often used as a key for a cache and not intended to be human-readable.

    :stability: experimental
    """
    STRING = "STRING"
    """(experimental) ``String`` scalar type is a free-form human-readable text.

    :stability: experimental
    """
    INT = "INT"
    """(experimental) ``Int`` scalar type is a signed non-fractional numerical value.

    :stability: experimental
    """
    FLOAT = "FLOAT"
    """(experimental) ``Float`` scalar type is a signed double-precision fractional value.

    :stability: experimental
    """
    BOOLEAN = "BOOLEAN"
    """(experimental) ``Boolean`` scalar type is a boolean value: true or false.

    :stability: experimental
    """
    AWS_DATE = "AWS_DATE"
    """(experimental) ``AWSDate`` scalar type represents a valid extended ``ISO 8601 Date`` string.

    In other words, accepts date strings in the form of ``YYYY-MM-DD``. It accepts time zone offsets.

    :see: https://en.wikipedia.org/wiki/ISO_8601#Calendar_dates
    :stability: experimental
    """
    AWS_TIME = "AWS_TIME"
    """(experimental) ``AWSTime`` scalar type represents a valid extended ``ISO 8601 Time`` string.

    In other words, accepts date strings in the form of ``hh:mm:ss.sss``. It accepts time zone offsets.

    :see: https://en.wikipedia.org/wiki/ISO_8601#Times
    :stability: experimental
    """
    AWS_DATE_TIME = "AWS_DATE_TIME"
    """(experimental) ``AWSDateTime`` scalar type represents a valid extended ``ISO 8601 DateTime`` string.

    In other words, accepts date strings in the form of ``YYYY-MM-DDThh:mm:ss.sssZ``. It accepts time zone offsets.

    :see: https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations
    :stability: experimental
    """
    AWS_TIMESTAMP = "AWS_TIMESTAMP"
    """(experimental) ``AWSTimestamp`` scalar type represents the number of seconds since ``1970-01-01T00:00Z``.

    Timestamps are serialized and deserialized as numbers.

    :stability: experimental
    """
    AWS_EMAIL = "AWS_EMAIL"
    """(experimental) ``AWSEmail`` scalar type represents an email address string (i.e.``username@example.com``).

    :stability: experimental
    """
    AWS_JSON = "AWS_JSON"
    """(experimental) ``AWSJson`` scalar type represents a JSON string.

    :stability: experimental
    """
    AWS_URL = "AWS_URL"
    """(experimental) ``AWSURL`` scalar type represetns a valid URL string.

    URLs wihtout schemes or contain double slashes are considered invalid.

    :stability: experimental
    """
    AWS_PHONE = "AWS_PHONE"
    """(experimental) ``AWSPhone`` scalar type represents a valid phone number. Phone numbers maybe be whitespace delimited or hyphenated.

    The number can specify a country code at the beginning, but is not required for US phone numbers.

    :stability: experimental
    """
    AWS_IP_ADDRESS = "AWS_IP_ADDRESS"
    """(experimental) ``AWSIPAddress`` scalar type respresents a valid ``IPv4`` of ``IPv6`` address string.

    :stability: experimental
    """
    INTERMEDIATE = "INTERMEDIATE"
    """(experimental) Type used for Intermediate Types (i.e. an interface or an object type).

    :stability: experimental
    """


@jsii.implements(IIntermediateType)
class UnionType(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.UnionType"):
    """(experimental) Union Types are abstract types that are similar to Interface Types, but they cannot to specify any common fields between types.

    Note that fields of a union type need to be object types. In other words,
    you can't create a union type out of interfaces, other unions, or inputs.

    :stability: experimental
    """

    def __init__(
        self,
        name: builtins.str,
        *,
        definition: typing.List[IIntermediateType],
    ) -> None:
        """
        :param name: -
        :param definition: (experimental) the object types for this union type.

        :stability: experimental
        """
        options = UnionTypeOptions(definition=definition)

        jsii.create(UnionType, self, [name, options])

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Union Type.

        Input Types must have field options and the IField must be an Object Type.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        options = AddFieldOptions(field=field, field_name=field_name)

        return jsii.invoke(self, "addField", [options])

    @jsii.member(jsii_name="attribute")
    def attribute(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) Create a GraphQL Type representing this Union Type.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.invoke(self, "attribute", [options])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this Union type.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        return jsii.get(self, "definition")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of this type.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modes")
    def _modes(self) -> typing.Optional[typing.List[AuthorizationType]]:
        """(experimental) the authorization modes supported by this intermediate type.

        :stability: experimental
        """
        return jsii.get(self, "modes")

    @_modes.setter # type: ignore
    def _modes(self, value: typing.Optional[typing.List[AuthorizationType]]) -> None:
        jsii.set(self, "modes", value)


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.UnionTypeOptions",
    jsii_struct_bases=[],
    name_mapping={"definition": "definition"},
)
class UnionTypeOptions:
    def __init__(self, *, definition: typing.List[IIntermediateType]) -> None:
        """(experimental) Properties for configuring an Union Type.

        :param definition: (experimental) the object types for this union type.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "definition": definition,
        }

    @builtins.property
    def definition(self) -> typing.List[IIntermediateType]:
        """(experimental) the object types for this union type.

        :stability: experimental
        """
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UnionTypeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.UserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "app_id_client_regex": "appIdClientRegex",
        "default_action": "defaultAction",
    },
)
class UserPoolConfig:
    def __init__(
        self,
        *,
        user_pool: _IUserPool_5e500460,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        default_action: typing.Optional["UserPoolDefaultAction"] = None,
    ) -> None:
        """(experimental) Configuration for Cognito user-pools in AppSync.

        :param user_pool: (experimental) The Cognito user pool to use as identity source.
        :param app_id_client_regex: (experimental) the optional app id regex. Default: - None
        :param default_action: (experimental) Default auth action. Default: ALLOW

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "user_pool": user_pool,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if default_action is not None:
            self._values["default_action"] = default_action

    @builtins.property
    def user_pool(self) -> _IUserPool_5e500460:
        """(experimental) The Cognito user pool to use as identity source.

        :stability: experimental
        """
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return result

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        """(experimental) the optional app id regex.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("app_id_client_regex")
        return result

    @builtins.property
    def default_action(self) -> typing.Optional["UserPoolDefaultAction"]:
        """(experimental) Default auth action.

        :default: ALLOW

        :stability: experimental
        """
        result = self._values.get("default_action")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="monocdk.aws_appsync.UserPoolDefaultAction")
class UserPoolDefaultAction(enum.Enum):
    """(experimental) enum with all possible values for Cognito user-pool default actions.

    :stability: experimental
    """

    ALLOW = "ALLOW"
    """(experimental) ALLOW access to API.

    :stability: experimental
    """
    DENY = "DENY"
    """(experimental) DENY access to API.

    :stability: experimental
    """


class Values(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.Values"):
    """(experimental) Factory class for attribute value assignments.

    :stability: experimental
    """

    def __init__(self) -> None:
        """
        :stability: experimental
        """
        jsii.create(Values, self, [])

    @jsii.member(jsii_name="attribute")
    @builtins.classmethod
    def attribute(cls, attr: builtins.str) -> AttributeValuesStep:
        """(experimental) Allows assigning a value to the specified attribute.

        :param attr: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "attribute", [attr])

    @jsii.member(jsii_name="projecting")
    @builtins.classmethod
    def projecting(cls, arg: typing.Optional[builtins.str] = None) -> AttributeValues:
        """(experimental) Treats the specified object as a map of assignments, where the property names represent attribute names.

        It’s opinionated about how it represents
        some of the nested objects: e.g., it will use lists (“L”) rather than sets
        (“SS”, “NS”, “BS”). By default it projects the argument container ("$ctx.args").

        :param arg: -

        :stability: experimental
        """
        return jsii.sinvoke(cls, "projecting", [arg])


@jsii.implements(IAppsyncFunction)
class AppsyncFunction(
    _Resource_abff4495,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.AppsyncFunction",
):
    """(experimental) AppSync Functions are local functions that perform certain operations onto a backend data source.

    Developers can compose operations (Functions)
    and execute them in sequence with Pipeline Resolvers.

    :stability: experimental
    :resource: AWS::AppSync::FunctionConfiguration
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        data_source: BaseDataSource,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param api: (experimental) the GraphQL Api linked to this AppSync Function.
        :param data_source: (experimental) the data source linked to this AppSync Function.
        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template

        :stability: experimental
        """
        props = AppsyncFunctionProps(
            api=api,
            data_source=data_source,
            name=name,
            description=description,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        jsii.create(AppsyncFunction, self, [scope, id, props])

    @jsii.member(jsii_name="fromAppsyncFunctionAttributes")
    @builtins.classmethod
    def from_appsync_function_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        function_arn: builtins.str,
    ) -> IAppsyncFunction:
        """(experimental) Import Appsync Function from arn.

        :param scope: -
        :param id: -
        :param function_arn: (experimental) the ARN of the AppSync function.

        :stability: experimental
        """
        attrs = AppsyncFunctionAttributes(function_arn=function_arn)

        return jsii.sinvoke(cls, "fromAppsyncFunctionAttributes", [scope, id, attrs])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> BaseDataSource:
        """(experimental) the data source of this AppSync Function.

        :stability: experimental
        :attribute: DataSourceName
        """
        return jsii.get(self, "dataSource")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        """(experimental) the ARN of the AppSync function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "functionArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        """(experimental) the ID of the AppSync function.

        :stability: experimental
        :attribute: true
        """
        return jsii.get(self, "functionId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        """(experimental) the name of this AppSync Function.

        :stability: experimental
        :attribute: Name
        """
        return jsii.get(self, "functionName")


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.AppsyncFunctionProps",
    jsii_struct_bases=[BaseAppsyncFunctionProps],
    name_mapping={
        "name": "name",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "api": "api",
        "data_source": "dataSource",
    },
)
class AppsyncFunctionProps(BaseAppsyncFunctionProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        api: IGraphqlApi,
        data_source: BaseDataSource,
    ) -> None:
        """(experimental) the CDK properties for AppSync Functions.

        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template
        :param api: (experimental) the GraphQL Api linked to this AppSync Function.
        :param data_source: (experimental) the data source linked to this AppSync Function.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "api": api,
            "data_source": data_source,
        }
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def name(self) -> builtins.str:
        """(experimental) the name of the AppSync Function.

        :stability: experimental
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description for this AppSync Function.

        :default: - no description

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        """(experimental) the request mapping template for the AppSync Function.

        :default: - no request mapping template

        :stability: experimental
        """
        result = self._values.get("request_mapping_template")
        return result

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        """(experimental) the response mapping template for the AppSync Function.

        :default: - no response mapping template

        :stability: experimental
        """
        result = self._values.get("response_mapping_template")
        return result

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) the GraphQL Api linked to this AppSync Function.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def data_source(self) -> BaseDataSource:
        """(experimental) the data source linked to this AppSync Function.

        :stability: experimental
        """
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IGrantable_4c5a91d1)
class BackedDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_appsync.BackedDataSource",
):
    """(experimental) Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for resource backed datasources

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _BackedDataSourceProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        props: "BackedDataSourceProps",
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[CfnDataSource.DynamoDBConfigProperty, _IResolvable_a771d0ef]] = None,
        elasticsearch_config: typing.Optional[typing.Union[CfnDataSource.ElasticsearchConfigProperty, _IResolvable_a771d0ef]] = None,
        http_config: typing.Optional[typing.Union[CfnDataSource.HttpConfigProperty, _IResolvable_a771d0ef]] = None,
        lambda_config: typing.Optional[typing.Union[CfnDataSource.LambdaConfigProperty, _IResolvable_a771d0ef]] = None,
        relational_database_config: typing.Optional[typing.Union[CfnDataSource.RelationalDatabaseConfigProperty, _IResolvable_a771d0ef]] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param type: (experimental) the type of the AppSync datasource.
        :param dynamo_db_config: (experimental) configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (experimental) configuration for Elasticsearch Datasource. Default: - No config
        :param http_config: (experimental) configuration for HTTP Datasource. Default: - No config
        :param lambda_config: (experimental) configuration for Lambda Datasource. Default: - No config
        :param relational_database_config: (experimental) configuration for RDS Datasource. Default: - No config

        :stability: experimental
        """
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(BackedDataSource, self, [scope, id, props, extended])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_93b48231:
        """(experimental) the principal of the data source to be IGrantable.

        :stability: experimental
        """
        return jsii.get(self, "grantPrincipal")


class _BackedDataSourceProxy(
    BackedDataSource, jsii.proxy_for(BaseDataSource) # type: ignore
):
    pass


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.BackedDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
    },
)
class BackedDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        """(experimental) properties for an AppSync datasource backed by a resource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        """
        result = self._values.get("service_role")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamoDbDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.DynamoDbDataSource",
):
    """(experimental) An AppSync datasource backed by a DynamoDB table.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        table: _ITable_24826f7e,
        read_only_access: typing.Optional[builtins.bool] = None,
        use_caller_credentials: typing.Optional[builtins.bool] = None,
        service_role: typing.Optional[_IRole_59af6f50] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param table: (experimental) The DynamoDB table backing this data source.
        :param read_only_access: (experimental) Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: (experimental) use credentials of caller to access DynamoDB. Default: false
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        props = DynamoDbDataSourceProps(
            table=table,
            read_only_access=read_only_access,
            use_caller_credentials=use_caller_credentials,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(DynamoDbDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.DynamoDbDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "table": "table",
        "read_only_access": "readOnlyAccess",
        "use_caller_credentials": "useCallerCredentials",
    },
)
class DynamoDbDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_59af6f50] = None,
        table: _ITable_24826f7e,
        read_only_access: typing.Optional[builtins.bool] = None,
        use_caller_credentials: typing.Optional[builtins.bool] = None,
    ) -> None:
        """(experimental) Properties for an AppSync DynamoDB datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param table: (experimental) The DynamoDB table backing this data source.
        :param read_only_access: (experimental) Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: (experimental) use credentials of caller to access DynamoDB. Default: false

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
            "table": table,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role
        if read_only_access is not None:
            self._values["read_only_access"] = read_only_access
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        """
        result = self._values.get("service_role")
        return result

    @builtins.property
    def table(self) -> _ITable_24826f7e:
        """(experimental) The DynamoDB table backing this data source.

        :stability: experimental
        """
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return result

    @builtins.property
    def read_only_access(self) -> typing.Optional[builtins.bool]:
        """(experimental) Specify whether this DS is read only or has read and write permissions to the DynamoDB table.

        :default: false

        :stability: experimental
        """
        result = self._values.get("read_only_access")
        return result

    @builtins.property
    def use_caller_credentials(self) -> typing.Optional[builtins.bool]:
        """(experimental) use credentials of caller to access DynamoDB.

        :default: false

        :stability: experimental
        """
        result = self._values.get("use_caller_credentials")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDbDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IIntermediateType)
class EnumType(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.EnumType"):
    """(experimental) Enum Types are abstract types that includes a set of fields that represent the strings this type can create.

    :stability: experimental
    """

    def __init__(
        self,
        name: builtins.str,
        *,
        definition: typing.List[builtins.str],
    ) -> None:
        """
        :param name: -
        :param definition: (experimental) the attributes of this type.

        :stability: experimental
        """
        options = EnumTypeOptions(definition=definition)

        jsii.create(EnumType, self, [name, options])

    @jsii.member(jsii_name="addField")
    def add_field(
        self,
        *,
        field: typing.Optional[IField] = None,
        field_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Add a field to this Enum Type.

        To add a field to this Enum Type, you must only configure
        addField with the fieldName options.

        :param field: (experimental) The resolvable field to add. This option must be configured for Object, Interface, Input and Union Types. Default: - no IField
        :param field_name: (experimental) The name of the field. This option must be configured for Object, Interface, Input and Enum Types. Default: - no fieldName

        :stability: experimental
        """
        options = AddFieldOptions(field=field, field_name=field_name)

        return jsii.invoke(self, "addField", [options])

    @jsii.member(jsii_name="attribute")
    def attribute(
        self,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) Create an GraphQL Type representing this Enum Type.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.invoke(self, "attribute", [options])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string of this enum type.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Mapping[builtins.str, IField]:
        """(experimental) the attributes of this type.

        :stability: experimental
        """
        return jsii.get(self, "definition")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of this type.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modes")
    def _modes(self) -> typing.Optional[typing.List[AuthorizationType]]:
        """(experimental) the authorization modes for this intermediate type.

        :stability: experimental
        """
        return jsii.get(self, "modes")

    @_modes.setter # type: ignore
    def _modes(self, value: typing.Optional[typing.List[AuthorizationType]]) -> None:
        jsii.set(self, "modes", value)


@jsii.implements(IGraphqlApi)
class GraphqlApiBase(
    _Resource_abff4495,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="monocdk.aws_appsync.GraphqlApiBase",
):
    """(experimental) Base Class for GraphQL API.

    :stability: experimental
    """

    @builtins.staticmethod
    def __jsii_proxy_class__():
        return _GraphqlApiBaseProxy

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param account: (experimental) The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param physical_name: (experimental) The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: (experimental) The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to

        :stability: experimental
        """
        props = _ResourceProps_9b554c0f(
            account=account, physical_name=physical_name, region=region
        )

        jsii.create(GraphqlApiBase, self, [scope, id, props])

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _ITable_24826f7e,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> DynamoDbDataSource:
        """(experimental) add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addDynamoDbDataSource", [id, table, options])

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[AwsIamConfig] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        """(experimental) add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = HttpDataSourceOptions(
            authorization_config=authorization_config,
            description=description,
            name=name,
        )

        return jsii.invoke(self, "addHttpDataSource", [id, endpoint, options])

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _IFunction_6e14f09e,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        """(experimental) add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addLambdaDataSource", [id, lambda_function, options])

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> NoneDataSource:
        """(experimental) add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addNoneDataSource", [id, options])

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        database_cluster: _IDatabaseCluster_2d93b7f0,
        secret_store: _ISecret_22fb8757,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        """(experimental) add a new Rds data source to this API.

        :param id: The data source's id.
        :param database_cluster: The database cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the database cluster.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        """
        options = DataSourceOptions(description=description, name=name)

        return jsii.invoke(self, "addRdsDataSource", [id, database_cluster, secret_store, options])

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_e0a482dc) -> builtins.bool:
        """(experimental) Add schema dependency if not imported.

        :param construct: the dependee.

        :stability: experimental
        """
        return jsii.invoke(self, "addSchemaDependency", [construct])

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> Resolver:
        """(experimental) creates a new resolver for this datasource and API using the given properties.

        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        """
        props = ExtendedResolverProps(
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return jsii.invoke(self, "createResolver", [props])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    @abc.abstractmethod
    def api_id(self) -> builtins.str:
        """(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        """
        ...

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    @abc.abstractmethod
    def arn(self) -> builtins.str:
        """(experimental) the ARN of the API.

        :stability: experimental
        """
        ...


class _GraphqlApiBaseProxy(
    GraphqlApiBase, jsii.proxy_for(_Resource_abff4495) # type: ignore
):
    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        """
        return jsii.get(self, "apiId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        """(experimental) the ARN of the API.

        :stability: experimental
        """
        return jsii.get(self, "arn")


@jsii.implements(IField)
class GraphqlType(metaclass=jsii.JSIIMeta, jsii_type="monocdk.aws_appsync.GraphqlType"):
    """(experimental) The GraphQL Types in AppSync's GraphQL.

    GraphQL Types are the
    building blocks for object types, queries, mutations, etc. They are
    types like String, Int, Id or even Object Types you create.

    i.e. ``String``, ``String!``, ``[String]``, ``[String!]``, ``[String]!``

    GraphQL Types are used to define the entirety of schema.

    :stability: experimental
    """

    def __init__(
        self,
        type: Type,
        *,
        intermediate_type: typing.Optional[IIntermediateType] = None,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param type: -
        :param intermediate_type: (experimental) the intermediate type linked to this attribute. Default: - no intermediate type
        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = GraphqlTypeOptions(
            intermediate_type=intermediate_type,
            is_list=is_list,
            is_required=is_required,
            is_required_list=is_required_list,
        )

        jsii.create(GraphqlType, self, [type, options])

    @jsii.member(jsii_name="awsDate")
    @builtins.classmethod
    def aws_date(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSDate`` scalar type represents a valid extended ``ISO 8601 Date`` string.

        In other words, accepts date strings in the form of ``YYYY-MM-DD``. It accepts time zone offsets.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsDate", [options])

    @jsii.member(jsii_name="awsDateTime")
    @builtins.classmethod
    def aws_date_time(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSDateTime`` scalar type represents a valid extended ``ISO 8601 DateTime`` string.

        In other words, accepts date strings in the form of ``YYYY-MM-DDThh:mm:ss.sssZ``. It accepts time zone offsets.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsDateTime", [options])

    @jsii.member(jsii_name="awsEmail")
    @builtins.classmethod
    def aws_email(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSEmail`` scalar type represents an email address string (i.e.``username@example.com``).

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsEmail", [options])

    @jsii.member(jsii_name="awsIpAddress")
    @builtins.classmethod
    def aws_ip_address(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSIPAddress`` scalar type respresents a valid ``IPv4`` of ``IPv6`` address string.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsIpAddress", [options])

    @jsii.member(jsii_name="awsJson")
    @builtins.classmethod
    def aws_json(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSJson`` scalar type represents a JSON string.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsJson", [options])

    @jsii.member(jsii_name="awsPhone")
    @builtins.classmethod
    def aws_phone(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSPhone`` scalar type represents a valid phone number. Phone numbers maybe be whitespace delimited or hyphenated.

        The number can specify a country code at the beginning, but is not required for US phone numbers.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsPhone", [options])

    @jsii.member(jsii_name="awsTime")
    @builtins.classmethod
    def aws_time(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSTime`` scalar type represents a valid extended ``ISO 8601 Time`` string.

        In other words, accepts date strings in the form of ``hh:mm:ss.sss``. It accepts time zone offsets.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsTime", [options])

    @jsii.member(jsii_name="awsTimestamp")
    @builtins.classmethod
    def aws_timestamp(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSTimestamp`` scalar type represents the number of seconds since ``1970-01-01T00:00Z``.

        Timestamps are serialized and deserialized as numbers.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsTimestamp", [options])

    @jsii.member(jsii_name="awsUrl")
    @builtins.classmethod
    def aws_url(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``AWSURL`` scalar type represetns a valid URL string.

        URLs wihtout schemes or contain double slashes are considered invalid.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "awsUrl", [options])

    @jsii.member(jsii_name="boolean")
    @builtins.classmethod
    def boolean(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``Boolean`` scalar type is a boolean value: true or false.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "boolean", [options])

    @jsii.member(jsii_name="float")
    @builtins.classmethod
    def float(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``Float`` scalar type is a signed double-precision fractional value.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "float", [options])

    @jsii.member(jsii_name="id")
    @builtins.classmethod
    def id(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``ID`` scalar type is a unique identifier. ``ID`` type is serialized similar to ``String``.

        Often used as a key for a cache and not intended to be human-readable.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "id", [options])

    @jsii.member(jsii_name="int")
    @builtins.classmethod
    def int(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``Int`` scalar type is a signed non-fractional numerical value.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "int", [options])

    @jsii.member(jsii_name="intermediate")
    @builtins.classmethod
    def intermediate(
        cls,
        *,
        intermediate_type: typing.Optional[IIntermediateType] = None,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) an intermediate type to be added as an attribute (i.e. an interface or an object type).

        :param intermediate_type: (experimental) the intermediate type linked to this attribute. Default: - no intermediate type
        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = GraphqlTypeOptions(
            intermediate_type=intermediate_type,
            is_list=is_list,
            is_required=is_required,
            is_required_list=is_required_list,
        )

        return jsii.sinvoke(cls, "intermediate", [options])

    @jsii.member(jsii_name="string")
    @builtins.classmethod
    def string(
        cls,
        *,
        is_list: typing.Optional[builtins.bool] = None,
        is_required: typing.Optional[builtins.bool] = None,
        is_required_list: typing.Optional[builtins.bool] = None,
    ) -> "GraphqlType":
        """(experimental) ``String`` scalar type is a free-form human-readable text.

        :param is_list: (experimental) property determining if this attribute is a list i.e. if true, attribute would be [Type]. Default: - false
        :param is_required: (experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be Type! Default: - false
        :param is_required_list: (experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be [ Type ]! or if isRequired true, attribe would be [ Type! ]! Default: - false

        :stability: experimental
        """
        options = BaseTypeOptions(
            is_list=is_list, is_required=is_required, is_required_list=is_required_list
        )

        return jsii.sinvoke(cls, "string", [options])

    @jsii.member(jsii_name="argsToString")
    def args_to_string(self) -> builtins.str:
        """(experimental) Generate the arguments for this field.

        :stability: experimental
        """
        return jsii.invoke(self, "argsToString", [])

    @jsii.member(jsii_name="directivesToString")
    def directives_to_string(
        self,
        _modes: typing.Optional[typing.List[AuthorizationType]] = None,
    ) -> builtins.str:
        """(experimental) Generate the directives for this field.

        :param _modes: -

        :stability: experimental
        """
        return jsii.invoke(self, "directivesToString", [_modes])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        """(experimental) Generate the string for this attribute.

        :stability: experimental
        """
        return jsii.invoke(self, "toString", [])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isList")
    def is_list(self) -> builtins.bool:
        """(experimental) property determining if this attribute is a list i.e. if true, attribute would be ``[Type]``.

        :default: - false

        :stability: experimental
        """
        return jsii.get(self, "isList")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isRequired")
    def is_required(self) -> builtins.bool:
        """(experimental) property determining if this attribute is non-nullable i.e. if true, attribute would be ``Type!`` and this attribute must always have a value.

        :default: - false

        :stability: experimental
        """
        return jsii.get(self, "isRequired")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="isRequiredList")
    def is_required_list(self) -> builtins.bool:
        """(experimental) property determining if this attribute is a non-nullable list i.e. if true, attribute would be ``[ Type ]!`` and this attribute's list must always have a value.

        :default: - false

        :stability: experimental
        """
        return jsii.get(self, "isRequiredList")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="type")
    def type(self) -> Type:
        """(experimental) the type of attribute.

        :stability: experimental
        """
        return jsii.get(self, "type")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="intermediateType")
    def intermediate_type(self) -> typing.Optional[IIntermediateType]:
        """(experimental) the intermediate type linked to this attribute (i.e. an interface or an object).

        :default: - no intermediate type

        :stability: experimental
        """
        return jsii.get(self, "intermediateType")


class HttpDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.HttpDataSource",
):
    """(experimental) An AppSync datasource backed by a http endpoint.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[AwsIamConfig] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param endpoint: (experimental) The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        props = HttpDataSourceProps(
            endpoint=endpoint,
            authorization_config=authorization_config,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(HttpDataSource, self, [scope, id, props])


class LambdaDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.LambdaDataSource",
):
    """(experimental) An AppSync datasource backed by a Lambda function.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        lambda_function: _IFunction_6e14f09e,
        service_role: typing.Optional[_IRole_59af6f50] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param lambda_function: (experimental) The Lambda function to call to interact with this data source.
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        props = LambdaDataSourceProps(
            lambda_function=lambda_function,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(LambdaDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.LambdaDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "lambda_function": "lambdaFunction",
    },
)
class LambdaDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_59af6f50] = None,
        lambda_function: _IFunction_6e14f09e,
    ) -> None:
        """(experimental) Properties for an AppSync Lambda datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param lambda_function: (experimental) The Lambda function to call to interact with this data source.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
            "lambda_function": lambda_function,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        """
        result = self._values.get("service_role")
        return result

    @builtins.property
    def lambda_function(self) -> _IFunction_6e14f09e:
        """(experimental) The Lambda function to call to interact with this data source.

        :stability: experimental
        """
        result = self._values.get("lambda_function")
        assert result is not None, "Required property 'lambda_function' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKey(
    PrimaryKey,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.PartitionKey",
):
    """(experimental) Specifies the assignment to the partition key.

    It can be
    enhanced with the assignment of the sort key.

    :stability: experimental
    """

    def __init__(self, pkey: Assign) -> None:
        """
        :param pkey: -

        :stability: experimental
        """
        jsii.create(PartitionKey, self, [pkey])

    @jsii.member(jsii_name="sort")
    def sort(self, key: builtins.str) -> SortKeyStep:
        """(experimental) Allows assigning a value to the sort key.

        :param key: -

        :stability: experimental
        """
        return jsii.invoke(self, "sort", [key])


class RdsDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.RdsDataSource",
):
    """(experimental) An AppSync datasource backed by RDS.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        database_cluster: _IDatabaseCluster_2d93b7f0,
        secret_store: _ISecret_22fb8757,
        service_role: typing.Optional[_IRole_59af6f50] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param database_cluster: (experimental) The database cluster to call to interact with this data source.
        :param secret_store: (experimental) The secret containing the credentials for the database.
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        """
        props = RdsDataSourceProps(
            database_cluster=database_cluster,
            secret_store=secret_store,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(RdsDataSource, self, [scope, id, props])


@jsii.data_type(
    jsii_type="monocdk.aws_appsync.RdsDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "database_cluster": "databaseCluster",
        "secret_store": "secretStore",
    },
)
class RdsDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_IRole_59af6f50] = None,
        database_cluster: _IDatabaseCluster_2d93b7f0,
        secret_store: _ISecret_22fb8757,
    ) -> None:
        """(experimental) Properties for an AppSync RDS datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param database_cluster: (experimental) The database cluster to call to interact with this data source.
        :param secret_store: (experimental) The secret containing the credentials for the database.

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
            "database_cluster": database_cluster,
            "secret_store": secret_store,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        """(experimental) The API to attach this data source to.

        :stability: experimental
        """
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return result

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        """
        result = self._values.get("description")
        return result

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        """
        result = self._values.get("name")
        return result

    @builtins.property
    def service_role(self) -> typing.Optional[_IRole_59af6f50]:
        """(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        """
        result = self._values.get("service_role")
        return result

    @builtins.property
    def database_cluster(self) -> _IDatabaseCluster_2d93b7f0:
        """(experimental) The database cluster to call to interact with this data source.

        :stability: experimental
        """
        result = self._values.get("database_cluster")
        assert result is not None, "Required property 'database_cluster' is missing"
        return result

    @builtins.property
    def secret_store(self) -> _ISecret_22fb8757:
        """(experimental) The secret containing the credentials for the database.

        :stability: experimental
        """
        result = self._values.get("secret_store")
        assert result is not None, "Required property 'secret_store' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IField)
class Field(
    GraphqlType,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.Field",
):
    """(experimental) Fields build upon Graphql Types and provide typing and arguments.

    :stability: experimental
    """

    def __init__(
        self,
        *,
        return_type: GraphqlType,
        args: typing.Optional[typing.Mapping[builtins.str, GraphqlType]] = None,
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """
        :param return_type: (experimental) The return type for this field.
        :param args: (experimental) The arguments for this field. i.e. type Example (first: String second: String) {} - where 'first' and 'second' are key values for args and 'String' is the GraphqlType Default: - no arguments
        :param directives: (experimental) the directives for this field. Default: - no directives

        :stability: experimental
        """
        options = FieldOptions(
            return_type=return_type, args=args, directives=directives
        )

        jsii.create(Field, self, [options])

    @jsii.member(jsii_name="argsToString")
    def args_to_string(self) -> builtins.str:
        """(experimental) Generate the args string of this resolvable field.

        :stability: experimental
        """
        return jsii.invoke(self, "argsToString", [])

    @jsii.member(jsii_name="directivesToString")
    def directives_to_string(
        self,
        modes: typing.Optional[typing.List[AuthorizationType]] = None,
    ) -> builtins.str:
        """(experimental) Generate the directives for this field.

        :param modes: -

        :stability: experimental
        """
        return jsii.invoke(self, "directivesToString", [modes])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="fieldOptions")
    def field_options(self) -> typing.Optional[ResolvableFieldOptions]:
        """(experimental) The options for this field.

        :default: - no arguments

        :stability: experimental
        """
        return jsii.get(self, "fieldOptions")


class GraphqlApi(
    GraphqlApiBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.GraphqlApi",
):
    """(experimental) An AppSync GraphQL API.

    :stability: experimental
    :resource: AWS::AppSync::GraphQLApi
    """

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        authorization_config: typing.Optional[AuthorizationConfig] = None,
        log_config: typing.Optional[LogConfig] = None,
        schema: typing.Optional[Schema] = None,
        xray_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        """
        :param scope: -
        :param id: -
        :param name: (experimental) the name of the GraphQL API.
        :param authorization_config: (experimental) Optional authorization configuration. Default: - API Key authorization
        :param log_config: (experimental) Logging configuration for this api. Default: - None
        :param schema: (experimental) GraphQL schema definition. Specify how you want to define your schema. Schema.fromFile(filePath: string) allows schema definition through schema.graphql file Default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        :param xray_enabled: (experimental) A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        :stability: experimental
        """
        props = GraphqlApiProps(
            name=name,
            authorization_config=authorization_config,
            log_config=log_config,
            schema=schema,
            xray_enabled=xray_enabled,
        )

        jsii.create(GraphqlApi, self, [scope, id, props])

    @jsii.member(jsii_name="fromGraphqlApiAttributes")
    @builtins.classmethod
    def from_graphql_api_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        graphql_api_id: builtins.str,
        graphql_api_arn: typing.Optional[builtins.str] = None,
    ) -> IGraphqlApi:
        """(experimental) Import a GraphQL API through this function.

        :param scope: scope.
        :param id: id.
        :param graphql_api_id: (experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.
        :param graphql_api_arn: (experimental) the arn for the GraphQL Api. Default: - autogenerated arn

        :stability: experimental
        """
        attrs = GraphqlApiAttributes(
            graphql_api_id=graphql_api_id, graphql_api_arn=graphql_api_arn
        )

        return jsii.sinvoke(cls, "fromGraphqlApiAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addMutation")
    def add_mutation(
        self,
        field_name: builtins.str,
        field: "ResolvableField",
    ) -> ObjectType:
        """(experimental) Add a mutation field to the schema's Mutation. CDK will create an Object Type called 'Mutation'. For example,.

        type Mutation {
        fieldName: Field.returnType
        }

        :param field_name: the name of the Mutation.
        :param field: the resolvable field to for this Mutation.

        :stability: experimental
        """
        return jsii.invoke(self, "addMutation", [field_name, field])

    @jsii.member(jsii_name="addQuery")
    def add_query(
        self,
        field_name: builtins.str,
        field: "ResolvableField",
    ) -> ObjectType:
        """(experimental) Add a query field to the schema's Query. CDK will create an Object Type called 'Query'. For example,.

        type Query {
        fieldName: Field.returnType
        }

        :param field_name: the name of the query.
        :param field: the resolvable field to for this query.

        :stability: experimental
        """
        return jsii.invoke(self, "addQuery", [field_name, field])

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(self, construct: _CfnResource_e0a482dc) -> builtins.bool:
        """(experimental) Add schema dependency to a given construct.

        :param construct: the dependee.

        :stability: experimental
        """
        return jsii.invoke(self, "addSchemaDependency", [construct])

    @jsii.member(jsii_name="addSubscription")
    def add_subscription(
        self,
        field_name: builtins.str,
        field: "ResolvableField",
    ) -> ObjectType:
        """(experimental) Add a subscription field to the schema's Subscription. CDK will create an Object Type called 'Subscription'. For example,.

        type Subscription {
        fieldName: Field.returnType
        }

        :param field_name: the name of the Subscription.
        :param field: the resolvable field to for this Subscription.

        :stability: experimental
        """
        return jsii.invoke(self, "addSubscription", [field_name, field])

    @jsii.member(jsii_name="addToSchema")
    def add_to_schema(
        self,
        addition: builtins.str,
        delimiter: typing.Optional[builtins.str] = None,
    ) -> None:
        """(experimental) Escape hatch to append to Schema as desired.

        Will always result
        in a newline.

        :param addition: the addition to add to schema.
        :param delimiter: the delimiter between schema and addition.

        :default: - ''

        :stability: experimental
        """
        return jsii.invoke(self, "addToSchema", [addition, delimiter])

    @jsii.member(jsii_name="addType")
    def add_type(self, type: IIntermediateType) -> IIntermediateType:
        """(experimental) Add type to the schema.

        :param type: the intermediate type to add to the schema.

        :stability: experimental
        """
        return jsii.invoke(self, "addType", [type])

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_4c5a91d1,
        resources: IamResource,
        *actions: builtins.str,
    ) -> _Grant_bcb5eae7:
        """(experimental) Adds an IAM policy statement associated with this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param resources: The set of resources to allow (i.e. ...:[region]:[accountId]:apis/GraphQLId/...).
        :param actions: The actions that should be granted to the principal (i.e. appsync:graphql ).

        :stability: experimental
        """
        return jsii.invoke(self, "grant", [grantee, resources, *actions])

    @jsii.member(jsii_name="grantMutation")
    def grant_mutation(
        self,
        grantee: _IGrantable_4c5a91d1,
        *fields: builtins.str,
    ) -> _Grant_bcb5eae7:
        """(experimental) Adds an IAM policy statement for Mutation access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Mutations (leave blank for all).

        :stability: experimental
        """
        return jsii.invoke(self, "grantMutation", [grantee, *fields])

    @jsii.member(jsii_name="grantQuery")
    def grant_query(
        self,
        grantee: _IGrantable_4c5a91d1,
        *fields: builtins.str,
    ) -> _Grant_bcb5eae7:
        """(experimental) Adds an IAM policy statement for Query access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Queries (leave blank for all).

        :stability: experimental
        """
        return jsii.invoke(self, "grantQuery", [grantee, *fields])

    @jsii.member(jsii_name="grantSubscription")
    def grant_subscription(
        self,
        grantee: _IGrantable_4c5a91d1,
        *fields: builtins.str,
    ) -> _Grant_bcb5eae7:
        """(experimental) Adds an IAM policy statement for Subscription access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Subscriptions (leave blank for all).

        :stability: experimental
        """
        return jsii.invoke(self, "grantSubscription", [grantee, *fields])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        """(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        """
        return jsii.get(self, "apiId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        """(experimental) the ARN of the API.

        :stability: experimental
        """
        return jsii.get(self, "arn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="graphqlUrl")
    def graphql_url(self) -> builtins.str:
        """(experimental) the URL of the endpoint created by AppSync.

        :stability: experimental
        :attribute: GraphQlUrl
        """
        return jsii.get(self, "graphqlUrl")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="modes")
    def modes(self) -> typing.List[AuthorizationType]:
        """(experimental) The Authorization Types for this GraphQL Api.

        :stability: experimental
        """
        return jsii.get(self, "modes")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """(experimental) the name of the API.

        :stability: experimental
        """
        return jsii.get(self, "name")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="schema")
    def schema(self) -> Schema:
        """(experimental) the schema attached to this api.

        :stability: experimental
        """
        return jsii.get(self, "schema")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        """(experimental) the configured API key, if present.

        :default: - no api key

        :stability: experimental
        """
        return jsii.get(self, "apiKey")


@jsii.implements(IField)
class ResolvableField(
    Field,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_appsync.ResolvableField",
):
    """(experimental) Resolvable Fields build upon Graphql Types and provide fields that can resolve into operations on a data source.

    :stability: experimental
    """

    def __init__(
        self,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        pipeline_config: typing.Optional[typing.List[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        return_type: GraphqlType,
        args: typing.Optional[typing.Mapping[builtins.str, GraphqlType]] = None,
        directives: typing.Optional[typing.List[Directive]] = None,
    ) -> None:
        """
        :param data_source: (experimental) The data source creating linked to this resolvable field. Default: - no data source
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array or undefined prop will set resolver to be of type unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template
        :param return_type: (experimental) The return type for this field.
        :param args: (experimental) The arguments for this field. i.e. type Example (first: String second: String) {} - where 'first' and 'second' are key values for args and 'String' is the GraphqlType Default: - no arguments
        :param directives: (experimental) the directives for this field. Default: - no directives

        :stability: experimental
        """
        options = ResolvableFieldOptions(
            data_source=data_source,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
            return_type=return_type,
            args=args,
            directives=directives,
        )

        jsii.create(ResolvableField, self, [options])

    @builtins.property # type: ignore
    @jsii.member(jsii_name="fieldOptions")
    def field_options(self) -> typing.Optional[ResolvableFieldOptions]:
        """(experimental) The options to make this field resolvable.

        :default: - not a resolvable field

        :stability: experimental
        """
        return jsii.get(self, "fieldOptions")


__all__ = [
    "AddFieldOptions",
    "ApiKeyConfig",
    "AppsyncFunction",
    "AppsyncFunctionAttributes",
    "AppsyncFunctionProps",
    "Assign",
    "AttributeValues",
    "AttributeValuesStep",
    "AuthorizationConfig",
    "AuthorizationMode",
    "AuthorizationType",
    "AwsIamConfig",
    "BackedDataSource",
    "BackedDataSourceProps",
    "BaseAppsyncFunctionProps",
    "BaseDataSource",
    "BaseDataSourceProps",
    "BaseResolverProps",
    "BaseTypeOptions",
    "CfnApiCache",
    "CfnApiCacheProps",
    "CfnApiKey",
    "CfnApiKeyProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnFunctionConfiguration",
    "CfnFunctionConfigurationProps",
    "CfnGraphQLApi",
    "CfnGraphQLApiProps",
    "CfnGraphQLSchema",
    "CfnGraphQLSchemaProps",
    "CfnResolver",
    "CfnResolverProps",
    "DataSourceOptions",
    "Directive",
    "DynamoDbDataSource",
    "DynamoDbDataSourceProps",
    "EnumType",
    "EnumTypeOptions",
    "ExtendedDataSourceProps",
    "ExtendedResolverProps",
    "Field",
    "FieldLogLevel",
    "FieldOptions",
    "GraphqlApi",
    "GraphqlApiAttributes",
    "GraphqlApiBase",
    "GraphqlApiProps",
    "GraphqlType",
    "GraphqlTypeOptions",
    "HttpDataSource",
    "HttpDataSourceOptions",
    "HttpDataSourceProps",
    "IAppsyncFunction",
    "IField",
    "IGraphqlApi",
    "IIntermediateType",
    "IamResource",
    "InputType",
    "InterfaceType",
    "IntermediateTypeOptions",
    "KeyCondition",
    "LambdaDataSource",
    "LambdaDataSourceProps",
    "LogConfig",
    "MappingTemplate",
    "NoneDataSource",
    "NoneDataSourceProps",
    "ObjectType",
    "ObjectTypeOptions",
    "OpenIdConnectConfig",
    "PartitionKey",
    "PartitionKeyStep",
    "PrimaryKey",
    "RdsDataSource",
    "RdsDataSourceProps",
    "ResolvableField",
    "ResolvableFieldOptions",
    "Resolver",
    "ResolverProps",
    "Schema",
    "SchemaOptions",
    "SortKeyStep",
    "Type",
    "UnionType",
    "UnionTypeOptions",
    "UserPoolConfig",
    "UserPoolDefaultAction",
    "Values",
]

publication.publish()
