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
from agilicus_api.models.list_auth_audits_response import ListAuthAuditsResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListAuthAuditsResponse(unittest.TestCase):
    """ListAuthAuditsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListAuthAuditsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_auth_audits_response.ListAuthAuditsResponse()  # noqa: E501
        if include_optional :
            return ListAuthAuditsResponse(
                auth_audits = [
                    agilicus_api.models.auth_audits.AuthAudits(
                        user_id = 'jjkkGmwB9oTJWDjIglTU', 
                        upstream_user_id = 'asvl2-1a1s-asdlk-3sl1', 
                        org_id = '2jkMGmwB9o7JW3jIglNZ', 
                        org_name = '2jkMGmwB9o7JW3jIglNZ', 
                        time = '2002-10-02T10:00-05:00', 
                        event = 'Timeout', 
                        source_ip = '192.0.2.1', 
                        token_id = 'XMYdZy7yAiudMDxQqgDwkY', 
                        trace_id = '00b893c9ec7c0089c3da65e7c9e2263a', 
                        session = '00b893c9ec7c0089c3da65e7c9e2263a', 
                        issuer = 'https://auth.cloud.egov.city', 
                        client_id = 'my-client-id-ABCD', 
                        application_name = 'app-1', 
                        login_org_id = 'Io7MGmwB9o7JW3jIg23B', 
                        login_org_name = 'Io7MGmwB9o7JW3jIg23B', 
                        upstream_idp = 'google', 
                        stage = 'Login', 
                        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) Chrome/83.0.4103.97 Safari/537.36', )
                    ], 
                limit = 56
            )
        else :
            return ListAuthAuditsResponse(
                limit = 56,
        )

    def testListAuthAuditsResponse(self):
        """Test ListAuthAuditsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
