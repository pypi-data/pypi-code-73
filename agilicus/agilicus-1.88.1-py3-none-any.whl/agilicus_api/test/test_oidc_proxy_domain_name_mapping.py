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
from agilicus_api.models.oidc_proxy_domain_name_mapping import OIDCProxyDomainNameMapping  # noqa: E501
from agilicus_api.rest import ApiException

class TestOIDCProxyDomainNameMapping(unittest.TestCase):
    """OIDCProxyDomainNameMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OIDCProxyDomainNameMapping
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.oidc_proxy_domain_name_mapping.OIDCProxyDomainNameMapping()  # noqa: E501
        if include_optional :
            return OIDCProxyDomainNameMapping(
                internal_name = 'local_test_app', 
                external_name = 'app-1'
            )
        else :
            return OIDCProxyDomainNameMapping(
                internal_name = 'local_test_app',
        )

    def testOIDCProxyDomainNameMapping(self):
        """Test OIDCProxyDomainNameMapping"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
