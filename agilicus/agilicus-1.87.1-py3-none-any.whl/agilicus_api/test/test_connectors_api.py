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

import agilicus_api
from agilicus_api.api.connectors_api import ConnectorsApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestConnectorsApi(unittest.TestCase):
    """ConnectorsApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.connectors_api.ConnectorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_agent_connector(self):
        """Test case for create_agent_connector

        Create an agent connector  # noqa: E501
        """
        pass

    def test_delete_agent_connector(self):
        """Test case for delete_agent_connector

        Delete a agent  # noqa: E501
        """
        pass

    def test_get_agent_connector(self):
        """Test case for get_agent_connector

        Get an agent  # noqa: E501
        """
        pass

    def test_get_agent_info(self):
        """Test case for get_agent_info

        Get information associated with connector  # noqa: E501
        """
        pass

    def test_get_connector(self):
        """Test case for get_connector

        Get a connector  # noqa: E501
        """
        pass

    def test_list_agent_connector(self):
        """Test case for list_agent_connector

        list agent connectors  # noqa: E501
        """
        pass

    def test_list_connector(self):
        """Test case for list_connector

        List connectors  # noqa: E501
        """
        pass

    def test_replace_agent_connector(self):
        """Test case for replace_agent_connector

        Update an agent  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
