# coding: utf-8

"""
    Process Registry API

    Register processes with the Process Registry API.

    OpenAPI spec version: 0.1.8
    
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

from pprint import pformat
from six import iteritems
import re


class ProcessDefPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProcessDefPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'logo_url': 'str',
            'description': 'str',
            'string_parameters': 'str',
            'file_parameters': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'logo_url': 'logo_url',
            'description': 'description',
            'string_parameters': 'string_parameters',
            'file_parameters': 'file_parameters'
        }

        self._name = None
        self._logo_url = None
        self._description = None
        self._string_parameters = None
        self._file_parameters = None

    @property
    def name(self):
        """
        Gets the name of this ProcessDefPost.
        Name given to the process definition

        :return: The name of this ProcessDefPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProcessDefPost.
        Name given to the process definition

        :param name: The name of this ProcessDefPost.
        :type: str
        """
        
        self._name = name

    @property
    def logo_url(self):
        """
        Gets the logo_url of this ProcessDefPost.
        URL to a logo image

        :return: The logo_url of this ProcessDefPost.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this ProcessDefPost.
        URL to a logo image

        :param logo_url: The logo_url of this ProcessDefPost.
        :type: str
        """
        
        self._logo_url = logo_url

    @property
    def description(self):
        """
        Gets the description of this ProcessDefPost.
        Textual description of the semantics of the process

        :return: The description of this ProcessDefPost.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProcessDefPost.
        Textual description of the semantics of the process

        :param description: The description of this ProcessDefPost.
        :type: str
        """
        
        self._description = description

    @property
    def string_parameters(self):
        """
        Gets the string_parameters of this ProcessDefPost.
        JSON-formatted array (treated as a set) giving the list of string parameters of the process

        :return: The string_parameters of this ProcessDefPost.
        :rtype: str
        """
        return self._string_parameters

    @string_parameters.setter
    def string_parameters(self, string_parameters):
        """
        Sets the string_parameters of this ProcessDefPost.
        JSON-formatted array (treated as a set) giving the list of string parameters of the process

        :param string_parameters: The string_parameters of this ProcessDefPost.
        :type: str
        """
        
        self._string_parameters = string_parameters

    @property
    def file_parameters(self):
        """
        Gets the file_parameters of this ProcessDefPost.
        JSON-formatted array (treated as a set) giving the list of file parameters of the process

        :return: The file_parameters of this ProcessDefPost.
        :rtype: str
        """
        return self._file_parameters

    @file_parameters.setter
    def file_parameters(self, file_parameters):
        """
        Sets the file_parameters of this ProcessDefPost.
        JSON-formatted array (treated as a set) giving the list of file parameters of the process

        :param file_parameters: The file_parameters of this ProcessDefPost.
        :type: str
        """
        
        self._file_parameters = file_parameters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

