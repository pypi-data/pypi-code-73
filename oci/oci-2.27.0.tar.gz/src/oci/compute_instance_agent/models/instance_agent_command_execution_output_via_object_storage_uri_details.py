# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_agent_command_execution_output_content import InstanceAgentCommandExecutionOutputContent
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails(InstanceAgentCommandExecutionOutputContent):
    """
    command execution output via uri.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.compute_instance_agent.models.InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.output_type` attribute
        of this class is ``OBJECT_STORAGE_URI`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param output_type:
            The value to assign to the output_type property of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
            Allowed values for this property are: "TEXT", "OBJECT_STORAGE_URI", "OBJECT_STORAGE_TUPLE"
        :type output_type: str

        :param exit_code:
            The value to assign to the exit_code property of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        :type exit_code: int

        :param message:
            The value to assign to the message property of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        :type message: str

        :param output_uri:
            The value to assign to the output_uri property of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        :type output_uri: str

        """
        self.swagger_types = {
            'output_type': 'str',
            'exit_code': 'int',
            'message': 'str',
            'output_uri': 'str'
        }

        self.attribute_map = {
            'output_type': 'outputType',
            'exit_code': 'exitCode',
            'message': 'message',
            'output_uri': 'outputUri'
        }

        self._output_type = None
        self._exit_code = None
        self._message = None
        self._output_uri = None
        self._output_type = 'OBJECT_STORAGE_URI'

    @property
    def output_uri(self):
        """
        **[Required]** Gets the output_uri of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        The Object Storage URL or PAR for the command output.


        :return: The output_uri of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        :rtype: str
        """
        return self._output_uri

    @output_uri.setter
    def output_uri(self, output_uri):
        """
        Sets the output_uri of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        The Object Storage URL or PAR for the command output.


        :param output_uri: The output_uri of this InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails.
        :type: str
        """
        self._output_uri = output_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
