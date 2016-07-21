# coding: utf-8

"""
    Resource provisioner API

    Provision Cloud Computing resources via API.

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


class Hosts(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Hosts - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'is_master': 'bool',
            'instance_ip': 'str',
            'cluster_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'is_master': 'is_master',
            'instance_ip': 'instance_ip',
            'cluster_id': 'cluster_id'
        }

        self._id = None
        self._name = None
        self._is_master = None
        self._instance_ip = None
        self._cluster_id = None

    @property
    def id(self):
        """
        Gets the id of this Hosts.
        Unique ID of the host

        :return: The id of this Hosts.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Hosts.
        Unique ID of the host

        :param id: The id of this Hosts.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Hosts.
        Name given to the host

        :return: The name of this Hosts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Hosts.
        Name given to the host

        :param name: The name of this Hosts.
        :type: str
        """
        
        self._name = name

    @property
    def is_master(self):
        """
        Gets the is_master of this Hosts.
        True if the host is a master_node

        :return: The is_master of this Hosts.
        :rtype: bool
        """
        return self._is_master

    @is_master.setter
    def is_master(self, is_master):
        """
        Sets the is_master of this Hosts.
        True if the host is a master_node

        :param is_master: The is_master of this Hosts.
        :type: bool
        """
        
        self._is_master = is_master

    @property
    def instance_ip(self):
        """
        Gets the instance_ip of this Hosts.
        IP address of the host

        :return: The instance_ip of this Hosts.
        :rtype: str
        """
        return self._instance_ip

    @instance_ip.setter
    def instance_ip(self, instance_ip):
        """
        Sets the instance_ip of this Hosts.
        IP address of the host

        :param instance_ip: The instance_ip of this Hosts.
        :type: str
        """
        
        self._instance_ip = instance_ip

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this Hosts.
        ID of the cluster

        :return: The cluster_id of this Hosts.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this Hosts.
        ID of the cluster

        :param cluster_id: The cluster_id of this Hosts.
        :type: int
        """
        
        self._cluster_id = cluster_id

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

