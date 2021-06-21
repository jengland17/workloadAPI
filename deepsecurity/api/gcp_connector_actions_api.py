# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2021 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.424
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class GCPConnectorActionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_gcp_connector_action(self, gcp_connector_id, gcp_connector_action, api_version, **kwargs):  # noqa: E501
        """Create a connector action  # noqa: E501

        Create a connector action by connector ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gcp_connector_action(gcp_connector_id, gcp_connector_action, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gcp_connector_id: The ID number of the GCP Connector. (required)
        :param Action gcp_connector_action: The property of the new GCP Connector action. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Action
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_gcp_connector_action_with_http_info(gcp_connector_id, gcp_connector_action, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_gcp_connector_action_with_http_info(gcp_connector_id, gcp_connector_action, api_version, **kwargs)  # noqa: E501
            return data

    def create_gcp_connector_action_with_http_info(self, gcp_connector_id, gcp_connector_action, api_version, **kwargs):  # noqa: E501
        """Create a connector action  # noqa: E501

        Create a connector action by connector ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_gcp_connector_action_with_http_info(gcp_connector_id, gcp_connector_action, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gcp_connector_id: The ID number of the GCP Connector. (required)
        :param Action gcp_connector_action: The property of the new GCP Connector action. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Action
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gcp_connector_id', 'gcp_connector_action', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_gcp_connector_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gcp_connector_id' is set
        if ('gcp_connector_id' not in params or
                params['gcp_connector_id'] is None):
            raise ValueError("Missing the required parameter `gcp_connector_id` when calling `create_gcp_connector_action`")  # noqa: E501
        # verify the required parameter 'gcp_connector_action' is set
        if ('gcp_connector_action' not in params or
                params['gcp_connector_action'] is None):
            raise ValueError("Missing the required parameter `gcp_connector_action` when calling `create_gcp_connector_action`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_gcp_connector_action`")  # noqa: E501

        if 'gcp_connector_id' in params and not re.search('\\d+', str(params['gcp_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `gcp_connector_id` when calling `create_gcp_connector_action`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'gcp_connector_id' in params:
            path_params['gcpConnectorID'] = params['gcp_connector_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'gcp_connector_action' in params:
            body_params = params['gcp_connector_action']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/gcpconnectors/{gcpConnectorID}/actions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Action',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_gcp_connector_action(self, gcp_connector_id, action_id, api_version, **kwargs):  # noqa: E501
        """Describe a connector action  # noqa: E501

        Describe a connector action by connector ID and action ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_gcp_connector_action(gcp_connector_id, action_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gcp_connector_id: The ID number of the GCP Connector. (required)
        :param int action_id: The ID number of the GCP Connector action. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Action
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_gcp_connector_action_with_http_info(gcp_connector_id, action_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_gcp_connector_action_with_http_info(gcp_connector_id, action_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_gcp_connector_action_with_http_info(self, gcp_connector_id, action_id, api_version, **kwargs):  # noqa: E501
        """Describe a connector action  # noqa: E501

        Describe a connector action by connector ID and action ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_gcp_connector_action_with_http_info(gcp_connector_id, action_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int gcp_connector_id: The ID number of the GCP Connector. (required)
        :param int action_id: The ID number of the GCP Connector action. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Action
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gcp_connector_id', 'action_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_gcp_connector_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gcp_connector_id' is set
        if ('gcp_connector_id' not in params or
                params['gcp_connector_id'] is None):
            raise ValueError("Missing the required parameter `gcp_connector_id` when calling `describe_gcp_connector_action`")  # noqa: E501
        # verify the required parameter 'action_id' is set
        if ('action_id' not in params or
                params['action_id'] is None):
            raise ValueError("Missing the required parameter `action_id` when calling `describe_gcp_connector_action`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_gcp_connector_action`")  # noqa: E501

        if 'gcp_connector_id' in params and not re.search('\\d+', str(params['gcp_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `gcp_connector_id` when calling `describe_gcp_connector_action`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'action_id' in params and not re.search('\\d+', str(params['action_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `action_id` when calling `describe_gcp_connector_action`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'gcp_connector_id' in params:
            path_params['gcpConnectorID'] = params['gcp_connector_id']  # noqa: E501
        if 'action_id' in params:
            path_params['actionID'] = params['action_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/gcpconnectors/{gcpConnectorID}/actions/{actionID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Action',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)