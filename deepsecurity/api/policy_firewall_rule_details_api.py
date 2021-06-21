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


class PolicyFirewallRuleDetailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def describe_firewall_rule_on_policy(self, policy_id, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe a firewall rule  # noqa: E501

        Describe a firewall rule including policy-level overrides.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_firewall_rule_on_policy(policy_id, firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int firewall_rule_id: The ID number of the firewall rule. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_firewall_rule_on_policy_with_http_info(self, policy_id, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe a firewall rule  # noqa: E501

        Describe a firewall rule including policy-level overrides.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int firewall_rule_id: The ID number of the firewall rule. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'firewall_rule_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_firewall_rule_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `describe_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'firewall_rule_id' is set
        if ('firewall_rule_id' not in params or
                params['firewall_rule_id'] is None):
            raise ValueError("Missing the required parameter `firewall_rule_id` when calling `describe_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_firewall_rule_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `describe_firewall_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'firewall_rule_id' in params and not re.search('\\d+', str(params['firewall_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `firewall_rule_id` when calling `describe_firewall_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'firewall_rule_id' in params:
            path_params['firewallRuleID'] = params['firewall_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

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
            '/policies/{policyID}/firewall/rules/{firewallRuleID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_firewall_rules_on_policy(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List firewall rules  # noqa: E501

        Lists all firewall rules assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_firewall_rules_on_policy(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only rules assigned to the current policy.
        :return: FirewallRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_firewall_rules_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_firewall_rules_on_policy_with_http_info(policy_id, api_version, **kwargs)  # noqa: E501
            return data

    def list_firewall_rules_on_policy_with_http_info(self, policy_id, api_version, **kwargs):  # noqa: E501
        """List firewall rules  # noqa: E501

        Lists all firewall rules assigned to a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_firewall_rules_on_policy_with_http_info(policy_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only rules assigned to the current policy.
        :return: FirewallRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_firewall_rules_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `list_firewall_rules_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_firewall_rules_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `list_firewall_rules_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

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
            '/policies/{policyID}/firewall/rules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_firewall_rule_on_policy(self, policy_id, firewall_rule_id, firewall_rule, api_version, **kwargs):  # noqa: E501
        """Modify a firewall rule  # noqa: E501

        Modify a firewall rule assigned to a policy. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_firewall_rule_on_policy(policy_id, firewall_rule_id, firewall_rule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int firewall_rule_id: The ID number of the firewall rule to modify. (required)
        :param FirewallRule firewall_rule: The settings of the firewall rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, firewall_rule, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, firewall_rule, api_version, **kwargs)  # noqa: E501
            return data

    def modify_firewall_rule_on_policy_with_http_info(self, policy_id, firewall_rule_id, firewall_rule, api_version, **kwargs):  # noqa: E501
        """Modify a firewall rule  # noqa: E501

        Modify a firewall rule assigned to a policy. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, firewall_rule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int firewall_rule_id: The ID number of the firewall rule to modify. (required)
        :param FirewallRule firewall_rule: The settings of the firewall rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'firewall_rule_id', 'firewall_rule', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_firewall_rule_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `modify_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'firewall_rule_id' is set
        if ('firewall_rule_id' not in params or
                params['firewall_rule_id'] is None):
            raise ValueError("Missing the required parameter `firewall_rule_id` when calling `modify_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'firewall_rule' is set
        if ('firewall_rule' not in params or
                params['firewall_rule'] is None):
            raise ValueError("Missing the required parameter `firewall_rule` when calling `modify_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_firewall_rule_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `modify_firewall_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'firewall_rule_id' in params and not re.search('\\d+', str(params['firewall_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `firewall_rule_id` when calling `modify_firewall_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'firewall_rule_id' in params:
            path_params['firewallRuleID'] = params['firewall_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'firewall_rule' in params:
            body_params = params['firewall_rule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/policies/{policyID}/firewall/rules/{firewallRuleID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reset_firewall_rule_on_policy(self, policy_id, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Reset firewall rule overrides  # noqa: E501

        Remove all overrides for a firewall rule from a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_firewall_rule_on_policy(policy_id, firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int firewall_rule_id: The ID number of the firewall rule to reset. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reset_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.reset_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def reset_firewall_rule_on_policy_with_http_info(self, policy_id, firewall_rule_id, api_version, **kwargs):  # noqa: E501
        """Reset firewall rule overrides  # noqa: E501

        Remove all overrides for a firewall rule from a policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reset_firewall_rule_on_policy_with_http_info(policy_id, firewall_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int policy_id: The ID number of the policy. (required)
        :param int firewall_rule_id: The ID number of the firewall rule to reset. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current policy.
        :return: FirewallRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'firewall_rule_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reset_firewall_rule_on_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `reset_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'firewall_rule_id' is set
        if ('firewall_rule_id' not in params or
                params['firewall_rule_id'] is None):
            raise ValueError("Missing the required parameter `firewall_rule_id` when calling `reset_firewall_rule_on_policy`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `reset_firewall_rule_on_policy`")  # noqa: E501

        if 'policy_id' in params and not re.search('\\d+', str(params['policy_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `policy_id` when calling `reset_firewall_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        if 'firewall_rule_id' in params and not re.search('\\d+', str(params['firewall_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `firewall_rule_id` when calling `reset_firewall_rule_on_policy`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyID'] = params['policy_id']  # noqa: E501
        if 'firewall_rule_id' in params:
            path_params['firewallRuleID'] = params['firewall_rule_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

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
            '/policies/{policyID}/firewall/rules/{firewallRuleID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirewallRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
