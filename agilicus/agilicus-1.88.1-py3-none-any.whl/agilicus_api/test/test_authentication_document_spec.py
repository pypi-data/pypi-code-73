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
from agilicus_api.models.authentication_document_spec import AuthenticationDocumentSpec  # noqa: E501
from agilicus_api.rest import ApiException

class TestAuthenticationDocumentSpec(unittest.TestCase):
    """AuthenticationDocumentSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthenticationDocumentSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.authentication_document_spec.AuthenticationDocumentSpec()  # noqa: E501
        if include_optional :
            return AuthenticationDocumentSpec(
                user_id = 'asdfghjklmn123', 
                org_id = 'asdfghjklmn123', 
                auth_issuer_url = 'https://auth.cloud.egov.city', 
                expiry = '2002-10-02T10:00-05:00'
            )
        else :
            return AuthenticationDocumentSpec(
                user_id = 'asdfghjklmn123',
                org_id = 'asdfghjklmn123',
        )

    def testAuthenticationDocumentSpec(self):
        """Test AuthenticationDocumentSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
