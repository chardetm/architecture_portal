# coding: utf-8

"""
    Process Dispatcher API

    Execute processes with the Process Dispatcher API.

    OpenAPI spec version: 0.1.2
    
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


class Execution(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Execution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'author': 'int',
            'process_instance': 'int',
            'callback_url': 'str',
            'creation_date': 'datetime',
            'status': 'str',
            'status_info': 'str',
            'resource_provisioner_token': 'str',
            'output_location': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'author': 'author',
            'process_instance': 'process_instance',
            'callback_url': 'callback_url',
            'creation_date': 'creation_date',
            'status': 'status',
            'status_info': 'status_info',
            'resource_provisioner_token': 'resource_provisioner_token',
            'output_location': 'output_location'
        }

        self._id = None
        self._author = None
        self._process_instance = None
        self._callback_url = None
        self._creation_date = None
        self._status = None
        self._status_info = None
        self._resource_provisioner_token = None
        self._output_location = None

    @property
    def id(self):
        """
        Gets the id of this Execution.
        Unique identifier representing a specific execution

        :return: The id of this Execution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Execution.
        Unique identifier representing a specific execution

        :param id: The id of this Execution.
        :type: int
        """
        
        self._id = id

    @property
    def author(self):
        """
        Gets the author of this Execution.
        Unique ID of the user who created the execution

        :return: The author of this Execution.
        :rtype: int
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this Execution.
        Unique ID of the user who created the execution

        :param author: The author of this Execution.
        :type: int
        """
        
        self._author = author

    @property
    def process_instance(self):
        """
        Gets the process_instance of this Execution.
        Unique ID of the process instance this execution is of

        :return: The process_instance of this Execution.
        :rtype: int
        """
        return self._process_instance

    @process_instance.setter
    def process_instance(self, process_instance):
        """
        Sets the process_instance of this Execution.
        Unique ID of the process instance this execution is of

        :param process_instance: The process_instance of this Execution.
        :type: int
        """
        
        self._process_instance = process_instance

    @property
    def callback_url(self):
        """
        Gets the callback_url of this Execution.
        URL called after completion of the job (possibly empty)

        :return: The callback_url of this Execution.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this Execution.
        URL called after completion of the job (possibly empty)

        :param callback_url: The callback_url of this Execution.
        :type: str
        """
        
        self._callback_url = callback_url

    @property
    def creation_date(self):
        """
        Gets the creation_date of this Execution.
        Date and time of creation of the execution

        :return: The creation_date of this Execution.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this Execution.
        Date and time of creation of the execution

        :param creation_date: The creation_date of this Execution.
        :type: datetime
        """
        
        self._creation_date = creation_date

    @property
    def status(self):
        """
        Gets the status of this Execution.
        Status of the cluster

        :return: The status of this Execution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Execution.
        Status of the cluster

        :param status: The status of this Execution.
        :type: str
        """
        
        self._status = status

    @property
    def status_info(self):
        """
        Gets the status_info of this Execution.
        More information about the status of the cluster

        :return: The status_info of this Execution.
        :rtype: str
        """
        return self._status_info

    @status_info.setter
    def status_info(self, status_info):
        """
        Sets the status_info of this Execution.
        More information about the status of the cluster

        :param status_info: The status_info of this Execution.
        :type: str
        """
        
        self._status_info = status_info

    @property
    def resource_provisioner_token(self):
        """
        Gets the resource_provisioner_token of this Execution.
        Authentication token to be used to connect to the Resource Provisioner

        :return: The resource_provisioner_token of this Execution.
        :rtype: str
        """
        return self._resource_provisioner_token

    @resource_provisioner_token.setter
    def resource_provisioner_token(self, resource_provisioner_token):
        """
        Sets the resource_provisioner_token of this Execution.
        Authentication token to be used to connect to the Resource Provisioner

        :param resource_provisioner_token: The resource_provisioner_token of this Execution.
        :type: str
        """
        
        self._resource_provisioner_token = resource_provisioner_token

    @property
    def output_location(self):
        """
        Gets the output_location of this Execution.
        Location of the output file of the job on the machine, empty if not yet completed

        :return: The output_location of this Execution.
        :rtype: str
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this Execution.
        Location of the output file of the job on the machine, empty if not yet completed

        :param output_location: The output_location of this Execution.
        :type: str
        """
        
        self._output_location = output_location

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

