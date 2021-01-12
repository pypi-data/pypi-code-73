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


class RuntimeStatus(object):
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
        'overall_status': 'str',
        'running_replicas': 'int',
        'error_message': 'str',
        'restarts': 'int',
        'cpu': 'float',
        'memory': 'float',
        'last_apply_time': 'datetime',
        'updated': 'datetime',
        'running_image': 'str',
        'running_hash': 'str',
        'org_id': 'str'
    }

    attribute_map = {
        'overall_status': 'overall_status',
        'running_replicas': 'running_replicas',
        'error_message': 'error_message',
        'restarts': 'restarts',
        'cpu': 'cpu',
        'memory': 'memory',
        'last_apply_time': 'last_apply_time',
        'updated': 'updated',
        'running_image': 'running_image',
        'running_hash': 'running_hash',
        'org_id': 'org_id'
    }

    def __init__(self, overall_status=None, running_replicas=None, error_message=None, restarts=None, cpu=None, memory=None, last_apply_time=None, updated=None, running_image=None, running_hash=None, org_id=None, local_vars_configuration=None):  # noqa: E501
        """RuntimeStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall_status = None
        self._running_replicas = None
        self._error_message = None
        self._restarts = None
        self._cpu = None
        self._memory = None
        self._last_apply_time = None
        self._updated = None
        self._running_image = None
        self._running_hash = None
        self._org_id = None
        self.discriminator = None

        if overall_status is not None:
            self.overall_status = overall_status
        if running_replicas is not None:
            self.running_replicas = running_replicas
        if error_message is not None:
            self.error_message = error_message
        if restarts is not None:
            self.restarts = restarts
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if last_apply_time is not None:
            self.last_apply_time = last_apply_time
        if updated is not None:
            self.updated = updated
        if running_image is not None:
            self.running_image = running_image
        if running_hash is not None:
            self.running_hash = running_hash
        if org_id is not None:
            self.org_id = org_id

    @property
    def overall_status(self):
        """Gets the overall_status of this RuntimeStatus.  # noqa: E501

        The status of the running components. - A `good` status means that no action is neccessary on this environment - A `warn` status means that there is an issue that should be dealt with   Examples include a rollout failing or crashing containers - A `down` status indicates that there is a service accessibility problem   that should be dealt with as soon as possible. This could   mean that there were multiple failed rollouts, containers are unstable,   access to a neccessary service is down or other problems. - A `stale` status indicates that although there may not be anything wrong,   we haven't been able to update the status recently. This may indicate   an issue with the platform   # noqa: E501

        :return: The overall_status of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """Sets the overall_status of this RuntimeStatus.

        The status of the running components. - A `good` status means that no action is neccessary on this environment - A `warn` status means that there is an issue that should be dealt with   Examples include a rollout failing or crashing containers - A `down` status indicates that there is a service accessibility problem   that should be dealt with as soon as possible. This could   mean that there were multiple failed rollouts, containers are unstable,   access to a neccessary service is down or other problems. - A `stale` status indicates that although there may not be anything wrong,   we haven't been able to update the status recently. This may indicate   an issue with the platform   # noqa: E501

        :param overall_status: The overall_status of this RuntimeStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["good", "warn", "down", "stale"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and overall_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `overall_status` ({0}), must be one of {1}"  # noqa: E501
                .format(overall_status, allowed_values)
            )

        self._overall_status = overall_status

    @property
    def running_replicas(self):
        """Gets the running_replicas of this RuntimeStatus.  # noqa: E501

        The number of current running replicas. 2 is redundant, 1 could indicate error handling, 0 is down.   # noqa: E501

        :return: The running_replicas of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._running_replicas

    @running_replicas.setter
    def running_replicas(self, running_replicas):
        """Sets the running_replicas of this RuntimeStatus.

        The number of current running replicas. 2 is redundant, 1 could indicate error handling, 0 is down.   # noqa: E501

        :param running_replicas: The running_replicas of this RuntimeStatus.  # noqa: E501
        :type: int
        """

        self._running_replicas = running_replicas

    @property
    def error_message(self):
        """Gets the error_message of this RuntimeStatus.  # noqa: E501

        The error in running the current instance. Common errors include CrashLoopBackoff, ContainerPullError, ConfigError. If there is no error description, this will be empty.   # noqa: E501

        :return: The error_message of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this RuntimeStatus.

        The error in running the current instance. Common errors include CrashLoopBackoff, ContainerPullError, ConfigError. If there is no error description, this will be empty.   # noqa: E501

        :param error_message: The error_message of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def restarts(self):
        """Gets the restarts of this RuntimeStatus.  # noqa: E501

        How many times a container has restarted across all replicas of this instance. A non-zero number might indicate some intermittent error that is handled by the Agilicus system. A large number of errors could indicate problems in the application   # noqa: E501

        :return: The restarts of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._restarts

    @restarts.setter
    def restarts(self, restarts):
        """Sets the restarts of this RuntimeStatus.

        How many times a container has restarted across all replicas of this instance. A non-zero number might indicate some intermittent error that is handled by the Agilicus system. A large number of errors could indicate problems in the application   # noqa: E501

        :param restarts: The restarts of this RuntimeStatus.  # noqa: E501
        :type: int
        """

        self._restarts = restarts

    @property
    def cpu(self):
        """Gets the cpu of this RuntimeStatus.  # noqa: E501

        The current number of CPU cores used by all the containers for the instance. A high number eg 1.00 may indicate performance problems as a container is unable to service all requests   # noqa: E501

        :return: The cpu of this RuntimeStatus.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this RuntimeStatus.

        The current number of CPU cores used by all the containers for the instance. A high number eg 1.00 may indicate performance problems as a container is unable to service all requests   # noqa: E501

        :param cpu: The cpu of this RuntimeStatus.  # noqa: E501
        :type: float
        """

        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this RuntimeStatus.  # noqa: E501

        The amount of RAM used by all containers used for the instance in MiB   # noqa: E501

        :return: The memory of this RuntimeStatus.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this RuntimeStatus.

        The amount of RAM used by all containers used for the instance in MiB   # noqa: E501

        :param memory: The memory of this RuntimeStatus.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def last_apply_time(self):
        """Gets the last_apply_time of this RuntimeStatus.  # noqa: E501

        The last time any change was applied to the running containers. This can be used to indicate if the system has 'picked up' a recent change that was made   # noqa: E501

        :return: The last_apply_time of this RuntimeStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_apply_time

    @last_apply_time.setter
    def last_apply_time(self, last_apply_time):
        """Sets the last_apply_time of this RuntimeStatus.

        The last time any change was applied to the running containers. This can be used to indicate if the system has 'picked up' a recent change that was made   # noqa: E501

        :param last_apply_time: The last_apply_time of this RuntimeStatus.  # noqa: E501
        :type: datetime
        """

        self._last_apply_time = last_apply_time

    @property
    def updated(self):
        """Gets the updated of this RuntimeStatus.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this RuntimeStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RuntimeStatus.

        Update time  # noqa: E501

        :param updated: The updated of this RuntimeStatus.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def running_image(self):
        """Gets the running_image of this RuntimeStatus.  # noqa: E501

        The container tag identifies what container is currently running in this instance. This could be different than the configured image if there was an error upgrading. Although relatively rare in practice, the same image tag could have been pushed with many different images, when the container is started it will pull the latest version. See running_hash for more information   # noqa: E501

        :return: The running_image of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._running_image

    @running_image.setter
    def running_image(self, running_image):
        """Sets the running_image of this RuntimeStatus.

        The container tag identifies what container is currently running in this instance. This could be different than the configured image if there was an error upgrading. Although relatively rare in practice, the same image tag could have been pushed with many different images, when the container is started it will pull the latest version. See running_hash for more information   # noqa: E501

        :param running_image: The running_image of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._running_image = running_image

    @property
    def running_hash(self):
        """Gets the running_hash of this RuntimeStatus.  # noqa: E501

        The container hash of What versions users see when they browse to the site. If a image tag has been pushed multiple times, ie for hotfixes then this could be used to identify exactly what software is running   # noqa: E501

        :return: The running_hash of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._running_hash

    @running_hash.setter
    def running_hash(self, running_hash):
        """Sets the running_hash of this RuntimeStatus.

        The container hash of What versions users see when they browse to the site. If a image tag has been pushed multiple times, ie for hotfixes then this could be used to identify exactly what software is running   # noqa: E501

        :param running_hash: The running_hash of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._running_hash = running_hash

    @property
    def org_id(self):
        """Gets the org_id of this RuntimeStatus.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The org_id of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this RuntimeStatus.

        Unique identifier  # noqa: E501

        :param org_id: The org_id of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

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
        if not isinstance(other, RuntimeStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuntimeStatus):
            return True

        return self.to_dict() != other.to_dict()
