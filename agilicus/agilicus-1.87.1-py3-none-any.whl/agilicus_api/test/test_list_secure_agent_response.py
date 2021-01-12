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
from agilicus_api.models.list_secure_agent_response import ListSecureAgentResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListSecureAgentResponse(unittest.TestCase):
    """ListSecureAgentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListSecureAgentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_secure_agent_response.ListSecureAgentResponse()  # noqa: E501
        if include_optional :
            return ListSecureAgentResponse(
                secure_agents = [
                    agilicus_api.models.secure_agent.SecureAgent(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.secure_agent_spec.SecureAgentSpec(
                            name = '0', 
                            org_id = '123', 
                            application_service_ids = [
                                '123'
                                ], 
                            connectors = [
                                agilicus_api.models.secure_agent_connector.SecureAgentConnector(
                                    max_number_connections = 0, 
                                    connection_uri = '0', )
                                ], ), 
                        status = agilicus_api.models.secure_agent_status.SecureAgentStatus(
                            application_services = [
                                agilicus_api.models.application_service.ApplicationService(
                                    created = '2015-07-07T15:49:51.230+02:00', 
                                    id = '123', 
                                    name = '0', 
                                    org_id = '0', 
                                    hostname = 'db.example.com', 
                                    ipv4_addresses = [
                                        '192.0.2.1'
                                        ], 
                                    name_resolution = 'static', 
                                    port = 56, 
                                    protocol = 'tcp', 
                                    assignments = [
                                        agilicus_api.models.application_service_assignment.ApplicationServiceAssignment(
                                            app_id = '0', 
                                            environment_name = '0', 
                                            org_id = '0', )
                                        ], 
                                    updated = '2015-07-07T15:49:51.230+02:00', 
                                    service_type = 'vpn', 
                                    service_protocol_type = 'ip', 
                                    connector_id = '123', )
                                ], 
                            connector_info = [
                                agilicus_api.models.secure_agent_connector_info.SecureAgentConnectorInfo(
                                    connection_uri = '0', 
                                    max_number_connections = 0, )
                                ], ), )
                    ], 
                limit = 56
            )
        else :
            return ListSecureAgentResponse(
                secure_agents = [
                    agilicus_api.models.secure_agent.SecureAgent(
                        metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                        spec = agilicus_api.models.secure_agent_spec.SecureAgentSpec(
                            name = '0', 
                            org_id = '123', 
                            application_service_ids = [
                                '123'
                                ], 
                            connectors = [
                                agilicus_api.models.secure_agent_connector.SecureAgentConnector(
                                    max_number_connections = 0, 
                                    connection_uri = '0', )
                                ], ), 
                        status = agilicus_api.models.secure_agent_status.SecureAgentStatus(
                            application_services = [
                                agilicus_api.models.application_service.ApplicationService(
                                    created = '2015-07-07T15:49:51.230+02:00', 
                                    id = '123', 
                                    name = '0', 
                                    org_id = '0', 
                                    hostname = 'db.example.com', 
                                    ipv4_addresses = [
                                        '192.0.2.1'
                                        ], 
                                    name_resolution = 'static', 
                                    port = 56, 
                                    protocol = 'tcp', 
                                    assignments = [
                                        agilicus_api.models.application_service_assignment.ApplicationServiceAssignment(
                                            app_id = '0', 
                                            environment_name = '0', 
                                            org_id = '0', )
                                        ], 
                                    updated = '2015-07-07T15:49:51.230+02:00', 
                                    service_type = 'vpn', 
                                    service_protocol_type = 'ip', 
                                    connector_id = '123', )
                                ], 
                            connector_info = [
                                agilicus_api.models.secure_agent_connector_info.SecureAgentConnectorInfo(
                                    connection_uri = '0', 
                                    max_number_connections = 0, )
                                ], ), )
                    ],
                limit = 56,
        )

    def testListSecureAgentResponse(self):
        """Test ListSecureAgentResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
