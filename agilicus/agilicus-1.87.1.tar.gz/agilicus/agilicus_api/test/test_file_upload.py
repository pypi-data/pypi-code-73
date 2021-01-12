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
from agilicus_api.models.file_upload import FileUpload  # noqa: E501
from agilicus_api.rest import ApiException

class TestFileUpload(unittest.TestCase):
    """FileUpload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileUpload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.file_upload.FileUpload()  # noqa: E501
        if include_optional :
            return FileUpload(
                org_id = '123', 
                tag = 'theme', 
                label = '0', 
                region = 'ca', 
                name = 'Alice', 
                visibility = 'private', 
                md5_hash = '0', 
                file_zip = bytes(b'blah')
            )
        else :
            return FileUpload(
                name = 'Alice',
                file_zip = bytes(b'blah'),
        )

    def testFileUpload(self):
        """Test FileUpload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
