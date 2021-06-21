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


class SettingRights(object):
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
        'can_edit_settings': 'bool',
        'can_view_settings': 'bool'
    }

    attribute_map = {
        'can_edit_settings': 'canEditSettings',
        'can_view_settings': 'canViewSettings'
    }

    def __init__(self, can_edit_settings=None, can_view_settings=None):  # noqa: E501
        """SettingRights - a model defined in Swagger"""  # noqa: E501

        self._can_edit_settings = None
        self._can_view_settings = None
        self.discriminator = None

        if can_edit_settings is not None:
            self.can_edit_settings = can_edit_settings
        if can_view_settings is not None:
            self.can_view_settings = can_view_settings

    @property
    def can_edit_settings(self):
        """Gets the can_edit_settings of this SettingRights.  # noqa: E501

        Right to edit settings.  # noqa: E501

        :return: The can_edit_settings of this SettingRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_settings

    @can_edit_settings.setter
    def can_edit_settings(self, can_edit_settings):
        """Sets the can_edit_settings of this SettingRights.

        Right to edit settings.  # noqa: E501

        :param can_edit_settings: The can_edit_settings of this SettingRights.  # noqa: E501
        :type: bool
        """

        self._can_edit_settings = can_edit_settings

    @property
    def can_view_settings(self):
        """Gets the can_view_settings of this SettingRights.  # noqa: E501

        Right to view settings.  # noqa: E501

        :return: The can_view_settings of this SettingRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_settings

    @can_view_settings.setter
    def can_view_settings(self, can_view_settings):
        """Sets the can_view_settings of this SettingRights.

        Right to view settings.  # noqa: E501

        :param can_view_settings: The can_view_settings of this SettingRights.  # noqa: E501
        :type: bool
        """

        self._can_view_settings = can_view_settings

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
        if issubclass(SettingRights, dict):
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
        if not isinstance(other, SettingRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

