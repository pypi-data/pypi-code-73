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
from agilicus_api.api.catalogues_api import CataloguesApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestCataloguesApi(unittest.TestCase):
    """CataloguesApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.catalogues_api.CataloguesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_catalogue(self):
        """Test case for create_catalogue

        create a catalogue  # noqa: E501
        """
        pass

    def test_create_catalogue_entry(self):
        """Test case for create_catalogue_entry

        create a catalogue entry  # noqa: E501
        """
        pass

    def test_delete_catalogue(self):
        """Test case for delete_catalogue

        Delete the catalogue specified by catalogue_id  # noqa: E501
        """
        pass

    def test_delete_catalogue_entry(self):
        """Test case for delete_catalogue_entry

        Delete the catalogue specified by catalogue_entry_id  # noqa: E501
        """
        pass

    def test_get_catalogue(self):
        """Test case for get_catalogue

        Get the catalogue specified by catalogue_id  # noqa: E501
        """
        pass

    def test_get_catalogue_entry(self):
        """Test case for get_catalogue_entry

        Get the catalogue entry by id for the given catalogue  # noqa: E501
        """
        pass

    def test_list_all_catalogue_entries(self):
        """Test case for list_all_catalogue_entries

        List all catalogue entries independant of the catalogue they belong to  # noqa: E501
        """
        pass

    def test_list_catalogue_entries(self):
        """Test case for list_catalogue_entries

        List catalogue entries in the catalogue  # noqa: E501
        """
        pass

    def test_list_catalogues(self):
        """Test case for list_catalogues

        List all catalogues  # noqa: E501
        """
        pass

    def test_replace_catalogue(self):
        """Test case for replace_catalogue

        Replace the catalogue specified by catalogue_id  # noqa: E501
        """
        pass

    def test_replace_catalogue_entry(self):
        """Test case for replace_catalogue_entry

        Replace the catalogue entry specified by catalogue_entry_id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
