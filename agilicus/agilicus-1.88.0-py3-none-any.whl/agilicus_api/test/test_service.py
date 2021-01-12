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
from agilicus_api.models.service import Service  # noqa: E501
from agilicus_api.rest import ApiException

class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Service
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.service.Service()  # noqa: E501
        if include_optional :
            return Service(
                created = '2015-07-07T15:49:51.230+02:00', 
                id = '123', 
                name = '0', 
                description = '0', 
                org_id = '0', 
                contact_email = '0', 
                roles = [
                    agilicus_api.models.role.Role(
                        name = '0', 
                        rules = [
                            agilicus_api.models.rule.Rule(
                                host = '0', 
                                name = 'rules.add', 
                                method = 'get', 
                                path = '/.*', 
                                query_parameters = [
                                    agilicus_api.models.rule_query_parameter.RuleQueryParameter(
                                        name = '0', 
                                        exact_match = '0', )
                                    ], 
                                body = agilicus_api.models.rule_query_body.RuleQueryBody(
                                    json = [
                                        agilicus_api.models.rule_query_body_json.RuleQueryBodyJSON(
                                            name = '0', 
                                            exact_match = '0', 
                                            match_type = 'string', 
                                            pointer = '/foo/0/a~1b/2', )
                                        ], ), )
                            ], )
                    ], 
                definitions = [
                    agilicus_api.models.definition.Definition(
                        key = '0', 
                        value = '0', )
                    ], 
                base_url = 'api.agilicus.com/v1', 
                updated = '2015-07-07T15:49:51.230+02:00'
            )
        else :
            return Service(
                name = '0',
                org_id = '0',
                base_url = 'api.agilicus.com/v1',
        )

    def testService(self):
        """Test Service"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
