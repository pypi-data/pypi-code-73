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
from ory_hydra_client.models.plugin_settings import PluginSettings  # noqa: E501
from ory_hydra_client.rest import ApiException

class TestPluginSettings(unittest.TestCase):
    """PluginSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PluginSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ory_hydra_client.models.plugin_settings.PluginSettings()  # noqa: E501
        if include_optional :
            return PluginSettings(
                args = [
                    '0'
                    ], 
                devices = [
                    ory_hydra_client.models.plugin_device.PluginDevice(
                        description = '0', 
                        name = '0', 
                        path = '0', 
                        settable = [
                            '0'
                            ], )
                    ], 
                env = [
                    '0'
                    ], 
                mounts = [
                    ory_hydra_client.models.plugin_mount.PluginMount(
                        description = '0', 
                        destination = '0', 
                        name = '0', 
                        options = [
                            '0'
                            ], 
                        settable = [
                            '0'
                            ], 
                        source = '0', 
                        type = '0', )
                    ]
            )
        else :
            return PluginSettings(
                args = [
                    '0'
                    ],
                devices = [
                    ory_hydra_client.models.plugin_device.PluginDevice(
                        description = '0', 
                        name = '0', 
                        path = '0', 
                        settable = [
                            '0'
                            ], )
                    ],
                env = [
                    '0'
                    ],
                mounts = [
                    ory_hydra_client.models.plugin_mount.PluginMount(
                        description = '0', 
                        destination = '0', 
                        name = '0', 
                        options = [
                            '0'
                            ], 
                        settable = [
                            '0'
                            ], 
                        source = '0', 
                        type = '0', )
                    ],
        )

    def testPluginSettings(self):
        """Test PluginSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
