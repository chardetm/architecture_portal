# coding: utf-8

"""
    Appliance Registry API

    Store appliances with the Appliance Registry API.

    OpenAPI spec version: 0.1.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ScriptsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def scripts_appliance_action_get(self, appliance, action, **kwargs):
        """
        Get the script corresponding to an appliance and an action.
        Get the script corresponding to an appliance and an action. Authentification is not required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_appliance_action_get(appliance, action, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str appliance: Name of the appliance (required)
        :param str action: Name of the action (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['appliance', 'action']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_appliance_action_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'appliance' is set
        if ('appliance' not in params) or (params['appliance'] is None):
            raise ValueError("Missing the required parameter `appliance` when calling `scripts_appliance_action_get`")
        # verify the required parameter 'action' is set
        if ('action' not in params) or (params['action'] is None):
            raise ValueError("Missing the required parameter `action` when calling `scripts_appliance_action_get`")


        resource_path = '/scripts/{appliance}/{action}/'.replace('{format}', 'json')
        path_params = {}
        if 'appliance' in params:
            path_params['appliance'] = params['appliance']
        if 'action' in params:
            path_params['action'] = params['action']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Script',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scripts_get(self, **kwargs):
        """
        Get the list of all the scripts registered.
        Get the list of all the scripts registered. No authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[Script]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_get" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/scripts/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Script]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scripts_id_delete(self, id, **kwargs):
        """
        Delete an already existing script.
        Delete an already existing script. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id of the script (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `scripts_id_delete`")

        if 'id' in params and params['id'] < 0.0: 
            raise ValueError("Invalid value for parameter `id` when calling `scripts_id_delete`, must be a value greater than or equal to `0.0`")

        resource_path = '/scripts/{id}/'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scripts_id_get(self, id, **kwargs):
        """
        Get a single script.
        Get a single script. Authentification is not required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_id_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id of the script (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_id_get" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `scripts_id_get`")

        if 'id' in params and params['id'] < 0.0: 
            raise ValueError("Invalid value for parameter `id` when calling `scripts_id_get`, must be a value greater than or equal to `0.0`")

        resource_path = '/scripts/{id}/'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Script',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scripts_id_patch(self, id, data, **kwargs):
        """
        Modify an already existing script.
        Modify an already existing script. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_id_patch(id, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id of the script (required)
        :param ScriptPatch data: Script (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_id_patch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `scripts_id_patch`")
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `scripts_id_patch`")

        if 'id' in params and params['id'] < 0.0: 
            raise ValueError("Invalid value for parameter `id` when calling `scripts_id_patch`, must be a value greater than or equal to `0.0`")

        resource_path = '/scripts/{id}/'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Script',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scripts_id_put(self, id, data, **kwargs):
        """
        Redefine an already existing script.
        Redefine an already existing script. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_id_put(id, data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Id of the script (required)
        :param ScriptPost data: Script (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_id_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `scripts_id_put`")
        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `scripts_id_put`")

        if 'id' in params and params['id'] < 0.0: 
            raise ValueError("Invalid value for parameter `id` when calling `scripts_id_put`, must be a value greater than or equal to `0.0`")

        resource_path = '/scripts/{id}/'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Script',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def scripts_post(self, data, **kwargs):
        """
        Add a new script.
        Add a new script. Authentification is required. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.scripts_post(data, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ScriptPost data: Script (required)
        :return: Script
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method scripts_post" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'data' is set
        if ('data' not in params) or (params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `scripts_post`")


        resource_path = '/scripts/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key', 'basic']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Script',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
