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
from agilicus_api.api.services_api import ServicesApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.services_api.ServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service(self):
        """Test case for create_service

        Create a Service  # noqa: E501
        """
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Remove a Service  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Get a single Service  # noqa: E501
        """
        pass

    def test_list_services(self):
        """Test case for list_services

        Get a subset of the Services  # noqa: E501
        """
        pass

    def test_replace_service(self):
        """Test case for replace_service

        Create or update a Service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
