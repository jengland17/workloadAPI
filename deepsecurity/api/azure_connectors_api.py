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


class AzureConnectorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_azure_connector(self, azure_connector, api_version, **kwargs):  # noqa: E501
        """Create an Azure Connector  # noqa: E501

        Create a new Azure Connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_azure_connector(azure_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AzureConnector azure_connector: The settings of the new Azure Connector. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AzureConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_azure_connector_with_http_info(azure_connector, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_azure_connector_with_http_info(azure_connector, api_version, **kwargs)  # noqa: E501
            return data

    def create_azure_connector_with_http_info(self, azure_connector, api_version, **kwargs):  # noqa: E501
        """Create an Azure Connector  # noqa: E501

        Create a new Azure Connector.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_azure_connector_with_http_info(azure_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AzureConnector azure_connector: The settings of the new Azure Connector. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AzureConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_connector', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_azure_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_connector' is set
        if ('azure_connector' not in params or
                params['azure_connector'] is None):
            raise ValueError("Missing the required parameter `azure_connector` when calling `create_azure_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_azure_connector`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'azure_connector' in params:
            body_params = params['azure_connector']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/azureconnectors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AzureConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_azure_connector(self, azure_connector_id, api_version, **kwargs):  # noqa: E501
        """Delete an Azure Connector  # noqa: E501

        Delete an existing Azure Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_azure_connector(azure_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_connector_id: The ID number of the Azure Connector to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_azure_connector_with_http_info(azure_connector_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_azure_connector_with_http_info(azure_connector_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_azure_connector_with_http_info(self, azure_connector_id, api_version, **kwargs):  # noqa: E501
        """Delete an Azure Connector  # noqa: E501

        Delete an existing Azure Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_azure_connector_with_http_info(azure_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_connector_id: The ID number of the Azure Connector to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_connector_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_azure_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_connector_id' is set
        if ('azure_connector_id' not in params or
                params['azure_connector_id'] is None):
            raise ValueError("Missing the required parameter `azure_connector_id` when calling `delete_azure_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_azure_connector`")  # noqa: E501

        if 'azure_connector_id' in params and not re.search('\\d+', str(params['azure_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `azure_connector_id` when calling `delete_azure_connector`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'azure_connector_id' in params:
            path_params['azureConnectorID'] = params['azure_connector_id']  # noqa: E501

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
            '/azureconnectors/{azureConnectorID}', 'DELETE',
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

    def describe_azure_connector(self, azure_connector_id, api_version, **kwargs):  # noqa: E501
        """Describe an existing Azure Connector  # noqa: E501

        Describe an Azure Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_azure_connector(azure_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_connector_id: The ID number of the Azure Connector to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AzureConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_azure_connector_with_http_info(azure_connector_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_azure_connector_with_http_info(azure_connector_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_azure_connector_with_http_info(self, azure_connector_id, api_version, **kwargs):  # noqa: E501
        """Describe an existing Azure Connector  # noqa: E501

        Describe an Azure Connector by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_azure_connector_with_http_info(azure_connector_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_connector_id: The ID number of the Azure Connector to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: AzureConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_connector_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_azure_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_connector_id' is set
        if ('azure_connector_id' not in params or
                params['azure_connector_id'] is None):
            raise ValueError("Missing the required parameter `azure_connector_id` when calling `describe_azure_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_azure_connector`")  # noqa: E501

        if 'azure_connector_id' in params and not re.search('\\d+', str(params['azure_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `azure_connector_id` when calling `describe_azure_connector`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'azure_connector_id' in params:
            path_params['azureConnectorID'] = params['azure_connector_id']  # noqa: E501

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
            '/azureconnectors/{azureConnectorID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AzureConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_azure_connectors(self, api_version, **kwargs):  # noqa: E501
        """List Azure Connectors  # noqa: E501

        Lists all Azure Connectors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_azure_connectors(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: AzureConnectors
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_azure_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_azure_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_azure_connectors_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Azure Connectors  # noqa: E501

        Lists all Azure Connectors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_azure_connectors_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: AzureConnectors
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
                    " to method list_azure_connectors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_azure_connectors`")  # noqa: E501

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
            '/azureconnectors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AzureConnectors',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_azure_connector(self, azure_connector_id, azure_connector, api_version, **kwargs):  # noqa: E501
        """Modify an Azure Connector  # noqa: E501

        Modify the specified Azure Connector by ID. Any unset elements will be left unchanged. Property `azureTenantID`, `subscriptionID`, `loginApiEndPoint` and `resourceApiEndPoint` can't be modified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_azure_connector(azure_connector_id, azure_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_connector_id: The ID number of the Azure Connector to modify. (required)
        :param AzureConnector azure_connector: The settings of the Azure Connector to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool sync: Immediately trigger a synchronization for the Azure Connector.
        :return: AzureConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_azure_connector_with_http_info(azure_connector_id, azure_connector, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_azure_connector_with_http_info(azure_connector_id, azure_connector, api_version, **kwargs)  # noqa: E501
            return data

    def modify_azure_connector_with_http_info(self, azure_connector_id, azure_connector, api_version, **kwargs):  # noqa: E501
        """Modify an Azure Connector  # noqa: E501

        Modify the specified Azure Connector by ID. Any unset elements will be left unchanged. Property `azureTenantID`, `subscriptionID`, `loginApiEndPoint` and `resourceApiEndPoint` can't be modified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_azure_connector_with_http_info(azure_connector_id, azure_connector, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int azure_connector_id: The ID number of the Azure Connector to modify. (required)
        :param AzureConnector azure_connector: The settings of the Azure Connector to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool sync: Immediately trigger a synchronization for the Azure Connector.
        :return: AzureConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['azure_connector_id', 'azure_connector', 'api_version', 'sync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_azure_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'azure_connector_id' is set
        if ('azure_connector_id' not in params or
                params['azure_connector_id'] is None):
            raise ValueError("Missing the required parameter `azure_connector_id` when calling `modify_azure_connector`")  # noqa: E501
        # verify the required parameter 'azure_connector' is set
        if ('azure_connector' not in params or
                params['azure_connector'] is None):
            raise ValueError("Missing the required parameter `azure_connector` when calling `modify_azure_connector`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_azure_connector`")  # noqa: E501

        if 'azure_connector_id' in params and not re.search('\\d+', str(params['azure_connector_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `azure_connector_id` when calling `modify_azure_connector`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'azure_connector_id' in params:
            path_params['azureConnectorID'] = params['azure_connector_id']  # noqa: E501

        query_params = []
        if 'sync' in params:
            query_params.append(('sync', params['sync']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'azure_connector' in params:
            body_params = params['azure_connector']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/azureconnectors/{azureConnectorID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AzureConnector',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_azure_connectors(self, api_version, **kwargs):  # noqa: E501
        """Search Azure Connectors  # noqa: E501

        Search for Azure Connectors using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_azure_connectors(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AzureConnectors
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_azure_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_azure_connectors_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_azure_connectors_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Azure Connectors  # noqa: E501

        Search for Azure Connectors using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_azure_connectors_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: AzureConnectors
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
                    " to method search_azure_connectors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_azure_connectors`")  # noqa: E501

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
            '/azureconnectors/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AzureConnectors',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
