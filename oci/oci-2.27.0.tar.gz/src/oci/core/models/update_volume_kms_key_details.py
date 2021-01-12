# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVolumeKmsKeyDetails(object):
    """
    UpdateVolumeKmsKeyDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVolumeKmsKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this UpdateVolumeKmsKeyDetails.
        :type kms_key_id: str

        """
        self.swagger_types = {
            'kms_key_id': 'str'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId'
        }

        self._kms_key_id = None

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this UpdateVolumeKmsKeyDetails.
        The OCID of the new Key Management key to assign to protect the specified volume.
        This key has to be a valid Key Management key, and policies must exist to allow the user and the Block Volume service to access this key.
        If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.


        :return: The kms_key_id of this UpdateVolumeKmsKeyDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this UpdateVolumeKmsKeyDetails.
        The OCID of the new Key Management key to assign to protect the specified volume.
        This key has to be a valid Key Management key, and policies must exist to allow the user and the Block Volume service to access this key.
        If you specify the same OCID as the previous key's OCID, the Block Volume service will use it to regenerate a volume encryption key.


        :param kms_key_id: The kms_key_id of this UpdateVolumeKmsKeyDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
