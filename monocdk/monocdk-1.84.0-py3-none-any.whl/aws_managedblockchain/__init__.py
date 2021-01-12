import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from .._jsii import *

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnMember(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_managedblockchain.CfnMember",
):
    """A CloudFormation ``AWS::ManagedBlockchain::Member``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html
    :cloudformationResource: AWS::ManagedBlockchain::Member
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        member_configuration: typing.Union["CfnMember.MemberConfigurationProperty", _IResolvable_a771d0ef],
        invitation_id: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["CfnMember.NetworkConfigurationProperty", _IResolvable_a771d0ef]] = None,
        network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new ``AWS::ManagedBlockchain::Member``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param member_configuration: ``AWS::ManagedBlockchain::Member.MemberConfiguration``.
        :param invitation_id: ``AWS::ManagedBlockchain::Member.InvitationId``.
        :param network_configuration: ``AWS::ManagedBlockchain::Member.NetworkConfiguration``.
        :param network_id: ``AWS::ManagedBlockchain::Member.NetworkId``.
        """
        props = CfnMemberProps(
            member_configuration=member_configuration,
            invitation_id=invitation_id,
            network_configuration=network_configuration,
            network_id=network_id,
        )

        jsii.create(CfnMember, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrMemberId")
    def attr_member_id(self) -> builtins.str:
        """
        :cloudformationAttribute: MemberId
        """
        return jsii.get(self, "attrMemberId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrNetworkId")
    def attr_network_id(self) -> builtins.str:
        """
        :cloudformationAttribute: NetworkId
        """
        return jsii.get(self, "attrNetworkId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="memberConfiguration")
    def member_configuration(
        self,
    ) -> typing.Union["CfnMember.MemberConfigurationProperty", _IResolvable_a771d0ef]:
        """``AWS::ManagedBlockchain::Member.MemberConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-memberconfiguration
        """
        return jsii.get(self, "memberConfiguration")

    @member_configuration.setter # type: ignore
    def member_configuration(
        self,
        value: typing.Union["CfnMember.MemberConfigurationProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "memberConfiguration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="invitationId")
    def invitation_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ManagedBlockchain::Member.InvitationId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-invitationid
        """
        return jsii.get(self, "invitationId")

    @invitation_id.setter # type: ignore
    def invitation_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "invitationId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnMember.NetworkConfigurationProperty", _IResolvable_a771d0ef]]:
        """``AWS::ManagedBlockchain::Member.NetworkConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-networkconfiguration
        """
        return jsii.get(self, "networkConfiguration")

    @network_configuration.setter # type: ignore
    def network_configuration(
        self,
        value: typing.Optional[typing.Union["CfnMember.NetworkConfigurationProperty", _IResolvable_a771d0ef]],
    ) -> None:
        jsii.set(self, "networkConfiguration", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ManagedBlockchain::Member.NetworkId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-networkid
        """
        return jsii.get(self, "networkId")

    @network_id.setter # type: ignore
    def network_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "networkId", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.ApprovalThresholdPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "proposal_duration_in_hours": "proposalDurationInHours",
            "threshold_comparator": "thresholdComparator",
            "threshold_percentage": "thresholdPercentage",
        },
    )
    class ApprovalThresholdPolicyProperty:
        def __init__(
            self,
            *,
            proposal_duration_in_hours: typing.Optional[jsii.Number] = None,
            threshold_comparator: typing.Optional[builtins.str] = None,
            threshold_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            """
            :param proposal_duration_in_hours: ``CfnMember.ApprovalThresholdPolicyProperty.ProposalDurationInHours``.
            :param threshold_comparator: ``CfnMember.ApprovalThresholdPolicyProperty.ThresholdComparator``.
            :param threshold_percentage: ``CfnMember.ApprovalThresholdPolicyProperty.ThresholdPercentage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if proposal_duration_in_hours is not None:
                self._values["proposal_duration_in_hours"] = proposal_duration_in_hours
            if threshold_comparator is not None:
                self._values["threshold_comparator"] = threshold_comparator
            if threshold_percentage is not None:
                self._values["threshold_percentage"] = threshold_percentage

        @builtins.property
        def proposal_duration_in_hours(self) -> typing.Optional[jsii.Number]:
            """``CfnMember.ApprovalThresholdPolicyProperty.ProposalDurationInHours``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html#cfn-managedblockchain-member-approvalthresholdpolicy-proposaldurationinhours
            """
            result = self._values.get("proposal_duration_in_hours")
            return result

        @builtins.property
        def threshold_comparator(self) -> typing.Optional[builtins.str]:
            """``CfnMember.ApprovalThresholdPolicyProperty.ThresholdComparator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html#cfn-managedblockchain-member-approvalthresholdpolicy-thresholdcomparator
            """
            result = self._values.get("threshold_comparator")
            return result

        @builtins.property
        def threshold_percentage(self) -> typing.Optional[jsii.Number]:
            """``CfnMember.ApprovalThresholdPolicyProperty.ThresholdPercentage``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-approvalthresholdpolicy.html#cfn-managedblockchain-member-approvalthresholdpolicy-thresholdpercentage
            """
            result = self._values.get("threshold_percentage")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApprovalThresholdPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.MemberConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "description": "description",
            "member_framework_configuration": "memberFrameworkConfiguration",
        },
    )
    class MemberConfigurationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            member_framework_configuration: typing.Optional[typing.Union["CfnMember.MemberFrameworkConfigurationProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param name: ``CfnMember.MemberConfigurationProperty.Name``.
            :param description: ``CfnMember.MemberConfigurationProperty.Description``.
            :param member_framework_configuration: ``CfnMember.MemberConfigurationProperty.MemberFrameworkConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if description is not None:
                self._values["description"] = description
            if member_framework_configuration is not None:
                self._values["member_framework_configuration"] = member_framework_configuration

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnMember.MemberConfigurationProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html#cfn-managedblockchain-member-memberconfiguration-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnMember.MemberConfigurationProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html#cfn-managedblockchain-member-memberconfiguration-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def member_framework_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnMember.MemberFrameworkConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnMember.MemberConfigurationProperty.MemberFrameworkConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberconfiguration.html#cfn-managedblockchain-member-memberconfiguration-memberframeworkconfiguration
            """
            result = self._values.get("member_framework_configuration")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.MemberFabricConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "admin_password": "adminPassword",
            "admin_username": "adminUsername",
        },
    )
    class MemberFabricConfigurationProperty:
        def __init__(
            self,
            *,
            admin_password: builtins.str,
            admin_username: builtins.str,
        ) -> None:
            """
            :param admin_password: ``CfnMember.MemberFabricConfigurationProperty.AdminPassword``.
            :param admin_username: ``CfnMember.MemberFabricConfigurationProperty.AdminUsername``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "admin_password": admin_password,
                "admin_username": admin_username,
            }

        @builtins.property
        def admin_password(self) -> builtins.str:
            """``CfnMember.MemberFabricConfigurationProperty.AdminPassword``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html#cfn-managedblockchain-member-memberfabricconfiguration-adminpassword
            """
            result = self._values.get("admin_password")
            assert result is not None, "Required property 'admin_password' is missing"
            return result

        @builtins.property
        def admin_username(self) -> builtins.str:
            """``CfnMember.MemberFabricConfigurationProperty.AdminUsername``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberfabricconfiguration.html#cfn-managedblockchain-member-memberfabricconfiguration-adminusername
            """
            result = self._values.get("admin_username")
            assert result is not None, "Required property 'admin_username' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberFabricConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.MemberFrameworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"member_fabric_configuration": "memberFabricConfiguration"},
    )
    class MemberFrameworkConfigurationProperty:
        def __init__(
            self,
            *,
            member_fabric_configuration: typing.Optional[typing.Union["CfnMember.MemberFabricConfigurationProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param member_fabric_configuration: ``CfnMember.MemberFrameworkConfigurationProperty.MemberFabricConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if member_fabric_configuration is not None:
                self._values["member_fabric_configuration"] = member_fabric_configuration

        @builtins.property
        def member_fabric_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnMember.MemberFabricConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnMember.MemberFrameworkConfigurationProperty.MemberFabricConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-memberframeworkconfiguration.html#cfn-managedblockchain-member-memberframeworkconfiguration-memberfabricconfiguration
            """
            result = self._values.get("member_fabric_configuration")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberFrameworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "framework": "framework",
            "framework_version": "frameworkVersion",
            "name": "name",
            "voting_policy": "votingPolicy",
            "description": "description",
            "network_framework_configuration": "networkFrameworkConfiguration",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            framework: builtins.str,
            framework_version: builtins.str,
            name: builtins.str,
            voting_policy: typing.Union["CfnMember.VotingPolicyProperty", _IResolvable_a771d0ef],
            description: typing.Optional[builtins.str] = None,
            network_framework_configuration: typing.Optional[typing.Union["CfnMember.NetworkFrameworkConfigurationProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param framework: ``CfnMember.NetworkConfigurationProperty.Framework``.
            :param framework_version: ``CfnMember.NetworkConfigurationProperty.FrameworkVersion``.
            :param name: ``CfnMember.NetworkConfigurationProperty.Name``.
            :param voting_policy: ``CfnMember.NetworkConfigurationProperty.VotingPolicy``.
            :param description: ``CfnMember.NetworkConfigurationProperty.Description``.
            :param network_framework_configuration: ``CfnMember.NetworkConfigurationProperty.NetworkFrameworkConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "framework": framework,
                "framework_version": framework_version,
                "name": name,
                "voting_policy": voting_policy,
            }
            if description is not None:
                self._values["description"] = description
            if network_framework_configuration is not None:
                self._values["network_framework_configuration"] = network_framework_configuration

        @builtins.property
        def framework(self) -> builtins.str:
            """``CfnMember.NetworkConfigurationProperty.Framework``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-framework
            """
            result = self._values.get("framework")
            assert result is not None, "Required property 'framework' is missing"
            return result

        @builtins.property
        def framework_version(self) -> builtins.str:
            """``CfnMember.NetworkConfigurationProperty.FrameworkVersion``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-frameworkversion
            """
            result = self._values.get("framework_version")
            assert result is not None, "Required property 'framework_version' is missing"
            return result

        @builtins.property
        def name(self) -> builtins.str:
            """``CfnMember.NetworkConfigurationProperty.Name``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-name
            """
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return result

        @builtins.property
        def voting_policy(
            self,
        ) -> typing.Union["CfnMember.VotingPolicyProperty", _IResolvable_a771d0ef]:
            """``CfnMember.NetworkConfigurationProperty.VotingPolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-votingpolicy
            """
            result = self._values.get("voting_policy")
            assert result is not None, "Required property 'voting_policy' is missing"
            return result

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            """``CfnMember.NetworkConfigurationProperty.Description``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-description
            """
            result = self._values.get("description")
            return result

        @builtins.property
        def network_framework_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnMember.NetworkFrameworkConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnMember.NetworkConfigurationProperty.NetworkFrameworkConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkconfiguration.html#cfn-managedblockchain-member-networkconfiguration-networkframeworkconfiguration
            """
            result = self._values.get("network_framework_configuration")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.NetworkFabricConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"edition": "edition"},
    )
    class NetworkFabricConfigurationProperty:
        def __init__(self, *, edition: builtins.str) -> None:
            """
            :param edition: ``CfnMember.NetworkFabricConfigurationProperty.Edition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "edition": edition,
            }

        @builtins.property
        def edition(self) -> builtins.str:
            """``CfnMember.NetworkFabricConfigurationProperty.Edition``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkfabricconfiguration.html#cfn-managedblockchain-member-networkfabricconfiguration-edition
            """
            result = self._values.get("edition")
            assert result is not None, "Required property 'edition' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkFabricConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.NetworkFrameworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_fabric_configuration": "networkFabricConfiguration"},
    )
    class NetworkFrameworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_fabric_configuration: typing.Optional[typing.Union["CfnMember.NetworkFabricConfigurationProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param network_fabric_configuration: ``CfnMember.NetworkFrameworkConfigurationProperty.NetworkFabricConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if network_fabric_configuration is not None:
                self._values["network_fabric_configuration"] = network_fabric_configuration

        @builtins.property
        def network_fabric_configuration(
            self,
        ) -> typing.Optional[typing.Union["CfnMember.NetworkFabricConfigurationProperty", _IResolvable_a771d0ef]]:
            """``CfnMember.NetworkFrameworkConfigurationProperty.NetworkFabricConfiguration``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-networkframeworkconfiguration.html#cfn-managedblockchain-member-networkframeworkconfiguration-networkfabricconfiguration
            """
            result = self._values.get("network_fabric_configuration")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkFrameworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnMember.VotingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"approval_threshold_policy": "approvalThresholdPolicy"},
    )
    class VotingPolicyProperty:
        def __init__(
            self,
            *,
            approval_threshold_policy: typing.Optional[typing.Union["CfnMember.ApprovalThresholdPolicyProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param approval_threshold_policy: ``CfnMember.VotingPolicyProperty.ApprovalThresholdPolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if approval_threshold_policy is not None:
                self._values["approval_threshold_policy"] = approval_threshold_policy

        @builtins.property
        def approval_threshold_policy(
            self,
        ) -> typing.Optional[typing.Union["CfnMember.ApprovalThresholdPolicyProperty", _IResolvable_a771d0ef]]:
            """``CfnMember.VotingPolicyProperty.ApprovalThresholdPolicy``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-member-votingpolicy.html#cfn-managedblockchain-member-votingpolicy-approvalthresholdpolicy
            """
            result = self._values.get("approval_threshold_policy")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VotingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_managedblockchain.CfnMemberProps",
    jsii_struct_bases=[],
    name_mapping={
        "member_configuration": "memberConfiguration",
        "invitation_id": "invitationId",
        "network_configuration": "networkConfiguration",
        "network_id": "networkId",
    },
)
class CfnMemberProps:
    def __init__(
        self,
        *,
        member_configuration: typing.Union[CfnMember.MemberConfigurationProperty, _IResolvable_a771d0ef],
        invitation_id: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union[CfnMember.NetworkConfigurationProperty, _IResolvable_a771d0ef]] = None,
        network_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """Properties for defining a ``AWS::ManagedBlockchain::Member``.

        :param member_configuration: ``AWS::ManagedBlockchain::Member.MemberConfiguration``.
        :param invitation_id: ``AWS::ManagedBlockchain::Member.InvitationId``.
        :param network_configuration: ``AWS::ManagedBlockchain::Member.NetworkConfiguration``.
        :param network_id: ``AWS::ManagedBlockchain::Member.NetworkId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "member_configuration": member_configuration,
        }
        if invitation_id is not None:
            self._values["invitation_id"] = invitation_id
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if network_id is not None:
            self._values["network_id"] = network_id

    @builtins.property
    def member_configuration(
        self,
    ) -> typing.Union[CfnMember.MemberConfigurationProperty, _IResolvable_a771d0ef]:
        """``AWS::ManagedBlockchain::Member.MemberConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-memberconfiguration
        """
        result = self._values.get("member_configuration")
        assert result is not None, "Required property 'member_configuration' is missing"
        return result

    @builtins.property
    def invitation_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ManagedBlockchain::Member.InvitationId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-invitationid
        """
        result = self._values.get("invitation_id")
        return result

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnMember.NetworkConfigurationProperty, _IResolvable_a771d0ef]]:
        """``AWS::ManagedBlockchain::Member.NetworkConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-networkconfiguration
        """
        result = self._values.get("network_configuration")
        return result

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        """``AWS::ManagedBlockchain::Member.NetworkId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html#cfn-managedblockchain-member-networkid
        """
        result = self._values.get("network_id")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_82c04a63)
