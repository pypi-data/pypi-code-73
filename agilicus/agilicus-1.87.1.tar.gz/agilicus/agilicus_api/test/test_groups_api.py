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
from agilicus_api.api.groups_api import GroupsApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.groups_api.GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group_member(self):
        """Test case for add_group_member

        Add a group member  # noqa: E501
        """
        pass

    def test_create_group(self):
        """Test case for create_group

        Create a group  # noqa: E501
        """
        pass

    def test_delete_group(self):
        """Test case for delete_group

        Delete a group  # noqa: E501
        """
        pass

    def test_delete_group_member(self):
        """Test case for delete_group_member

        Remove a group member  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get a group  # noqa: E501
        """
        pass

    def test_list_groups(self):
        """Test case for list_groups

        Get all groups  # noqa: E501
        """
        pass

    def test_replace_group(self):
        """Test case for replace_group

        update a group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
