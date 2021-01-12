# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.12
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.list_user_metadata_response import ListUserMetadataResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListUserMetadataResponse(unittest.TestCase):
    """ListUserMetadataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUserMetadataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_user_metadata_response.ListUserMetadataResponse()  # noqa: E501
        if include_optional :
            return ListUserMetadataResponse(
                user_metadata = [
                    agilicus_api.models.user_metadata.UserMetadata(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.user_metadata_spec.UserMetadataSpec(
                            user_id = 'tuU7smH86zAXMl76sua6xQ', 
                            org_id = 'IAsl3dl40aSsfLKiU76', 
                            app_id = 'IAsl3dl40aSsfLKiU76', 
                            name = '0', 
                            data_type = 'mfa_enrollment_expiry', 
                            data = '2002-10-02T10:00:00-05:00', ), )
                    ], 
                limit = 56
            )
        else :
            return ListUserMetadataResponse(
                user_metadata = [
                    agilicus_api.models.user_metadata.UserMetadata(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.user_metadata_spec.UserMetadataSpec(
                            user_id = 'tuU7smH86zAXMl76sua6xQ', 
                            org_id = 'IAsl3dl40aSsfLKiU76', 
                            app_id = 'IAsl3dl40aSsfLKiU76', 
                            name = '0', 
                            data_type = 'mfa_enrollment_expiry', 
                            data = '2002-10-02T10:00:00-05:00', ), )
                    ],
                limit = 56,
        )

    def testListUserMetadataResponse(self):
        """Test ListUserMetadataResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
