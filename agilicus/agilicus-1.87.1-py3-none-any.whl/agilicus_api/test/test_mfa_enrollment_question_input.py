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
from agilicus_api.models.mfa_enrollment_question_input import MFAEnrollmentQuestionInput  # noqa: E501
from agilicus_api.rest import ApiException

class TestMFAEnrollmentQuestionInput(unittest.TestCase):
    """MFAEnrollmentQuestionInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MFAEnrollmentQuestionInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.mfa_enrollment_question_input.MFAEnrollmentQuestionInput()  # noqa: E501
        if include_optional :
            return MFAEnrollmentQuestionInput(
                login_info = agilicus_api.models.mfa_enrollment_question_login_info.MFAEnrollmentQuestionLoginInfo(
                    issuer_org_id = 'absjfladasdf23', 
                    enrollment_expiry = '2015-07-07T15:49:51.230+02:00', 
                    user_mfa_methods = ["totp","webauthn"], )
            )
        else :
            return MFAEnrollmentQuestionInput(
                login_info = agilicus_api.models.mfa_enrollment_question_login_info.MFAEnrollmentQuestionLoginInfo(
                    issuer_org_id = 'absjfladasdf23', 
                    enrollment_expiry = '2015-07-07T15:49:51.230+02:00', 
                    user_mfa_methods = ["totp","webauthn"], ),
        )

    def testMFAEnrollmentQuestionInput(self):
        """Test MFAEnrollmentQuestionInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
