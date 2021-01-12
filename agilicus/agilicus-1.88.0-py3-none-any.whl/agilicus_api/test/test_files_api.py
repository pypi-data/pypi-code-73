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

import agilicus_api
from agilicus_api.api.files_api import FilesApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestFilesApi(unittest.TestCase):
    """FilesApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.files_api.FilesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_file(self):
        """Test case for add_file

        upload a file  # noqa: E501
        """
        pass

    def test_delete_file(self):
        """Test case for delete_file

        Delete a File  # noqa: E501
        """
        pass

    def test_get_download(self):
        """Test case for get_download

        Download File  # noqa: E501
        """
        pass

    def test_get_file(self):
        """Test case for get_file

        Get File metadata  # noqa: E501
        """
        pass

    def test_list_files(self):
        """Test case for list_files

        Query Files  # noqa: E501
        """
        pass

    def test_replace_file(self):
        """Test case for replace_file

        Update a file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
