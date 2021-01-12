# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobDefinitionPermissionsSummary(object):
    """
    Permissions object for job definitions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobDefinitionPermissionsSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_definition_key:
            The value to assign to the job_definition_key property of this JobDefinitionPermissionsSummary.
        :type job_definition_key: str

        :param user_permissions:
            The value to assign to the user_permissions property of this JobDefinitionPermissionsSummary.
        :type user_permissions: list[str]

        """
        self.swagger_types = {
            'job_definition_key': 'str',
            'user_permissions': 'list[str]'
        }

        self.attribute_map = {
            'job_definition_key': 'jobDefinitionKey',
            'user_permissions': 'userPermissions'
        }

        self._job_definition_key = None
        self._user_permissions = None

    @property
    def job_definition_key(self):
        """
        Gets the job_definition_key of this JobDefinitionPermissionsSummary.
        The unique key of the parent job definition.


        :return: The job_definition_key of this JobDefinitionPermissionsSummary.
        :rtype: str
        """
        return self._job_definition_key

    @job_definition_key.setter
    def job_definition_key(self, job_definition_key):
        """
        Sets the job_definition_key of this JobDefinitionPermissionsSummary.
        The unique key of the parent job definition.


        :param job_definition_key: The job_definition_key of this JobDefinitionPermissionsSummary.
        :type: str
        """
        self._job_definition_key = job_definition_key

    @property
    def user_permissions(self):
        """
        Gets the user_permissions of this JobDefinitionPermissionsSummary.
        An array of permissions.


        :return: The user_permissions of this JobDefinitionPermissionsSummary.
        :rtype: list[str]
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(self, user_permissions):
        """
        Sets the user_permissions of this JobDefinitionPermissionsSummary.
        An array of permissions.


        :param user_permissions: The user_permissions of this JobDefinitionPermissionsSummary.
        :type: list[str]
        """
        self._user_permissions = user_permissions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
