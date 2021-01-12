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
import datetime

import agilicus_api
from agilicus_api.models.policy_group import PolicyGroup  # noqa: E501
from agilicus_api.rest import ApiException

class TestPolicyGroup(unittest.TestCase):
    """PolicyGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PolicyGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.policy_group.PolicyGroup()  # noqa: E501
        if include_optional :
            return PolicyGroup(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.policy_group_spec.PolicyGroupSpec(
                    name = '0', 
                    rule_ids = [
                        '123'
                        ], )
            )
        else :
            return PolicyGroup(
                spec = agilicus_api.models.policy_group_spec.PolicyGroupSpec(
                    name = '0', 
                    rule_ids = [
                        '123'
                        ], ),
        )

    def testPolicyGroup(self):
        """Test PolicyGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
