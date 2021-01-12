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
from agilicus_api.models.list_authentication_document_response import ListAuthenticationDocumentResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListAuthenticationDocumentResponse(unittest.TestCase):
    """ListAuthenticationDocumentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListAuthenticationDocumentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_authentication_document_response.ListAuthenticationDocumentResponse()  # noqa: E501
        if include_optional :
            return ListAuthenticationDocumentResponse(
                authentication_documents = [
                    agilicus_api.models.authentication_document.AuthenticationDocument(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.authentication_document_spec.AuthenticationDocumentSpec(
                            user_id = 'asdfghjklmn123', 
                            org_id = 'asdfghjklmn123', 
                            auth_issuer_url = 'https://auth.cloud.egov.city', 
                            expiry = '2002-10-02T10:00-05:00', ), 
                        status = agilicus_api.models.authentication_document_status.AuthenticationDocumentStatus(
                            issuer = 'urn:agilicus:authentication_document:abc123', 
                            audience = 'urn:agilicus:api:tokens', 
                            key = '-----BEGIN PRIVATE KEY-----\nActualKeyContents\n-----END PRIVATE KEY-----\n', ), )
                    ], 
                limit = 56
            )
        else :
            return ListAuthenticationDocumentResponse(
                authentication_documents = [
                    agilicus_api.models.authentication_document.AuthenticationDocument(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.authentication_document_spec.AuthenticationDocumentSpec(
                            user_id = 'asdfghjklmn123', 
                            org_id = 'asdfghjklmn123', 
                            auth_issuer_url = 'https://auth.cloud.egov.city', 
                            expiry = '2002-10-02T10:00-05:00', ), 
                        status = agilicus_api.models.authentication_document_status.AuthenticationDocumentStatus(
                            issuer = 'urn:agilicus:authentication_document:abc123', 
                            audience = 'urn:agilicus:api:tokens', 
                            key = '-----BEGIN PRIVATE KEY-----\nActualKeyContents\n-----END PRIVATE KEY-----\n', ), )
                    ],
                limit = 56,
        )

    def testListAuthenticationDocumentResponse(self):
        """Test ListAuthenticationDocumentResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
