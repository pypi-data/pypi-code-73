# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.01.11
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from agilicus_api.api_client import ApiClient
from agilicus_api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DiagnosticsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_logs(self, org_id, **kwargs):  # noqa: E501
        """Retrieve application logs  # noqa: E501

        Retrieve application diagnostic logs. These are the output from stdout/stderr (stream).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_logs(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str org_id: query for a specific organization (required)
        :param str dt_from: search criteria, search logs from
        :param str dt_to: search criteria, search logs to
        :param str app: search criteria, search logs for an app
        :param str sub: search criteria, search logs for a given subject (USER) GUID
        :param int limit: limit number of output logs
        :param str sub_org_id: query for a specific sub-organization
        :param str env: query for a specific environment
        :param str dt_sort: Sort order: *'asc' - ascending, from old to new logs *'desc' - descending, from new to old logs 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_logs_with_http_info(org_id, **kwargs)  # noqa: E501

    def list_logs_with_http_info(self, org_id, **kwargs):  # noqa: E501
        """Retrieve application logs  # noqa: E501

        Retrieve application diagnostic logs. These are the output from stdout/stderr (stream).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_logs_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str org_id: query for a specific organization (required)
        :param str dt_from: search criteria, search logs from
        :param str dt_to: search criteria, search logs to
        :param str app: search criteria, search logs for an app
        :param str sub: search criteria, search logs for a given subject (USER) GUID
        :param int limit: limit number of output logs
        :param str sub_org_id: query for a specific sub-organization
        :param str env: query for a specific environment
        :param str dt_sort: Sort order: *'asc' - ascending, from old to new logs *'desc' - descending, from new to old logs 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListLogsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['org_id', 'dt_from', 'dt_to', 'app', 'sub', 'limit', 'sub_org_id', 'env', 'dt_sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'org_id' is set
        if self.api_client.client_side_validation and ('org_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['org_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `org_id` when calling `list_logs`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 500:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_logs`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org_id' in local_var_params and local_var_params['org_id'] is not None:  # noqa: E501
            query_params.append(('org_id', local_var_params['org_id']))  # noqa: E501
        if 'dt_from' in local_var_params and local_var_params['dt_from'] is not None:  # noqa: E501
            query_params.append(('dt_from', local_var_params['dt_from']))  # noqa: E501
        if 'dt_to' in local_var_params and local_var_params['dt_to'] is not None:  # noqa: E501
            query_params.append(('dt_to', local_var_params['dt_to']))  # noqa: E501
        if 'app' in local_var_params and local_var_params['app'] is not None:  # noqa: E501
            query_params.append(('app', local_var_params['app']))  # noqa: E501
        if 'sub' in local_var_params and local_var_params['sub'] is not None:  # noqa: E501
            query_params.append(('sub', local_var_params['sub']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'sub_org_id' in local_var_params and local_var_params['sub_org_id'] is not None:  # noqa: E501
            query_params.append(('sub_org_id', local_var_params['sub_org_id']))  # noqa: E501
        if 'env' in local_var_params and local_var_params['env'] is not None:  # noqa: E501
            query_params.append(('env', local_var_params['env']))  # noqa: E501
        if 'dt_sort' in local_var_params and local_var_params['dt_sort'] is not None:  # noqa: E501
            query_params.append(('dt_sort', local_var_params['dt_sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token-valid']  # noqa: E501

        return self.api_client.call_api(
            '/v1/diagnostics/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
