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
class CfnBudget(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_budgets.CfnBudget",
):
    """A CloudFormation ``AWS::Budgets::Budget``.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
    :cloudformationResource: AWS::Budgets::Budget
    """

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        budget: typing.Union["CfnBudget.BudgetDataProperty", _IResolvable_a771d0ef],
        notifications_with_subscribers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnBudget.NotificationWithSubscribersProperty", _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Create a new ``AWS::Budgets::Budget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param budget: ``AWS::Budgets::Budget.Budget``.
        :param notifications_with_subscribers: ``AWS::Budgets::Budget.NotificationsWithSubscribers``.
        """
        props = CfnBudgetProps(
            budget=budget,
            notifications_with_subscribers=notifications_with_subscribers,
        )

        jsii.create(CfnBudget, self, [scope, id, props])

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
    @jsii.member(jsii_name="budget")
    def budget(
        self,
    ) -> typing.Union["CfnBudget.BudgetDataProperty", _IResolvable_a771d0ef]:
        """``AWS::Budgets::Budget.Budget``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget
        """
        return jsii.get(self, "budget")

    @budget.setter # type: ignore
    def budget(
        self,
        value: typing.Union["CfnBudget.BudgetDataProperty", _IResolvable_a771d0ef],
    ) -> None:
        jsii.set(self, "budget", value)

    @builtins.property # type: ignore
    @jsii.member(jsii_name="notificationsWithSubscribers")
    def notifications_with_subscribers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnBudget.NotificationWithSubscribersProperty", _IResolvable_a771d0ef]]]]:
        """``AWS::Budgets::Budget.NotificationsWithSubscribers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers
        """
        return jsii.get(self, "notificationsWithSubscribers")

    @notifications_with_subscribers.setter # type: ignore
    def notifications_with_subscribers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnBudget.NotificationWithSubscribersProperty", _IResolvable_a771d0ef]]]],
    ) -> None:
        jsii.set(self, "notificationsWithSubscribers", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.BudgetDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "budget_type": "budgetType",
            "time_unit": "timeUnit",
            "budget_limit": "budgetLimit",
            "budget_name": "budgetName",
            "cost_filters": "costFilters",
            "cost_types": "costTypes",
            "planned_budget_limits": "plannedBudgetLimits",
            "time_period": "timePeriod",
        },
    )
    class BudgetDataProperty:
        def __init__(
            self,
            *,
            budget_type: builtins.str,
            time_unit: builtins.str,
            budget_limit: typing.Optional[typing.Union["CfnBudget.SpendProperty", _IResolvable_a771d0ef]] = None,
            budget_name: typing.Optional[builtins.str] = None,
            cost_filters: typing.Any = None,
            cost_types: typing.Optional[typing.Union["CfnBudget.CostTypesProperty", _IResolvable_a771d0ef]] = None,
            planned_budget_limits: typing.Any = None,
            time_period: typing.Optional[typing.Union["CfnBudget.TimePeriodProperty", _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param budget_type: ``CfnBudget.BudgetDataProperty.BudgetType``.
            :param time_unit: ``CfnBudget.BudgetDataProperty.TimeUnit``.
            :param budget_limit: ``CfnBudget.BudgetDataProperty.BudgetLimit``.
            :param budget_name: ``CfnBudget.BudgetDataProperty.BudgetName``.
            :param cost_filters: ``CfnBudget.BudgetDataProperty.CostFilters``.
            :param cost_types: ``CfnBudget.BudgetDataProperty.CostTypes``.
            :param planned_budget_limits: ``CfnBudget.BudgetDataProperty.PlannedBudgetLimits``.
            :param time_period: ``CfnBudget.BudgetDataProperty.TimePeriod``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "budget_type": budget_type,
                "time_unit": time_unit,
            }
            if budget_limit is not None:
                self._values["budget_limit"] = budget_limit
            if budget_name is not None:
                self._values["budget_name"] = budget_name
            if cost_filters is not None:
                self._values["cost_filters"] = cost_filters
            if cost_types is not None:
                self._values["cost_types"] = cost_types
            if planned_budget_limits is not None:
                self._values["planned_budget_limits"] = planned_budget_limits
            if time_period is not None:
                self._values["time_period"] = time_period

        @builtins.property
        def budget_type(self) -> builtins.str:
            """``CfnBudget.BudgetDataProperty.BudgetType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgettype
            """
            result = self._values.get("budget_type")
            assert result is not None, "Required property 'budget_type' is missing"
            return result

        @builtins.property
        def time_unit(self) -> builtins.str:
            """``CfnBudget.BudgetDataProperty.TimeUnit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeunit
            """
            result = self._values.get("time_unit")
            assert result is not None, "Required property 'time_unit' is missing"
            return result

        @builtins.property
        def budget_limit(
            self,
        ) -> typing.Optional[typing.Union["CfnBudget.SpendProperty", _IResolvable_a771d0ef]]:
            """``CfnBudget.BudgetDataProperty.BudgetLimit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetlimit
            """
            result = self._values.get("budget_limit")
            return result

        @builtins.property
        def budget_name(self) -> typing.Optional[builtins.str]:
            """``CfnBudget.BudgetDataProperty.BudgetName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetname
            """
            result = self._values.get("budget_name")
            return result

        @builtins.property
        def cost_filters(self) -> typing.Any:
            """``CfnBudget.BudgetDataProperty.CostFilters``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costfilters
            """
            result = self._values.get("cost_filters")
            return result

        @builtins.property
        def cost_types(
            self,
        ) -> typing.Optional[typing.Union["CfnBudget.CostTypesProperty", _IResolvable_a771d0ef]]:
            """``CfnBudget.BudgetDataProperty.CostTypes``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costtypes
            """
            result = self._values.get("cost_types")
            return result

        @builtins.property
        def planned_budget_limits(self) -> typing.Any:
            """``CfnBudget.BudgetDataProperty.PlannedBudgetLimits``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-plannedbudgetlimits
            """
            result = self._values.get("planned_budget_limits")
            return result

        @builtins.property
        def time_period(
            self,
        ) -> typing.Optional[typing.Union["CfnBudget.TimePeriodProperty", _IResolvable_a771d0ef]]:
            """``CfnBudget.BudgetDataProperty.TimePeriod``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeperiod
            """
            result = self._values.get("time_period")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BudgetDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.CostTypesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "include_credit": "includeCredit",
            "include_discount": "includeDiscount",
            "include_other_subscription": "includeOtherSubscription",
            "include_recurring": "includeRecurring",
            "include_refund": "includeRefund",
            "include_subscription": "includeSubscription",
            "include_support": "includeSupport",
            "include_tax": "includeTax",
            "include_upfront": "includeUpfront",
            "use_amortized": "useAmortized",
            "use_blended": "useBlended",
        },
    )
    class CostTypesProperty:
        def __init__(
            self,
            *,
            include_credit: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_discount: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_other_subscription: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_recurring: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_refund: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_subscription: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_tax: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            include_upfront: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_amortized: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
            use_blended: typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]] = None,
        ) -> None:
            """
            :param include_credit: ``CfnBudget.CostTypesProperty.IncludeCredit``.
            :param include_discount: ``CfnBudget.CostTypesProperty.IncludeDiscount``.
            :param include_other_subscription: ``CfnBudget.CostTypesProperty.IncludeOtherSubscription``.
            :param include_recurring: ``CfnBudget.CostTypesProperty.IncludeRecurring``.
            :param include_refund: ``CfnBudget.CostTypesProperty.IncludeRefund``.
            :param include_subscription: ``CfnBudget.CostTypesProperty.IncludeSubscription``.
            :param include_support: ``CfnBudget.CostTypesProperty.IncludeSupport``.
            :param include_tax: ``CfnBudget.CostTypesProperty.IncludeTax``.
            :param include_upfront: ``CfnBudget.CostTypesProperty.IncludeUpfront``.
            :param use_amortized: ``CfnBudget.CostTypesProperty.UseAmortized``.
            :param use_blended: ``CfnBudget.CostTypesProperty.UseBlended``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if include_credit is not None:
                self._values["include_credit"] = include_credit
            if include_discount is not None:
                self._values["include_discount"] = include_discount
            if include_other_subscription is not None:
                self._values["include_other_subscription"] = include_other_subscription
            if include_recurring is not None:
                self._values["include_recurring"] = include_recurring
            if include_refund is not None:
                self._values["include_refund"] = include_refund
            if include_subscription is not None:
                self._values["include_subscription"] = include_subscription
            if include_support is not None:
                self._values["include_support"] = include_support
            if include_tax is not None:
                self._values["include_tax"] = include_tax
            if include_upfront is not None:
                self._values["include_upfront"] = include_upfront
            if use_amortized is not None:
                self._values["use_amortized"] = use_amortized
            if use_blended is not None:
                self._values["use_blended"] = use_blended

        @builtins.property
        def include_credit(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeCredit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includecredit
            """
            result = self._values.get("include_credit")
            return result

        @builtins.property
        def include_discount(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeDiscount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includediscount
            """
            result = self._values.get("include_discount")
            return result

        @builtins.property
        def include_other_subscription(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeOtherSubscription``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeothersubscription
            """
            result = self._values.get("include_other_subscription")
            return result

        @builtins.property
        def include_recurring(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeRecurring``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerecurring
            """
            result = self._values.get("include_recurring")
            return result

        @builtins.property
        def include_refund(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeRefund``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerefund
            """
            result = self._values.get("include_refund")
            return result

        @builtins.property
        def include_subscription(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeSubscription``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesubscription
            """
            result = self._values.get("include_subscription")
            return result

        @builtins.property
        def include_support(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeSupport``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesupport
            """
            result = self._values.get("include_support")
            return result

        @builtins.property
        def include_tax(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeTax``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includetax
            """
            result = self._values.get("include_tax")
            return result

        @builtins.property
        def include_upfront(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.IncludeUpfront``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeupfront
            """
            result = self._values.get("include_upfront")
            return result

        @builtins.property
        def use_amortized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.UseAmortized``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useamortized
            """
            result = self._values.get("use_amortized")
            return result

        @builtins.property
        def use_blended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_a771d0ef]]:
            """``CfnBudget.CostTypesProperty.UseBlended``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useblended
            """
            result = self._values.get("use_blended")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CostTypesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.NotificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "notification_type": "notificationType",
            "threshold": "threshold",
            "threshold_type": "thresholdType",
        },
    )
    class NotificationProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            notification_type: builtins.str,
            threshold: jsii.Number,
            threshold_type: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param comparison_operator: ``CfnBudget.NotificationProperty.ComparisonOperator``.
            :param notification_type: ``CfnBudget.NotificationProperty.NotificationType``.
            :param threshold: ``CfnBudget.NotificationProperty.Threshold``.
            :param threshold_type: ``CfnBudget.NotificationProperty.ThresholdType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "notification_type": notification_type,
                "threshold": threshold,
            }
            if threshold_type is not None:
                self._values["threshold_type"] = threshold_type

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            """``CfnBudget.NotificationProperty.ComparisonOperator``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-comparisonoperator
            """
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return result

        @builtins.property
        def notification_type(self) -> builtins.str:
            """``CfnBudget.NotificationProperty.NotificationType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-notificationtype
            """
            result = self._values.get("notification_type")
            assert result is not None, "Required property 'notification_type' is missing"
            return result

        @builtins.property
        def threshold(self) -> jsii.Number:
            """``CfnBudget.NotificationProperty.Threshold``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-threshold
            """
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return result

        @builtins.property
        def threshold_type(self) -> typing.Optional[builtins.str]:
            """``CfnBudget.NotificationProperty.ThresholdType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-thresholdtype
            """
            result = self._values.get("threshold_type")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.NotificationWithSubscribersProperty",
        jsii_struct_bases=[],
        name_mapping={"notification": "notification", "subscribers": "subscribers"},
    )
    class NotificationWithSubscribersProperty:
        def __init__(
            self,
            *,
            notification: typing.Union["CfnBudget.NotificationProperty", _IResolvable_a771d0ef],
            subscribers: typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnBudget.SubscriberProperty", _IResolvable_a771d0ef]]],
        ) -> None:
            """
            :param notification: ``CfnBudget.NotificationWithSubscribersProperty.Notification``.
            :param subscribers: ``CfnBudget.NotificationWithSubscribersProperty.Subscribers``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "notification": notification,
                "subscribers": subscribers,
            }

        @builtins.property
        def notification(
            self,
        ) -> typing.Union["CfnBudget.NotificationProperty", _IResolvable_a771d0ef]:
            """``CfnBudget.NotificationWithSubscribersProperty.Notification``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-notification
            """
            result = self._values.get("notification")
            assert result is not None, "Required property 'notification' is missing"
            return result

        @builtins.property
        def subscribers(
            self,
        ) -> typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union["CfnBudget.SubscriberProperty", _IResolvable_a771d0ef]]]:
            """``CfnBudget.NotificationWithSubscribersProperty.Subscribers``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-subscribers
            """
            result = self._values.get("subscribers")
            assert result is not None, "Required property 'subscribers' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationWithSubscribersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.SpendProperty",
        jsii_struct_bases=[],
        name_mapping={"amount": "amount", "unit": "unit"},
    )
    class SpendProperty:
        def __init__(self, *, amount: jsii.Number, unit: builtins.str) -> None:
            """
            :param amount: ``CfnBudget.SpendProperty.Amount``.
            :param unit: ``CfnBudget.SpendProperty.Unit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "amount": amount,
                "unit": unit,
            }

        @builtins.property
        def amount(self) -> jsii.Number:
            """``CfnBudget.SpendProperty.Amount``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-amount
            """
            result = self._values.get("amount")
            assert result is not None, "Required property 'amount' is missing"
            return result

        @builtins.property
        def unit(self) -> builtins.str:
            """``CfnBudget.SpendProperty.Unit``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-unit
            """
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpendProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.SubscriberProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "subscription_type": "subscriptionType"},
    )
    class SubscriberProperty:
        def __init__(
            self,
            *,
            address: builtins.str,
            subscription_type: builtins.str,
        ) -> None:
            """
            :param address: ``CfnBudget.SubscriberProperty.Address``.
            :param subscription_type: ``CfnBudget.SubscriberProperty.SubscriptionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html
            """
            self._values: typing.Dict[str, typing.Any] = {
                "address": address,
                "subscription_type": subscription_type,
            }

        @builtins.property
        def address(self) -> builtins.str:
            """``CfnBudget.SubscriberProperty.Address``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-address
            """
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return result

        @builtins.property
        def subscription_type(self) -> builtins.str:
            """``CfnBudget.SubscriberProperty.SubscriptionType``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-subscriptiontype
            """
            result = self._values.get("subscription_type")
            assert result is not None, "Required property 'subscription_type' is missing"
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="monocdk.aws_budgets.CfnBudget.TimePeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class TimePeriodProperty:
        def __init__(
            self,
            *,
            end: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
        ) -> None:
            """
            :param end: ``CfnBudget.TimePeriodProperty.End``.
            :param start: ``CfnBudget.TimePeriodProperty.Start``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html
            """
            self._values: typing.Dict[str, typing.Any] = {}
            if end is not None:
                self._values["end"] = end
            if start is not None:
                self._values["start"] = start

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            """``CfnBudget.TimePeriodProperty.End``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-end
            """
            result = self._values.get("end")
            return result

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            """``CfnBudget.TimePeriodProperty.Start``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-start
            """
            result = self._values.get("start")
            return result

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimePeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_budgets.CfnBudgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "budget": "budget",
        "notifications_with_subscribers": "notificationsWithSubscribers",
    },
)
class CfnBudgetProps:
    def __init__(
        self,
        *,
        budget: typing.Union[CfnBudget.BudgetDataProperty, _IResolvable_a771d0ef],
        notifications_with_subscribers: typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnBudget.NotificationWithSubscribersProperty, _IResolvable_a771d0ef]]]] = None,
    ) -> None:
        """Properties for defining a ``AWS::Budgets::Budget``.

        :param budget: ``AWS::Budgets::Budget.Budget``.
        :param notifications_with_subscribers: ``AWS::Budgets::Budget.NotificationsWithSubscribers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
        """
        self._values: typing.Dict[str, typing.Any] = {
            "budget": budget,
        }
        if notifications_with_subscribers is not None:
            self._values["notifications_with_subscribers"] = notifications_with_subscribers

    @builtins.property
    def budget(
        self,
    ) -> typing.Union[CfnBudget.BudgetDataProperty, _IResolvable_a771d0ef]:
        """``AWS::Budgets::Budget.Budget``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget
        """
        result = self._values.get("budget")
        assert result is not None, "Required property 'budget' is missing"
        return result

    @builtins.property
    def notifications_with_subscribers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_a771d0ef, typing.List[typing.Union[CfnBudget.NotificationWithSubscribersProperty, _IResolvable_a771d0ef]]]]:
        """``AWS::Budgets::Budget.NotificationsWithSubscribers``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers
        """
        result = self._values.get("notifications_with_subscribers")
        return result

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBudgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBudget",
    "CfnBudgetProps",
]

publication.publish()
