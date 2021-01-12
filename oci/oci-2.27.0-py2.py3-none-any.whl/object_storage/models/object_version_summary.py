# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectVersionSummary(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ObjectVersionSummary.
        :type name: str

        :param size:
            The value to assign to the size property of this ObjectVersionSummary.
        :type size: int

        :param md5:
            The value to assign to the md5 property of this ObjectVersionSummary.
        :type md5: str

        :param time_created:
            The value to assign to the time_created property of this ObjectVersionSummary.
        :type time_created: datetime

        :param time_modified:
            The value to assign to the time_modified property of this ObjectVersionSummary.
        :type time_modified: datetime

        :param etag:
            The value to assign to the etag property of this ObjectVersionSummary.
        :type etag: str

        :param version_id:
            The value to assign to the version_id property of this ObjectVersionSummary.
        :type version_id: str

        :param is_delete_marker:
            The value to assign to the is_delete_marker property of this ObjectVersionSummary.
        :type is_delete_marker: bool

        """
        self.swagger_types = {
            'name': 'str',
            'size': 'int',
            'md5': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'etag': 'str',
            'version_id': 'str',
            'is_delete_marker': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'size': 'size',
            'md5': 'md5',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'etag': 'etag',
            'version_id': 'versionId',
            'is_delete_marker': 'isDeleteMarker'
        }

        self._name = None
        self._size = None
        self._md5 = None
        self._time_created = None
        self._time_modified = None
        self._etag = None
        self._version_id = None
        self._is_delete_marker = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ObjectVersionSummary.
        The name of the object. Avoid entering confidential information.
        Example: test/object1.log


        :return: The name of this ObjectVersionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectVersionSummary.
        The name of the object. Avoid entering confidential information.
        Example: test/object1.log


        :param name: The name of this ObjectVersionSummary.
        :type: str
        """
        self._name = name

    @property
    def size(self):
        """
        Gets the size of this ObjectVersionSummary.
        Size of the object in bytes.


        :return: The size of this ObjectVersionSummary.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ObjectVersionSummary.
        Size of the object in bytes.


        :param size: The size of this ObjectVersionSummary.
        :type: int
        """
        self._size = size

    @property
    def md5(self):
        """
        Gets the md5 of this ObjectVersionSummary.
        Base64-encoded MD5 hash of the object data.


        :return: The md5 of this ObjectVersionSummary.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this ObjectVersionSummary.
        Base64-encoded MD5 hash of the object data.


        :param md5: The md5 of this ObjectVersionSummary.
        :type: str
        """
        self._md5 = md5

    @property
    def time_created(self):
        """
        Gets the time_created of this ObjectVersionSummary.
        The date and time the object was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :return: The time_created of this ObjectVersionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ObjectVersionSummary.
        The date and time the object was created, as described in `RFC 2616`__.

        __ https://tools.ietf.org/html/rfc2616#section-14.29


        :param time_created: The time_created of this ObjectVersionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_modified(self):
        """
        **[Required]** Gets the time_modified of this ObjectVersionSummary.
        The date and time the object was modified, as described in `RFC 2616`__.

        __ https://tools.ietf.org/rfc/rfc2616#section-14.29


        :return: The time_modified of this ObjectVersionSummary.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """
        Sets the time_modified of this ObjectVersionSummary.
        The date and time the object was modified, as described in `RFC 2616`__.

        __ https://tools.ietf.org/rfc/rfc2616#section-14.29


        :param time_modified: The time_modified of this ObjectVersionSummary.
        :type: datetime
        """
        self._time_modified = time_modified

    @property
    def etag(self):
        """
        Gets the etag of this ObjectVersionSummary.
        The current entity tag (ETag) for the object.


        :return: The etag of this ObjectVersionSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this ObjectVersionSummary.
        The current entity tag (ETag) for the object.


        :param etag: The etag of this ObjectVersionSummary.
        :type: str
        """
        self._etag = etag

    @property
    def version_id(self):
        """
        **[Required]** Gets the version_id of this ObjectVersionSummary.
        VersionId of the object.


        :return: The version_id of this ObjectVersionSummary.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """
        Sets the version_id of this ObjectVersionSummary.
        VersionId of the object.


        :param version_id: The version_id of this ObjectVersionSummary.
        :type: str
        """
        self._version_id = version_id

    @property
    def is_delete_marker(self):
        """
        **[Required]** Gets the is_delete_marker of this ObjectVersionSummary.
        This flag will indicate if the version is deleted or not.


        :return: The is_delete_marker of this ObjectVersionSummary.
        :rtype: bool
        """
        return self._is_delete_marker

    @is_delete_marker.setter
    def is_delete_marker(self, is_delete_marker):
        """
        Sets the is_delete_marker of this ObjectVersionSummary.
        This flag will indicate if the version is deleted or not.


        :param is_delete_marker: The is_delete_marker of this ObjectVersionSummary.
        :type: bool
        """
        self._is_delete_marker = is_delete_marker

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
