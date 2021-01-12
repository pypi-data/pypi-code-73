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
from agilicus_api.models.list_well_known_issuer_info import ListWellKnownIssuerInfo  # noqa: E501
from agilicus_api.rest import ApiException

class TestListWellKnownIssuerInfo(unittest.TestCase):
    """ListWellKnownIssuerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListWellKnownIssuerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_well_known_issuer_info.ListWellKnownIssuerInfo()  # noqa: E501
        if include_optional :
            return ListWellKnownIssuerInfo(
                well_known_info = [
                    agilicus_api.models.well_known_issuer_info.WellKnownIssuerInfo(
                        issuer_id = '123', 
                        supported_mfa_methods = ["totp","webauthn"], )
                    ], 
                limit = 56
            )
        else :
            return ListWellKnownIssuerInfo(
                limit = 56,
        )

    def testListWellKnownIssuerInfo(self):
        """Test ListWellKnownIssuerInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
