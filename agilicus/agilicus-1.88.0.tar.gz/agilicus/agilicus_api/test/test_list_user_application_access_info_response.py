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
from agilicus_api.models.list_user_application_access_info_response import ListUserApplicationAccessInfoResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListUserApplicationAccessInfoResponse(unittest.TestCase):
    """ListUserApplicationAccessInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUserApplicationAccessInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_user_application_access_info_response.ListUserApplicationAccessInfoResponse()  # noqa: E501
        if include_optional :
            return ListUserApplicationAccessInfoResponse(
                user_application_access_info = [
                    agilicus_api.models.user_application_access_info.UserApplicationAccessInfo(
                        status = agilicus_api.models.user_application_access_info_status.UserApplicationAccessInfoStatus(
                            user_id = 'tuU7smH86zAXMl76sua6xQ', 
                            org_id = 'IAsl3dl40aSsfLKiU76', 
                            org_name = 'egov', 
                            parent_org_id = 'G99q3lasls29wsk', 
                            parent_org_name = 'root', 
                            application_name = 'parking', 
                            application_url = 'https://parking.cloud.egov.city', 
                            application_description = 'An application to submit parking requests', 
                            application_category = 'citizen-facing', 
                            icon_url = 'https://storage.googleapis.com/agilicus/logo.svg', 
                            access_level = 'requested', 
                            application_default_role_name = 'self', 
                            application_default_role_id = 'as0Z6fXFsl23', 
                            roles = [
                                '0'
                                ], ), )
                    ], 
                limit = 56
            )
        else :
            return ListUserApplicationAccessInfoResponse(
                user_application_access_info = [
                    agilicus_api.models.user_application_access_info.UserApplicationAccessInfo(
                        status = agilicus_api.models.user_application_access_info_status.UserApplicationAccessInfoStatus(
                            user_id = 'tuU7smH86zAXMl76sua6xQ', 
                            org_id = 'IAsl3dl40aSsfLKiU76', 
                            org_name = 'egov', 
                            parent_org_id = 'G99q3lasls29wsk', 
                            parent_org_name = 'root', 
                            application_name = 'parking', 
                            application_url = 'https://parking.cloud.egov.city', 
                            application_description = 'An application to submit parking requests', 
                            application_category = 'citizen-facing', 
                            icon_url = 'https://storage.googleapis.com/agilicus/logo.svg', 
                            access_level = 'requested', 
                            application_default_role_name = 'self', 
                            application_default_role_id = 'as0Z6fXFsl23', 
                            roles = [
                                '0'
                                ], ), )
                    ],
                limit = 56,
        )

    def testListUserApplicationAccessInfoResponse(self):
        """Test ListUserApplicationAccessInfoResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
