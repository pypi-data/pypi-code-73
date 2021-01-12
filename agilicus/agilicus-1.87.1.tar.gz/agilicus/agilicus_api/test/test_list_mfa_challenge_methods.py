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
from agilicus_api.models.list_mfa_challenge_methods import ListMFAChallengeMethods  # noqa: E501
from agilicus_api.rest import ApiException

class TestListMFAChallengeMethods(unittest.TestCase):
    """ListMFAChallengeMethods unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListMFAChallengeMethods
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_mfa_challenge_methods.ListMFAChallengeMethods()  # noqa: E501
        if include_optional :
            return ListMFAChallengeMethods(
                mfa_challenge_methods = [
                    agilicus_api.models.mfa_challenge_method.MFAChallengeMethod(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.mfa_challenge_method_spec.MFAChallengeMethodSpec(
                            priority = 1, 
                            challenge_type = '0', 
                            endpoint = '0', 
                            nickname = '0', 
                            enabled = True, ), )
                    ], 
                limit = 56
            )
        else :
            return ListMFAChallengeMethods(
                limit = 56,
        )

    def testListMFAChallengeMethods(self):
        """Test ListMFAChallengeMethods"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
