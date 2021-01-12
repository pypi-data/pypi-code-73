# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestResourceSubTypeDetail(object):
    """
    SubType information for a work request resource.
    """

    #: A constant which can be used with the sub_type_status property of a WorkRequestResourceSubTypeDetail.
    #: This constant has a value of "CREATED"
    SUB_TYPE_STATUS_CREATED = "CREATED"

    #: A constant which can be used with the sub_type_status property of a WorkRequestResourceSubTypeDetail.
    #: This constant has a value of "UPDATED"
    SUB_TYPE_STATUS_UPDATED = "UPDATED"

    #: A constant which can be used with the sub_type_status property of a WorkRequestResourceSubTypeDetail.
    #: This constant has a value of "DELETED"
    SUB_TYPE_STATUS_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestResourceSubTypeDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sub_type:
            The value to assign to the sub_type property of this WorkRequestResourceSubTypeDetail.
        :type sub_type: str

        :param sub_type_key:
            The value to assign to the sub_type_key property of this WorkRequestResourceSubTypeDetail.
        :type sub_type_key: str

        :param sub_type_status:
            The value to assign to the sub_type_status property of this WorkRequestResourceSubTypeDetail.
            Allowed values for this property are: "CREATED", "UPDATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sub_type_status: str

        """
        self.swagger_types = {
            'sub_type': 'str',
            'sub_type_key': 'str',
            'sub_type_status': 'str'
        }

        self.attribute_map = {
            'sub_type': 'subType',
            'sub_type_key': 'subTypeKey',
            'sub_type_status': 'subTypeStatus'
        }

        self._sub_type = None
        self._sub_type_key = None
        self._sub_type_status = None

    @property
    def sub_type(self):
        """
        **[Required]** Gets the sub_type of this WorkRequestResourceSubTypeDetail.
        Subtype of the work request resource like osn or peer.


        :return: The sub_type of this WorkRequestResourceSubTypeDetail.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this WorkRequestResourceSubTypeDetail.
        Subtype of the work request resource like osn or peer.


        :param sub_type: The sub_type of this WorkRequestResourceSubTypeDetail.
        :type: str
        """
        self._sub_type = sub_type

    @property
    def sub_type_key(self):
        """
        **[Required]** Gets the sub_type_key of this WorkRequestResourceSubTypeDetail.
        The identifier of the resource subType.


        :return: The sub_type_key of this WorkRequestResourceSubTypeDetail.
        :rtype: str
        """
        return self._sub_type_key

    @sub_type_key.setter
    def sub_type_key(self, sub_type_key):
        """
        Sets the sub_type_key of this WorkRequestResourceSubTypeDetail.
        The identifier of the resource subType.


        :param sub_type_key: The sub_type_key of this WorkRequestResourceSubTypeDetail.
        :type: str
        """
        self._sub_type_key = sub_type_key

    @property
    def sub_type_status(self):
        """
        **[Required]** Gets the sub_type_status of this WorkRequestResourceSubTypeDetail.
        Status of the resource subType, as a result of the work tracked in this work request.
        A resource subType would be CREATED, UPDATED or DELETED, after the work request is completed.

        Allowed values for this property are: "CREATED", "UPDATED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sub_type_status of this WorkRequestResourceSubTypeDetail.
        :rtype: str
        """
        return self._sub_type_status

    @sub_type_status.setter
    def sub_type_status(self, sub_type_status):
        """
        Sets the sub_type_status of this WorkRequestResourceSubTypeDetail.
        Status of the resource subType, as a result of the work tracked in this work request.
        A resource subType would be CREATED, UPDATED or DELETED, after the work request is completed.


        :param sub_type_status: The sub_type_status of this WorkRequestResourceSubTypeDetail.
        :type: str
        """
        allowed_values = ["CREATED", "UPDATED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(sub_type_status, allowed_values):
            sub_type_status = 'UNKNOWN_ENUM_VALUE'
        self._sub_type_status = sub_type_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
