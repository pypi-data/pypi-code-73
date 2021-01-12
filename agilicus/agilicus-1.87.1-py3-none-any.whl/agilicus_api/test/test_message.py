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
from agilicus_api.models.message import Message  # noqa: E501
from agilicus_api.rest import ApiException

class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Message
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.message.Message()  # noqa: E501
        if include_optional :
            return Message(
                id = '123', 
                title = '0', 
                sub_header = '0', 
                icon = '0', 
                image = '0', 
                text = '0', 
                uri = '0', 
                context = '0', 
                actions = [
                    agilicus_api.models.message_action.MessageAction(
                        title = '0', 
                        uri = '0', 
                        icon = '0', )
                    ]
            )
        else :
            return Message(
                text = '0',
        )

    def testMessage(self):
        """Test Message"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
