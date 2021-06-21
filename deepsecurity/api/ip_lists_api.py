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


class IPListsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_ip_list(self, ip_list, api_version, **kwargs):  # noqa: E501
        """Create an IP List  # noqa: E501

        Create a new IP list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ip_list(ip_list, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IpList ip_list: The settings of the new IP list. (required)
        :param str api_version: The version of the api being called. (required)
        :return: IpList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_ip_list_with_http_info(ip_list, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_ip_list_with_http_info(ip_list, api_version, **kwargs)  # noqa: E501
            return data

    def create_ip_list_with_http_info(self, ip_list, api_version, **kwargs):  # noqa: E501
        """Create an IP List  # noqa: E501

        Create a new IP list.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ip_list_with_http_info(ip_list, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IpList ip_list: The settings of the new IP list. (required)
        :param str api_version: The version of the api being called. (required)
        :return: IpList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip_list', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ip_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip_list' is set
        if ('ip_list' not in params or
                params['ip_list'] is None):
            raise ValueError("Missing the required parameter `ip_list` when calling `create_ip_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_ip_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ip_list' in params:
            body_params = params['ip_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/iplists', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_ip_list(self, ip_list_id, api_version, **kwargs):  # noqa: E501
        """Delete an IP List  # noqa: E501

        Delete an IP list by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ip_list(ip_list_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip_list_id: The ID number of the IP list to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_ip_list_with_http_info(ip_list_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_ip_list_with_http_info(ip_list_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_ip_list_with_http_info(self, ip_list_id, api_version, **kwargs):  # noqa: E501
        """Delete an IP List  # noqa: E501

        Delete an IP list by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_ip_list_with_http_info(ip_list_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip_list_id: The ID number of the IP list to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip_list_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ip_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip_list_id' is set
        if ('ip_list_id' not in params or
                params['ip_list_id'] is None):
            raise ValueError("Missing the required parameter `ip_list_id` when calling `delete_ip_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_ip_list`")  # noqa: E501

        if 'ip_list_id' in params and not re.search('\\d+', str(params['ip_list_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `ip_list_id` when calling `delete_ip_list`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ip_list_id' in params:
            path_params['ipListID'] = params['ip_list_id']  # noqa: E501

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
            '/iplists/{ipListID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_ip_list(self, ip_list_id, api_version, **kwargs):  # noqa: E501
        """Describe an IP List  # noqa: E501

        Describe an IP list by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_ip_list(ip_list_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip_list_id: The ID number of the IP list to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: IpList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_ip_list_with_http_info(ip_list_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_ip_list_with_http_info(ip_list_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_ip_list_with_http_info(self, ip_list_id, api_version, **kwargs):  # noqa: E501
        """Describe an IP List  # noqa: E501

        Describe an IP list by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_ip_list_with_http_info(ip_list_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip_list_id: The ID number of the IP list to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: IpList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip_list_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_ip_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip_list_id' is set
        if ('ip_list_id' not in params or
                params['ip_list_id'] is None):
            raise ValueError("Missing the required parameter `ip_list_id` when calling `describe_ip_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_ip_list`")  # noqa: E501

        if 'ip_list_id' in params and not re.search('\\d+', str(params['ip_list_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `ip_list_id` when calling `describe_ip_list`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ip_list_id' in params:
            path_params['ipListID'] = params['ip_list_id']  # noqa: E501

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
            '/iplists/{ipListID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_ip_lists(self, api_version, **kwargs):  # noqa: E501
        """List IP Lists  # noqa: E501

        Lists all IP lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ip_lists(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: IpLists
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_ip_lists_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_ip_lists_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_ip_lists_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List IP Lists  # noqa: E501

        Lists all IP lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_ip_lists_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: IpLists
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ip_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_ip_lists`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/iplists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpLists',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_ip_list(self, ip_list_id, ip_list, api_version, **kwargs):  # noqa: E501
        """Modify an IP List  # noqa: E501

        Modify an IP list by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_ip_list(ip_list_id, ip_list, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip_list_id: The ID number of the IP list to modify. (required)
        :param IpList ip_list: The settings of the IP list to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: IpList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_ip_list_with_http_info(ip_list_id, ip_list, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_ip_list_with_http_info(ip_list_id, ip_list, api_version, **kwargs)  # noqa: E501
            return data

    def modify_ip_list_with_http_info(self, ip_list_id, ip_list, api_version, **kwargs):  # noqa: E501
        """Modify an IP List  # noqa: E501

        Modify an IP list by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_ip_list_with_http_info(ip_list_id, ip_list, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ip_list_id: The ID number of the IP list to modify. (required)
        :param IpList ip_list: The settings of the IP list to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: IpList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip_list_id', 'ip_list', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_ip_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip_list_id' is set
        if ('ip_list_id' not in params or
                params['ip_list_id'] is None):
            raise ValueError("Missing the required parameter `ip_list_id` when calling `modify_ip_list`")  # noqa: E501
        # verify the required parameter 'ip_list' is set
        if ('ip_list' not in params or
                params['ip_list'] is None):
            raise ValueError("Missing the required parameter `ip_list` when calling `modify_ip_list`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_ip_list`")  # noqa: E501

        if 'ip_list_id' in params and not re.search('\\d+', str(params['ip_list_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `ip_list_id` when calling `modify_ip_list`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ip_list_id' in params:
            path_params['ipListID'] = params['ip_list_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ip_list' in params:
            body_params = params['ip_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/iplists/{ipListID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_ip_lists(self, api_version, **kwargs):  # noqa: E501
        """Search IP Lists  # noqa: E501

        Search for IP lists using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ip_lists(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: IpLists
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_ip_lists_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_ip_lists_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_ip_lists_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search IP Lists  # noqa: E501

        Search for IP lists using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_ip_lists_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: IpLists
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_ip_lists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_ip_lists`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/iplists/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpLists',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
