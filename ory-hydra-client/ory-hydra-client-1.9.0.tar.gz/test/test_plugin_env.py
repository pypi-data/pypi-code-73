# coding: utf-8

"""
    ORY Hydra

    Welcome to the ORY Hydra HTTP API documentation. You will find documentation for all HTTP APIs here.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ory_hydra_client
from ory_hydra_client.models.plugin_env import PluginEnv  # noqa: E501
from ory_hydra_client.rest import ApiException

class TestPluginEnv(unittest.TestCase):
    """PluginEnv unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PluginEnv
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_hydra_client.models.plugin_env.PluginEnv()  # noqa: E501
        if include_optional :
            return PluginEnv(
                description = '0', 
                name = '0', 
                settable = [
                    '0'
                    ], 
                value = '0'
            )
        else :
            return PluginEnv(
                description = '0',
                name = '0',
                settable = [
                    '0'
                    ],
                value = '0',
        )

    def testPluginEnv(self):
        """Test PluginEnv"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
