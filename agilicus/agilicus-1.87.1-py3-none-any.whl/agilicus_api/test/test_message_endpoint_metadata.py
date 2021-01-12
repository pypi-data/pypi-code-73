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
from agilicus_api.models.message_endpoint_metadata import MessageEndpointMetadata  # noqa: E501
from agilicus_api.rest import ApiException

class TestMessageEndpointMetadata(unittest.TestCase):
    """MessageEndpointMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageEndpointMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.message_endpoint_metadata.MessageEndpointMetadata()  # noqa: E501
        if include_optional :
            return MessageEndpointMetadata(
                message_endpoint_id = '123', 
                user_id = '123', 
                created = '2015-07-07T15:49:51.230+02:00', 
                updated = '2015-07-07T15:49:51.230+02:00'
            )
        else :
            return MessageEndpointMetadata(
        )

    def testMessageEndpointMetadata(self):
        """Test MessageEndpointMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
