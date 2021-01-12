# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.12
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class File(object):
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
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'tag': 'str',
        'label': 'str',
        'size': 'int',
        'visibility': 'FileVisibility',
        'public_url': 'str',
        'region': 'StorageRegion',
        'lock': 'bool',
        'storage_path': 'str',
        'md5_hash': 'str',
        'last_accessed': 'datetime',
        'created': 'datetime',
        'updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag': 'tag',
        'label': 'label',
        'size': 'size',
        'visibility': 'visibility',
        'public_url': 'public_url',
        'region': 'region',
        'lock': 'lock',
        'storage_path': 'storage_path',
        'md5_hash': 'md5_hash',
        'last_accessed': 'last_accessed',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, tag=None, label=None, size=None, visibility=None, public_url=None, region=None, lock=None, storage_path=None, md5_hash=None, last_accessed=None, created=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._tag = None
        self._label = None
        self._size = None
        self._visibility = None
        self._public_url = None
        self._region = None
        self._lock = None
        self._storage_path = None
        self._md5_hash = None
        self._last_accessed = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if label is not None:
            self.label = label
        if size is not None:
            self.size = size
        if visibility is not None:
            self.visibility = visibility
        if public_url is not None:
            self.public_url = public_url
        if region is not None:
            self.region = region
        if lock is not None:
            self.lock = lock
        if storage_path is not None:
            self.storage_path = storage_path
        if md5_hash is not None:
            self.md5_hash = md5_hash
        if last_accessed is not None:
            self.last_accessed = last_accessed
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this File.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.

        Unique identifier  # noqa: E501

        :param id: The id of this File.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this File.  # noqa: E501

        Name of file  # noqa: E501

        :return: The name of this File.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this File.

        Name of file  # noqa: E501

        :param name: The name of this File.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this File.  # noqa: E501

        A file tag  # noqa: E501

        :return: The tag of this File.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this File.

        A file tag  # noqa: E501

        :param tag: The tag of this File.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def label(self):
        """Gets the label of this File.  # noqa: E501

        A file label  # noqa: E501

        :return: The label of this File.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this File.

        A file label  # noqa: E501

        :param label: The label of this File.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def size(self):
        """Gets the size of this File.  # noqa: E501

        Size in bytes of the file  # noqa: E501

        :return: The size of this File.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this File.

        Size in bytes of the file  # noqa: E501

        :param size: The size of this File.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def visibility(self):
        """Gets the visibility of this File.  # noqa: E501


        :return: The visibility of this File.  # noqa: E501
        :rtype: FileVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this File.


        :param visibility: The visibility of this File.  # noqa: E501
        :type: FileVisibility
        """

        self._visibility = visibility

    @property
    def public_url(self):
        """Gets the public_url of this File.  # noqa: E501

        The location of the file on the internet. If present, this file can be downloaded by requesting this URI. If the file is publically visible, then no credentials need be provided.   # noqa: E501

        :return: The public_url of this File.  # noqa: E501
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """Sets the public_url of this File.

        The location of the file on the internet. If present, this file can be downloaded by requesting this URI. If the file is publically visible, then no credentials need be provided.   # noqa: E501

        :param public_url: The public_url of this File.  # noqa: E501
        :type: str
        """

        self._public_url = public_url

    @property
    def region(self):
        """Gets the region of this File.  # noqa: E501


        :return: The region of this File.  # noqa: E501
        :rtype: StorageRegion
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this File.


        :param region: The region of this File.  # noqa: E501
        :type: StorageRegion
        """

        self._region = region

    @property
    def lock(self):
        """Gets the lock of this File.  # noqa: E501

        Locking prevents the deletion or modification of the file  # noqa: E501

        :return: The lock of this File.  # noqa: E501
        :rtype: bool
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this File.

        Locking prevents the deletion or modification of the file  # noqa: E501

        :param lock: The lock of this File.  # noqa: E501
        :type: bool
        """

        self._lock = lock

    @property
    def storage_path(self):
        """Gets the storage_path of this File.  # noqa: E501

        storage path  # noqa: E501

        :return: The storage_path of this File.  # noqa: E501
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """Sets the storage_path of this File.

        storage path  # noqa: E501

        :param storage_path: The storage_path of this File.  # noqa: E501
        :type: str
        """

        self._storage_path = storage_path

    @property
    def md5_hash(self):
        """Gets the md5_hash of this File.  # noqa: E501

        MD5 Hash of file in base64  # noqa: E501

        :return: The md5_hash of this File.  # noqa: E501
        :rtype: str
        """
        return self._md5_hash

    @md5_hash.setter
    def md5_hash(self, md5_hash):
        """Sets the md5_hash of this File.

        MD5 Hash of file in base64  # noqa: E501

        :param md5_hash: The md5_hash of this File.  # noqa: E501
        :type: str
        """

        self._md5_hash = md5_hash

    @property
    def last_accessed(self):
        """Gets the last_accessed of this File.  # noqa: E501

        Time object was last accessed  # noqa: E501

        :return: The last_accessed of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        """Sets the last_accessed of this File.

        Time object was last accessed  # noqa: E501

        :param last_accessed: The last_accessed of this File.  # noqa: E501
        :type: datetime
        """

        self._last_accessed = last_accessed

    @property
    def created(self):
        """Gets the created of this File.  # noqa: E501

        Creation time  # noqa: E501

        :return: The created of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this File.

        Creation time  # noqa: E501

        :param created: The created of this File.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this File.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this File.

        Update time  # noqa: E501

        :param updated: The updated of this File.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
