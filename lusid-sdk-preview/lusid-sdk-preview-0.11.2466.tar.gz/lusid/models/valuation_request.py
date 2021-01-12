# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2466
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ValuationRequest(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'recipe_id': 'ResourceId',
        'as_at': 'datetime',
        'metrics': 'list[AggregateSpec]',
        'group_by': 'list[str]',
        'filters': 'list[PropertyFilter]',
        'sort': 'list[OrderBySpec]',
        'report_currency': 'str',
        'equip_with_subtotals': 'bool',
        'portfolio_entity_ids': 'list[PortfolioEntityId]',
        'valuation_schedule': 'ValuationSchedule'
    }

    attribute_map = {
        'recipe_id': 'recipeId',
        'as_at': 'asAt',
        'metrics': 'metrics',
        'group_by': 'groupBy',
        'filters': 'filters',
        'sort': 'sort',
        'report_currency': 'reportCurrency',
        'equip_with_subtotals': 'equipWithSubtotals',
        'portfolio_entity_ids': 'portfolioEntityIds',
        'valuation_schedule': 'valuationSchedule'
    }

    required_map = {
        'recipe_id': 'optional',
        'as_at': 'optional',
        'metrics': 'required',
        'group_by': 'optional',
        'filters': 'optional',
        'sort': 'optional',
        'report_currency': 'optional',
        'equip_with_subtotals': 'optional',
        'portfolio_entity_ids': 'optional',
        'valuation_schedule': 'optional'
    }

    def __init__(self, recipe_id=None, as_at=None, metrics=None, group_by=None, filters=None, sort=None, report_currency=None, equip_with_subtotals=None, portfolio_entity_ids=None, valuation_schedule=None):  # noqa: E501
        """
        ValuationRequest - a model defined in OpenAPI

        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param as_at:  The asAt date to use
        :type as_at: datetime
        :param metrics:  The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec('Holding/default/PV','Sum') for returning the PV (present value) of holdings  AggregateSpec('Holding/default/Units','Sum') for returning the units of holidays  AggregateSpec('Instrument/default/LusidInstrumentId','Value') for returning the Lusid Instrument identifier (required)
        :type metrics: list[lusid.AggregateSpec]
        :param group_by:  The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.
        :type group_by: list[str]
        :param filters:  A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.
        :type filters: list[lusid.PropertyFilter]
        :param sort:  A (possibly empty/null) set of specifications for how to order the results.
        :type sort: list[lusid.OrderBySpec]
        :param report_currency:  Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.
        :type report_currency: str
        :param equip_with_subtotals:  Flag directing the Valuation call to populate the results with subtotals of aggregates.
        :type equip_with_subtotals: bool
        :param portfolio_entity_ids:  The set of portfolio or portfolio group identifier(s) that is to be valued.
        :type portfolio_entity_ids: list[lusid.PortfolioEntityId]
        :param valuation_schedule: 
        :type valuation_schedule: lusid.ValuationSchedule

        """  # noqa: E501

        self._recipe_id = None
        self._as_at = None
        self._metrics = None
        self._group_by = None
        self._filters = None
        self._sort = None
        self._report_currency = None
        self._equip_with_subtotals = None
        self._portfolio_entity_ids = None
        self._valuation_schedule = None
        self.discriminator = None

        if recipe_id is not None:
            self.recipe_id = recipe_id
        self.as_at = as_at
        self.metrics = metrics
        self.group_by = group_by
        self.filters = filters
        self.sort = sort
        self.report_currency = report_currency
        if equip_with_subtotals is not None:
            self.equip_with_subtotals = equip_with_subtotals
        self.portfolio_entity_ids = portfolio_entity_ids
        if valuation_schedule is not None:
            self.valuation_schedule = valuation_schedule

    @property
    def recipe_id(self):
        """Gets the recipe_id of this ValuationRequest.  # noqa: E501


        :return: The recipe_id of this ValuationRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this ValuationRequest.


        :param recipe_id: The recipe_id of this ValuationRequest.  # noqa: E501
        :type: ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def as_at(self):
        """Gets the as_at of this ValuationRequest.  # noqa: E501

        The asAt date to use  # noqa: E501

        :return: The as_at of this ValuationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this ValuationRequest.

        The asAt date to use  # noqa: E501

        :param as_at: The as_at of this ValuationRequest.  # noqa: E501
        :type: datetime
        """

        self._as_at = as_at

    @property
    def metrics(self):
        """Gets the metrics of this ValuationRequest.  # noqa: E501

        The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec('Holding/default/PV','Sum') for returning the PV (present value) of holdings  AggregateSpec('Holding/default/Units','Sum') for returning the units of holidays  AggregateSpec('Instrument/default/LusidInstrumentId','Value') for returning the Lusid Instrument identifier  # noqa: E501

        :return: The metrics of this ValuationRequest.  # noqa: E501
        :rtype: list[AggregateSpec]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ValuationRequest.

        The set of specifications to calculate or retrieve during the valuation and present in the results. For example:  AggregateSpec('Holding/default/PV','Sum') for returning the PV (present value) of holdings  AggregateSpec('Holding/default/Units','Sum') for returning the units of holidays  AggregateSpec('Instrument/default/LusidInstrumentId','Value') for returning the Lusid Instrument identifier  # noqa: E501

        :param metrics: The metrics of this ValuationRequest.  # noqa: E501
        :type: list[AggregateSpec]
        """
        if metrics is None:
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def group_by(self):
        """Gets the group_by of this ValuationRequest.  # noqa: E501

        The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.  # noqa: E501

        :return: The group_by of this ValuationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ValuationRequest.

        The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out.  # noqa: E501

        :param group_by: The group_by of this ValuationRequest.  # noqa: E501
        :type: list[str]
        """

        self._group_by = group_by

    @property
    def filters(self):
        """Gets the filters of this ValuationRequest.  # noqa: E501

        A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.  # noqa: E501

        :return: The filters of this ValuationRequest.  # noqa: E501
        :rtype: list[PropertyFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ValuationRequest.

        A set of filters to use to reduce the data found in a request. Equivalent to the 'where ...' part of a Sql select statement.  For example, filter a set of values within a given range or matching a particular value.  # noqa: E501

        :param filters: The filters of this ValuationRequest.  # noqa: E501
        :type: list[PropertyFilter]
        """

        self._filters = filters

    @property
    def sort(self):
        """Gets the sort of this ValuationRequest.  # noqa: E501

        A (possibly empty/null) set of specifications for how to order the results.  # noqa: E501

        :return: The sort of this ValuationRequest.  # noqa: E501
        :rtype: list[OrderBySpec]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ValuationRequest.

        A (possibly empty/null) set of specifications for how to order the results.  # noqa: E501

        :param sort: The sort of this ValuationRequest.  # noqa: E501
        :type: list[OrderBySpec]
        """

        self._sort = sort

    @property
    def report_currency(self):
        """Gets the report_currency of this ValuationRequest.  # noqa: E501

        Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.  # noqa: E501

        :return: The report_currency of this ValuationRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_currency

    @report_currency.setter
    def report_currency(self, report_currency):
        """Sets the report_currency of this ValuationRequest.

        Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  If not present, then the currency of the relevant portfolio will be used in its place.  # noqa: E501

        :param report_currency: The report_currency of this ValuationRequest.  # noqa: E501
        :type: str
        """

        self._report_currency = report_currency

    @property
    def equip_with_subtotals(self):
        """Gets the equip_with_subtotals of this ValuationRequest.  # noqa: E501

        Flag directing the Valuation call to populate the results with subtotals of aggregates.  # noqa: E501

        :return: The equip_with_subtotals of this ValuationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._equip_with_subtotals

    @equip_with_subtotals.setter
    def equip_with_subtotals(self, equip_with_subtotals):
        """Sets the equip_with_subtotals of this ValuationRequest.

        Flag directing the Valuation call to populate the results with subtotals of aggregates.  # noqa: E501

        :param equip_with_subtotals: The equip_with_subtotals of this ValuationRequest.  # noqa: E501
        :type: bool
        """

        self._equip_with_subtotals = equip_with_subtotals

    @property
    def portfolio_entity_ids(self):
        """Gets the portfolio_entity_ids of this ValuationRequest.  # noqa: E501

        The set of portfolio or portfolio group identifier(s) that is to be valued.  # noqa: E501

        :return: The portfolio_entity_ids of this ValuationRequest.  # noqa: E501
        :rtype: list[PortfolioEntityId]
        """
        return self._portfolio_entity_ids

    @portfolio_entity_ids.setter
    def portfolio_entity_ids(self, portfolio_entity_ids):
        """Sets the portfolio_entity_ids of this ValuationRequest.

        The set of portfolio or portfolio group identifier(s) that is to be valued.  # noqa: E501

        :param portfolio_entity_ids: The portfolio_entity_ids of this ValuationRequest.  # noqa: E501
        :type: list[PortfolioEntityId]
        """

        self._portfolio_entity_ids = portfolio_entity_ids

    @property
    def valuation_schedule(self):
        """Gets the valuation_schedule of this ValuationRequest.  # noqa: E501


        :return: The valuation_schedule of this ValuationRequest.  # noqa: E501
        :rtype: ValuationSchedule
        """
        return self._valuation_schedule

    @valuation_schedule.setter
    def valuation_schedule(self, valuation_schedule):
        """Sets the valuation_schedule of this ValuationRequest.


        :param valuation_schedule: The valuation_schedule of this ValuationRequest.  # noqa: E501
        :type: ValuationSchedule
        """

        self._valuation_schedule = valuation_schedule

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
        if not isinstance(other, ValuationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
