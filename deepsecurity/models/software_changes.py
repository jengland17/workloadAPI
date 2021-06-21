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

from deepsecurity.models.software_change import SoftwareChange  # noqa: F401,E501


class SoftwareChanges(object):
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
        'software_changes': 'list[SoftwareChange]'
    }

    attribute_map = {
        'software_changes': 'softwareChanges'
    }

    def __init__(self, software_changes=None):  # noqa: E501
        """SoftwareChanges - a model defined in Swagger"""  # noqa: E501

        self._software_changes = None
        self.discriminator = None

        if software_changes is not None:
            self.software_changes = software_changes

    @property
    def software_changes(self):
        """Gets the software_changes of this SoftwareChanges.  # noqa: E501


        :return: The software_changes of this SoftwareChanges.  # noqa: E501
        :rtype: list[SoftwareChange]
        """
        return self._software_changes

    @software_changes.setter
    def software_changes(self, software_changes):
        """Sets the software_changes of this SoftwareChanges.


        :param software_changes: The software_changes of this SoftwareChanges.  # noqa: E501
        :type: list[SoftwareChange]
        """

        self._software_changes = software_changes

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
        if issubclass(SoftwareChanges, dict):
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
        if not isinstance(other, SoftwareChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

