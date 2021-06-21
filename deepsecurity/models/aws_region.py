# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2021 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.424
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AWSRegion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'region': 'str',
        'computers_synced': 'int',
        'workspaces_synced': 'int'
    }

    attribute_map = {
        'region': 'region',
        'computers_synced': 'computersSynced',
        'workspaces_synced': 'workspacesSynced'
    }

    def __init__(self, region=None, computers_synced=None, workspaces_synced=None):  # noqa: E501
        """AWSRegion - a model defined in Swagger"""  # noqa: E501

        self._region = None
        self._computers_synced = None
        self._workspaces_synced = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if computers_synced is not None:
            self.computers_synced = computers_synced
        if workspaces_synced is not None:
            self.workspaces_synced = workspaces_synced

    @property
    def region(self):
        """Gets the region of this AWSRegion.  # noqa: E501

        The Amazon region name.  # noqa: E501

        :return: The region of this AWSRegion.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AWSRegion.

        The Amazon region name.  # noqa: E501

        :param region: The region of this AWSRegion.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def computers_synced(self):
        """Gets the computers_synced of this AWSRegion.  # noqa: E501

        The number of instances in the region during the last sync.  # noqa: E501

        :return: The computers_synced of this AWSRegion.  # noqa: E501
        :rtype: int
        """
        return self._computers_synced

    @computers_synced.setter
    def computers_synced(self, computers_synced):
        """Sets the computers_synced of this AWSRegion.

        The number of instances in the region during the last sync.  # noqa: E501

        :param computers_synced: The computers_synced of this AWSRegion.  # noqa: E501
        :type: int
        """

        self._computers_synced = computers_synced

    @property
    def workspaces_synced(self):
        """Gets the workspaces_synced of this AWSRegion.  # noqa: E501

        The number of workspaces in the region during the last sync.  # noqa: E501

        :return: The workspaces_synced of this AWSRegion.  # noqa: E501
        :rtype: int
        """
        return self._workspaces_synced

    @workspaces_synced.setter
    def workspaces_synced(self, workspaces_synced):
        """Sets the workspaces_synced of this AWSRegion.

        The number of workspaces in the region during the last sync.  # noqa: E501

        :param workspaces_synced: The workspaces_synced of this AWSRegion.  # noqa: E501
        :type: int
        """

        self._workspaces_synced = workspaces_synced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AWSRegion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AWSRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

