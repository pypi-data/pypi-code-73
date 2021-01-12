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
from agilicus_api.models.oidc_proxy_header_override import OIDCProxyHeaderOverride  # noqa: E501
from agilicus_api.rest import ApiException

class TestOIDCProxyHeaderOverride(unittest.TestCase):
    """OIDCProxyHeaderOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OIDCProxyHeaderOverride
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.oidc_proxy_header_override.OIDCProxyHeaderOverride()  # noqa: E501
        if include_optional :
            return OIDCProxyHeaderOverride(
                request = agilicus_api.models.oidc_proxy_header_user_config.OIDCProxyHeaderUserConfig(
                    set = [
                        agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                            name = 'Accept-Encoding', 
                            value = '*', )
                        ], 
                    add = [
                        agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                            name = 'Accept-Encoding', 
                            value = '*', )
                        ], 
                    remove = [
                        agilicus_api.models.oidc_proxy_header_name.OIDCProxyHeaderName(
                            name = '0', )
                        ], ), 
                response = agilicus_api.models.oidc_proxy_header_user_config.OIDCProxyHeaderUserConfig(
                    set = [
                        agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                            name = 'Accept-Encoding', 
                            value = '*', )
                        ], 
                    add = [
                        agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                            name = 'Accept-Encoding', 
                            value = '*', )
                        ], 
                    remove = [
                        agilicus_api.models.oidc_proxy_header_name.OIDCProxyHeaderName(
                            name = '0', )
                        ], )
            )
        else :
            return OIDCProxyHeaderOverride(
        )

    def testOIDCProxyHeaderOverride(self):
        """Test OIDCProxyHeaderOverride"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
