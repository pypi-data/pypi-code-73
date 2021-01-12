# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseManualRefreshDetails(object):
    """
    Details of manual refresh for an Autonomous Database refreshable clone.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseManualRefreshDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_refresh_cutoff:
            The value to assign to the time_refresh_cutoff property of this AutonomousDatabaseManualRefreshDetails.
        :type time_refresh_cutoff: datetime

        """
        self.swagger_types = {
            'time_refresh_cutoff': 'datetime'
        }

        self.attribute_map = {
            'time_refresh_cutoff': 'timeRefreshCutoff'
        }

        self._time_refresh_cutoff = None

    @property
    def time_refresh_cutoff(self):
        """
        Gets the time_refresh_cutoff of this AutonomousDatabaseManualRefreshDetails.
        The timestamp to which the Autonomous Database refreshable clone will be refreshed. Changes made in the primary database after this timestamp are not part of the data refresh.


        :return: The time_refresh_cutoff of this AutonomousDatabaseManualRefreshDetails.
        :rtype: datetime
        """
        return self._time_refresh_cutoff

    @time_refresh_cutoff.setter
    def time_refresh_cutoff(self, time_refresh_cutoff):
        """
        Sets the time_refresh_cutoff of this AutonomousDatabaseManualRefreshDetails.
        The timestamp to which the Autonomous Database refreshable clone will be refreshed. Changes made in the primary database after this timestamp are not part of the data refresh.


        :param time_refresh_cutoff: The time_refresh_cutoff of this AutonomousDatabaseManualRefreshDetails.
        :type: datetime
        """
        self._time_refresh_cutoff = time_refresh_cutoff

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
