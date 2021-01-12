# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .target_details import TargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoringTargetDetails(TargetDetails):
    """
    The monitoring target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoringTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.MonitoringTargetDetails.kind` attribute
        of this class is ``monitoring`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this MonitoringTargetDetails.
            Allowed values for this property are: "streaming", "objectStorage", "monitoring", "functions", "notifications"
        :type kind: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoringTargetDetails.
        :type compartment_id: str

        :param metric_namespace:
            The value to assign to the metric_namespace property of this MonitoringTargetDetails.
        :type metric_namespace: str

        :param metric:
            The value to assign to the metric property of this MonitoringTargetDetails.
        :type metric: str

        """
        self.swagger_types = {
            'kind': 'str',
            'compartment_id': 'str',
            'metric_namespace': 'str',
            'metric': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'compartment_id': 'compartmentId',
            'metric_namespace': 'metricNamespace',
            'metric': 'metric'
        }

        self._kind = None
        self._compartment_id = None
        self._metric_namespace = None
        self._metric = None
        self._kind = 'monitoring'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoringTargetDetails.
        The `OCID`__ of the compartment containing the metric.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoringTargetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoringTargetDetails.
        The `OCID`__ of the compartment containing the metric.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoringTargetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def metric_namespace(self):
        """
        **[Required]** Gets the metric_namespace of this MonitoringTargetDetails.
        The namespace of the metric.

        Example: `oci_computeagent`


        :return: The metric_namespace of this MonitoringTargetDetails.
        :rtype: str
        """
        return self._metric_namespace

    @metric_namespace.setter
    def metric_namespace(self, metric_namespace):
        """
        Sets the metric_namespace of this MonitoringTargetDetails.
        The namespace of the metric.

        Example: `oci_computeagent`


        :param metric_namespace: The metric_namespace of this MonitoringTargetDetails.
        :type: str
        """
        self._metric_namespace = metric_namespace

    @property
    def metric(self):
        """
        **[Required]** Gets the metric of this MonitoringTargetDetails.
        The name of the metric.

        Example: `CpuUtilization`


        :return: The metric of this MonitoringTargetDetails.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MonitoringTargetDetails.
        The name of the metric.

        Example: `CpuUtilization`


        :param metric: The metric of this MonitoringTargetDetails.
        :type: str
        """
        self._metric = metric

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
