# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.11
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.user_request_info import UserRequestInfo  # noqa: E501
from agilicus_api.rest import ApiException

class TestUserRequestInfo(unittest.TestCase):
    """UserRequestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserRequestInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.user_request_info.UserRequestInfo()  # noqa: E501
        if include_optional :
            return UserRequestInfo(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.user_request_info_spec.UserRequestInfoSpec(
                    user_id = 'tuU7smH86zAXMl76sua6xQ', 
                    org_id = 'IAsl3dl40aSsfLKiU76', 
                    requested_resource = 'phone', 
                    requested_sub_resource = 'self', 
                    requested_resource_type = 'application_access', 
                    request_information = 'I need this to do my job', 
                    state = 'pending', ), 
                status = agilicus_api.models.user_request_info_status.UserRequestInfoStatus(
                    email = 'foo@example.com', )
            )
        else :
            return UserRequestInfo(
                spec = agilicus_api.models.user_request_info_spec.UserRequestInfoSpec(
                    user_id = 'tuU7smH86zAXMl76sua6xQ', 
                    org_id = 'IAsl3dl40aSsfLKiU76', 
                    requested_resource = 'phone', 
                    requested_sub_resource = 'self', 
                    requested_resource_type = 'application_access', 
                    request_information = 'I need this to do my job', 
                    state = 'pending', ),
        )

    def testUserRequestInfo(self):
        """Test UserRequestInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
