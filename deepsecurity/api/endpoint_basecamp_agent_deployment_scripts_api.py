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


class EndpointBasecampAgentDeploymentScriptsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def generate_endpoint_basecamp_agent_deployment_script(self, api_version, **kwargs):  # noqa: E501
        """Generate Endpoint Basecamp Agent Deployment Scripts  # noqa: E501

        Generate Endpoint Basecamp Agent deployment scripts by platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_endpoint_basecamp_agent_deployment_script(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param EndpointBasecampAgentDeploymentScript endpoint_basecamp_agent_deployment_script: The platform type for the Endpoint Basecamp Agent.
        :return: EndpointBasecampAgentDeploymentScript
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_endpoint_basecamp_agent_deployment_script_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_endpoint_basecamp_agent_deployment_script_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def generate_endpoint_basecamp_agent_deployment_script_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Generate Endpoint Basecamp Agent Deployment Scripts  # noqa: E501

        Generate Endpoint Basecamp Agent deployment scripts by platform.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_endpoint_basecamp_agent_deployment_script_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param EndpointBasecampAgentDeploymentScript endpoint_basecamp_agent_deployment_script: The platform type for the Endpoint Basecamp Agent.
        :return: EndpointBasecampAgentDeploymentScript
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'endpoint_basecamp_agent_deployment_script']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_endpoint_basecamp_agent_deployment_script" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `generate_endpoint_basecamp_agent_deployment_script`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'endpoint_basecamp_agent_deployment_script' in params:
            body_params = params['endpoint_basecamp_agent_deployment_script']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/endpointbasecampagentdeploymentscripts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EndpointBasecampAgentDeploymentScript',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
