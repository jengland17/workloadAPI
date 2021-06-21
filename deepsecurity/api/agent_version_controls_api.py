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


class AgentVersionControlsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def describe_agent_version_control(self, agent_version_control_profile_id, agent_version_control_id, api_version, **kwargs):  # noqa: E501
        """Describe an agent version control  # noqa: E501

        Describe an Agent Version Control by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_agent_version_control(agent_version_control_profile_id, agent_version_control_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param int agent_version_control_id: The ID number of the agent version control to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AgentVersionControl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_agent_version_control_with_http_info(agent_version_control_profile_id, agent_version_control_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_agent_version_control_with_http_info(agent_version_control_profile_id, agent_version_control_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_agent_version_control_with_http_info(self, agent_version_control_profile_id, agent_version_control_id, api_version, **kwargs):  # noqa: E501
        """Describe an agent version control  # noqa: E501

        Describe an Agent Version Control by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_agent_version_control_with_http_info(agent_version_control_profile_id, agent_version_control_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param int agent_version_control_id: The ID number of the agent version control to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AgentVersionControl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_version_control_profile_id', 'agent_version_control_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_agent_version_control" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_version_control_profile_id' is set
        if ('agent_version_control_profile_id' not in params or
                params['agent_version_control_profile_id'] is None):
            raise ValueError("Missing the required parameter `agent_version_control_profile_id` when calling `describe_agent_version_control`")  # noqa: E501
        # verify the required parameter 'agent_version_control_id' is set
        if ('agent_version_control_id' not in params or
                params['agent_version_control_id'] is None):
            raise ValueError("Missing the required parameter `agent_version_control_id` when calling `describe_agent_version_control`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_agent_version_control`")  # noqa: E501

        if 'agent_version_control_profile_id' in params and not re.search('\\d+', str(params['agent_version_control_profile_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `agent_version_control_profile_id` when calling `describe_agent_version_control`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'agent_version_control_id' in params and not re.search('\\d+', str(params['agent_version_control_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `agent_version_control_id` when calling `describe_agent_version_control`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'agent_version_control_profile_id' in params:
            path_params['agentVersionControlProfileID'] = params['agent_version_control_profile_id']  # noqa: E501
        if 'agent_version_control_id' in params:
            path_params['agentVersionControlID'] = params['agent_version_control_id']  # noqa: E501

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
            '/agentversioncontrolprofiles/{agentVersionControlProfileID}/agentversioncontrols/{agentVersionControlID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AgentVersionControl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_agent_version_controls(self, agent_version_control_profile_id, api_version, **kwargs):  # noqa: E501
        """List agent version controls  # noqa: E501

        Lists all agent version controls.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_agent_version_controls(agent_version_control_profile_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AgentVersionControls
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_agent_version_controls_with_http_info(agent_version_control_profile_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_agent_version_controls_with_http_info(agent_version_control_profile_id, api_version, **kwargs)  # noqa: E501
            return data

    def list_agent_version_controls_with_http_info(self, agent_version_control_profile_id, api_version, **kwargs):  # noqa: E501
        """List agent version controls  # noqa: E501

        Lists all agent version controls.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_agent_version_controls_with_http_info(agent_version_control_profile_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AgentVersionControls
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_version_control_profile_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_agent_version_controls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_version_control_profile_id' is set
        if ('agent_version_control_profile_id' not in params or
                params['agent_version_control_profile_id'] is None):
            raise ValueError("Missing the required parameter `agent_version_control_profile_id` when calling `list_agent_version_controls`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_agent_version_controls`")  # noqa: E501

        if 'agent_version_control_profile_id' in params and not re.search('\\d+', str(params['agent_version_control_profile_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `agent_version_control_profile_id` when calling `list_agent_version_controls`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'agent_version_control_profile_id' in params:
            path_params['agentVersionControlProfileID'] = params['agent_version_control_profile_id']  # noqa: E501

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
            '/agentversioncontrolprofiles/{agentVersionControlProfileID}/agentversioncontrols', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AgentVersionControls',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_agent_version_controls(self, agent_version_control_profile_id, agent_version_controls, api_version, **kwargs):  # noqa: E501
        """Modify agent version controls  # noqa: E501

        Modify the agent version controls. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_agent_version_controls(agent_version_control_profile_id, agent_version_controls, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param AgentVersionControls agent_version_controls: The agent version controls to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AgentVersionControls
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_agent_version_controls_with_http_info(agent_version_control_profile_id, agent_version_controls, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_agent_version_controls_with_http_info(agent_version_control_profile_id, agent_version_controls, api_version, **kwargs)  # noqa: E501
            return data

    def modify_agent_version_controls_with_http_info(self, agent_version_control_profile_id, agent_version_controls, api_version, **kwargs):  # noqa: E501
        """Modify agent version controls  # noqa: E501

        Modify the agent version controls. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_agent_version_controls_with_http_info(agent_version_control_profile_id, agent_version_controls, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param AgentVersionControls agent_version_controls: The agent version controls to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AgentVersionControls
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_version_control_profile_id', 'agent_version_controls', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_agent_version_controls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_version_control_profile_id' is set
        if ('agent_version_control_profile_id' not in params or
                params['agent_version_control_profile_id'] is None):
            raise ValueError("Missing the required parameter `agent_version_control_profile_id` when calling `modify_agent_version_controls`")  # noqa: E501
        # verify the required parameter 'agent_version_controls' is set
        if ('agent_version_controls' not in params or
                params['agent_version_controls'] is None):
            raise ValueError("Missing the required parameter `agent_version_controls` when calling `modify_agent_version_controls`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_agent_version_controls`")  # noqa: E501

        if 'agent_version_control_profile_id' in params and not re.search('\\d+', str(params['agent_version_control_profile_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `agent_version_control_profile_id` when calling `modify_agent_version_controls`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'agent_version_control_profile_id' in params:
            path_params['agentVersionControlProfileID'] = params['agent_version_control_profile_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'agent_version_controls' in params:
            body_params = params['agent_version_controls']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/agentversioncontrolprofiles/{agentVersionControlProfileID}/agentversioncontrols', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AgentVersionControls',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_agent_version_controls(self, agent_version_control_profile_id, api_version, **kwargs):  # noqa: E501
        """Search agent version controls  # noqa: E501

        Search for agent version controls using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_agent_version_controls(agent_version_control_profile_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AgentVersionControls
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_agent_version_controls_with_http_info(agent_version_control_profile_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_agent_version_controls_with_http_info(agent_version_control_profile_id, api_version, **kwargs)  # noqa: E501
            return data

    def search_agent_version_controls_with_http_info(self, agent_version_control_profile_id, api_version, **kwargs):  # noqa: E501
        """Search agent version controls  # noqa: E501

        Search for agent version controls using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_agent_version_controls_with_http_info(agent_version_control_profile_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int agent_version_control_profile_id: The ID number of the agent version control profile. (required)
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AgentVersionControls
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_version_control_profile_id', 'api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_agent_version_controls" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_version_control_profile_id' is set
        if ('agent_version_control_profile_id' not in params or
                params['agent_version_control_profile_id'] is None):
            raise ValueError("Missing the required parameter `agent_version_control_profile_id` when calling `search_agent_version_controls`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_agent_version_controls`")  # noqa: E501

        if 'agent_version_control_profile_id' in params and not re.search('\\d+', str(params['agent_version_control_profile_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `agent_version_control_profile_id` when calling `search_agent_version_controls`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'agent_version_control_profile_id' in params:
            path_params['agentVersionControlProfileID'] = params['agent_version_control_profile_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/agentversioncontrolprofiles/{agentVersionControlProfileID}/agentversioncontrols/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AgentVersionControls',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