class CfnNode(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_managedblockchain.CfnNode",
):
    """A CloudFormation ``AWS::ManagedBlockchain::Node``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html
    :cloudformationResource: AWS::ManagedBlockchain::Node
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        member_id: builtins.str,
        network_id: builtins.str,
        node_configuration: typing.Union["CfnNode.NodeConfigurationProperty", _IResolvable_a771d0ef],
    ) -> None:
        """Create a new ``AWS::ManagedBlockchain::Node``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param member_id: ``AWS::ManagedBlockchain::Node.MemberId``.
        :param network_id: ``AWS::ManagedBlockchain::Node.NetworkId``.
        :param node_configuration: ``AWS::ManagedBlockchain::Node.NodeConfiguration``.
        """
        props = CfnNodeProps(
            member_id=member_id,
            network_id=network_id,
            node_configuration=node_configuration,
        )

        jsii.create(CfnNode, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        """
        :cloudformationAttribute: Arn
        """
        return jsii.get(self, "attrArn")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrMemberId")
    def attr_member_id(self) -> builtins.str:
        """
        :cloudformationAttribute: MemberId
        """
        return jsii.get(self, "attrMemberId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrNetworkId")
    def attr_network_id(self) -> builtins.str:
        """
        :cloudformationAttribute: NetworkId
        """
        return jsii.get(self, "attrNetworkId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="attrNodeId")
    def attr_node_id(self) -> builtins.str:
        """
        :cloudformationAttribute: NodeId
        """
        return jsii.get(self, "attrNodeId")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property # type: ignore
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        """``AWS::ManagedBlockchain::Node.MemberId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-memberid
        """
        return jsii.get(self, "memberId")

    @member_id.setter # type: ignore
    def member_id(self, value: builtins.str) -> None:
        jsii.set(self, "memberId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        """``AWS::ManagedBlockchain::Node.NetworkId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-networkid
        """
        return jsii.get(self, "networkId")

    @network_id.setter # type: ignore
    def network_id(self, value: builtins.str) -> None:
        jsii.set(self, "networkId", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="nodeConfiguration")
    def node_configuration(
        self,
    ) -> typing.Union["CfnNode.NodeConfigurationProperty", _IResolvable_a771d0ef]:
        """``AWS::ManagedBlockchain::Node.NodeConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-nodeconfiguration
        """
        return jsii.get(self, "nodeConfiguration")

    @node_configuration.setter # type: ignore
    def node_configuration(
        self,
        value: typing.Union["CfnNode.NodeConfigurationProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "nodeConfiguration", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_managedblockchain.CfnNode.NodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "instance_type": "instanceType",
        },
    )
    class NodeConfigurationProperty:
        def __init__(
            self,
            *,
            availability_zone: builtins.str,
            instance_type: builtins.str,
        ) -> None:
            """
            :param availability_zone: ``CfnNode.NodeConfigurationProperty.AvailabilityZone``.
            :param instance_type: ``CfnNode.NodeConfigurationProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "availability_zone": availability_zone,
                "instance_type": instance_type,
            }

        @builtins.property
        def availability_zone(self) -> builtins.str:
            """``CfnNode.NodeConfigurationProperty.AvailabilityZone``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html#cfn-managedblockchain-node-nodeconfiguration-availabilityzone
            """
            result = self._values.get("availability_zone")
            assert result is not None, "Required property 'availability_zone' is missing"
            return result

        @builtins.property
        def instance_type(self) -> builtins.str:
            """``CfnNode.NodeConfigurationProperty.InstanceType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-managedblockchain-node-nodeconfiguration.html#cfn-managedblockchain-node-nodeconfiguration-instancetype
            """
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_managedblockchain.CfnNodeProps",
    jsii_struct_bases=[],
    name_mapping={
        "member_id": "memberId",
        "network_id": "networkId",
        "node_configuration": "nodeConfiguration",
    },
)
class CfnNodeProps:
    def __init__(
        self,
        *,
        member_id: builtins.str,
        network_id: builtins.str,
        node_configuration: typing.Union[CfnNode.NodeConfigurationProperty, _IResolvable_a771d0ef],
    ) -> None:
        """Properties for defining a ``AWS::ManagedBlockchain::Node``.

        :param member_id: ``AWS::ManagedBlockchain::Node.MemberId``.
        :param network_id: ``AWS::ManagedBlockchain::Node.NetworkId``.
        :param node_configuration: ``AWS::ManagedBlockchain::Node.NodeConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "member_id": member_id,
            "network_id": network_id,
            "node_configuration": node_configuration,
        }

    @builtins.property
    def member_id(self) -> builtins.str:
        """``AWS::ManagedBlockchain::Node.MemberId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-memberid
        """
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return result

    @builtins.property
    def network_id(self) -> builtins.str:
        """``AWS::ManagedBlockchain::Node.NetworkId``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-networkid
        """
        result = self._values.get("network_id")
        assert result is not None, "Required property 'network_id' is missing"
        return result

    @builtins.property
    def node_configuration(
        self,
    ) -> typing.Union[CfnNode.NodeConfigurationProperty, _IResolvable_a771d0ef]:
        """``AWS::ManagedBlockchain::Node.NodeConfiguration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html#cfn-managedblockchain-node-nodeconfiguration
        """
        result = self._values.get("node_configuration")
        assert result is not None, "Required property 'node_configuration' is missing"
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMember",
    "CfnMemberProps",
    "CfnNode",
    "CfnNodeProps",
]

publication.publish()
