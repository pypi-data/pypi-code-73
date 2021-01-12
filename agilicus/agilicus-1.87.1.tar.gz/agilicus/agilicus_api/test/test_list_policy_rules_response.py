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
from agilicus_api.models.list_policy_rules_response import ListPolicyRulesResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListPolicyRulesResponse(unittest.TestCase):
    """ListPolicyRulesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListPolicyRulesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_policy_rules_response.ListPolicyRulesResponse()  # noqa: E501
        if include_optional :
            return ListPolicyRulesResponse(
                policy_rules = [
                    agilicus_api.models.policy_rule.PolicyRule(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.policy_rule_spec.PolicyRuleSpec(
                            name = 'blocked IPs rule', 
                            action = 'enroll', 
                            priority = 1, 
                            org_id = 'asdfg123hjkl', 
                            conditions = [
                                agilicus_api.models.policy_condition.PolicyCondition(
                                    condition_type = 'type_client_id_list', 
                                    inverted = True, 
                                    input_is_list = True, 
                                    value = 'my-city-org', 
                                    operator = 'equals', 
                                    field = 'clients.name', 
                                    created = '2015-07-07T15:49:51.230+02:00', 
                                    updated = '2015-07-07T15:49:51.230+02:00', )
                                ], ), )
                    ], 
                limit = 56
            )
        else :
            return ListPolicyRulesResponse(
                policy_rules = [
                    agilicus_api.models.policy_rule.PolicyRule(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.policy_rule_spec.PolicyRuleSpec(
                            name = 'blocked IPs rule', 
                            action = 'enroll', 
                            priority = 1, 
                            org_id = 'asdfg123hjkl', 
                            conditions = [
                                agilicus_api.models.policy_condition.PolicyCondition(
                                    condition_type = 'type_client_id_list', 
                                    inverted = True, 
                                    input_is_list = True, 
                                    value = 'my-city-org', 
                                    operator = 'equals', 
                                    field = 'clients.name', 
                                    created = '2015-07-07T15:49:51.230+02:00', 
                                    updated = '2015-07-07T15:49:51.230+02:00', )
                                ], ), )
                    ],
                limit = 56,
        )

    def testListPolicyRulesResponse(self):
        """Test ListPolicyRulesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
