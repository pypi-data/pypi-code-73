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
from agilicus_api.models.api_key_introspect_authorization_info import APIKeyIntrospectAuthorizationInfo  # noqa: E501
from agilicus_api.rest import ApiException

class TestAPIKeyIntrospectAuthorizationInfo(unittest.TestCase):
    """APIKeyIntrospectAuthorizationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test APIKeyIntrospectAuthorizationInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.api_key_introspect_authorization_info.APIKeyIntrospectAuthorizationInfo()  # noqa: E501
        if include_optional :
            return APIKeyIntrospectAuthorizationInfo(
                key = '0', 
                username = '0'
            )
        else :
            return APIKeyIntrospectAuthorizationInfo(
                key = '0',
                username = '0',
        )

    def testAPIKeyIntrospectAuthorizationInfo(self):
        """Test APIKeyIntrospectAuthorizationInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
