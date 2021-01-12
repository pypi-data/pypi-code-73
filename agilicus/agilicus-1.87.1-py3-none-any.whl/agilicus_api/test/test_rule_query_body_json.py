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
from agilicus_api.models.rule_query_body_json import RuleQueryBodyJSON  # noqa: E501
from agilicus_api.rest import ApiException

class TestRuleQueryBodyJSON(unittest.TestCase):
    """RuleQueryBodyJSON unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RuleQueryBodyJSON
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.rule_query_body_json.RuleQueryBodyJSON()  # noqa: E501
        if include_optional :
            return RuleQueryBodyJSON(
                name = '0', 
                exact_match = '0', 
                match_type = 'string', 
                pointer = '/foo/0/a~1b/2'
            )
        else :
            return RuleQueryBodyJSON(
                name = '0',
        )

    def testRuleQueryBodyJSON(self):
        """Test RuleQueryBodyJSON"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
