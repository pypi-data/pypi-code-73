# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePatternDetails(object):
    """
    Properties used in data asset create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePatternDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreatePatternDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreatePatternDetails.
        :type description: str

        :param expression:
            The value to assign to the expression property of this CreatePatternDetails.
        :type expression: str

        :param check_file_path_list:
            The value to assign to the check_file_path_list property of this CreatePatternDetails.
        :type check_file_path_list: list[str]

        :param is_enable_check_failure_limit:
            The value to assign to the is_enable_check_failure_limit property of this CreatePatternDetails.
        :type is_enable_check_failure_limit: bool

        :param check_failure_limit:
            The value to assign to the check_failure_limit property of this CreatePatternDetails.
        :type check_failure_limit: int

        :param properties:
            The value to assign to the properties property of this CreatePatternDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'expression': 'str',
            'check_file_path_list': 'list[str]',
            'is_enable_check_failure_limit': 'bool',
            'check_failure_limit': 'int',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'expression': 'expression',
            'check_file_path_list': 'checkFilePathList',
            'is_enable_check_failure_limit': 'isEnableCheckFailureLimit',
            'check_failure_limit': 'checkFailureLimit',
            'properties': 'properties'
        }

        self._display_name = None
        self._description = None
        self._expression = None
        self._check_file_path_list = None
        self._is_enable_check_failure_limit = None
        self._check_failure_limit = None
        self._properties = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreatePatternDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreatePatternDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreatePatternDetails.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreatePatternDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreatePatternDetails.
        Detailed description of the Pattern.


        :return: The description of this CreatePatternDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreatePatternDetails.
        Detailed description of the Pattern.


        :param description: The description of this CreatePatternDetails.
        :type: str
        """
        self._description = description

    @property
    def expression(self):
        """
        Gets the expression of this CreatePatternDetails.
        The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.


        :return: The expression of this CreatePatternDetails.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this CreatePatternDetails.
        The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.


        :param expression: The expression of this CreatePatternDetails.
        :type: str
        """
        self._expression = expression

    @property
    def check_file_path_list(self):
        """
        Gets the check_file_path_list of this CreatePatternDetails.
        List of file paths against which the expression can be tried, as a check. This documents, for reference
        purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true,
        this will be run as a validation during the request, such that if the check fails the request fails. If
        isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even
        if the check fails, with a lifecycleState of FAILED.


        :return: The check_file_path_list of this CreatePatternDetails.
        :rtype: list[str]
        """
        return self._check_file_path_list

    @check_file_path_list.setter
    def check_file_path_list(self, check_file_path_list):
        """
        Sets the check_file_path_list of this CreatePatternDetails.
        List of file paths against which the expression can be tried, as a check. This documents, for reference
        purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true,
        this will be run as a validation during the request, such that if the check fails the request fails. If
        isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even
        if the check fails, with a lifecycleState of FAILED.


        :param check_file_path_list: The check_file_path_list of this CreatePatternDetails.
        :type: list[str]
        """
        self._check_file_path_list = check_file_path_list

    @property
    def is_enable_check_failure_limit(self):
        """
        Gets the is_enable_check_failure_limit of this CreatePatternDetails.
        Indicates whether the expression check, against the checkFilePathList, will fail the request if the count of
        UNMATCHED files is above the checkFailureLimit.


        :return: The is_enable_check_failure_limit of this CreatePatternDetails.
        :rtype: bool
        """
        return self._is_enable_check_failure_limit

    @is_enable_check_failure_limit.setter
    def is_enable_check_failure_limit(self, is_enable_check_failure_limit):
        """
        Sets the is_enable_check_failure_limit of this CreatePatternDetails.
        Indicates whether the expression check, against the checkFilePathList, will fail the request if the count of
        UNMATCHED files is above the checkFailureLimit.


        :param is_enable_check_failure_limit: The is_enable_check_failure_limit of this CreatePatternDetails.
        :type: bool
        """
        self._is_enable_check_failure_limit = is_enable_check_failure_limit

    @property
    def check_failure_limit(self):
        """
        Gets the check_failure_limit of this CreatePatternDetails.
        The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if
        checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.


        :return: The check_failure_limit of this CreatePatternDetails.
        :rtype: int
        """
        return self._check_failure_limit

    @check_failure_limit.setter
    def check_failure_limit(self, check_failure_limit):
        """
        Sets the check_failure_limit of this CreatePatternDetails.
        The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if
        checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.


        :param check_failure_limit: The check_failure_limit of this CreatePatternDetails.
        :type: int
        """
        self._check_failure_limit = check_failure_limit

    @property
    def properties(self):
        """
        Gets the properties of this CreatePatternDetails.
        A map of maps that contains the properties which are specific to the pattern type. Each pattern type
        definition defines it's set of required and optional properties.
        Example: `{\"properties\": { \"default\": { \"tbd\"}}}`


        :return: The properties of this CreatePatternDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreatePatternDetails.
        A map of maps that contains the properties which are specific to the pattern type. Each pattern type
        definition defines it's set of required and optional properties.
        Example: `{\"properties\": { \"default\": { \"tbd\"}}}`


        :param properties: The properties of this CreatePatternDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
