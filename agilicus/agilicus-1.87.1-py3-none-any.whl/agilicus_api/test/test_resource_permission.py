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
from agilicus_api.models.resource_permission import ResourcePermission  # noqa: E501
from agilicus_api.rest import ApiException

class TestResourcePermission(unittest.TestCase):
    """ResourcePermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResourcePermission
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.resource_permission.ResourcePermission()  # noqa: E501
        if include_optional :
            return ResourcePermission(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.resource_permission_spec.ResourcePermissionSpec(
                    user_id = '549sSkfdsksakSKD40', 
                    org_id = 'IAsl3dl40aSsfLKiU76', 
                    resource_id = 's9df932aSFl48sazZ4', 
                    resource_type = 'fileshare', 
                    resource_role_id = 'fileshare', )
            )
        else :
            return ResourcePermission(
                spec = agilicus_api.models.resource_permission_spec.ResourcePermissionSpec(
                    user_id = '549sSkfdsksakSKD40', 
                    org_id = 'IAsl3dl40aSsfLKiU76', 
                    resource_id = 's9df932aSFl48sazZ4', 
                    resource_type = 'fileshare', 
                    resource_role_id = 'fileshare', ),
        )

    def testResourcePermission(self):
        """Test ResourcePermission"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
