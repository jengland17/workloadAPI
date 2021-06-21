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


class ApiKeyRights(object):
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
        'can_create_new_api_keys': 'bool',
        'can_delete_api_keys': 'bool',
        'can_edit_api_key_properties': 'bool',
        'can_view_api_keys': 'bool'
    }

    attribute_map = {
        'can_create_new_api_keys': 'canCreateNewApiKeys',
        'can_delete_api_keys': 'canDeleteApiKeys',
        'can_edit_api_key_properties': 'canEditApiKeyProperties',
        'can_view_api_keys': 'canViewApiKeys'
    }

    def __init__(self, can_create_new_api_keys=None, can_delete_api_keys=None, can_edit_api_key_properties=None, can_view_api_keys=None):  # noqa: E501
        """ApiKeyRights - a model defined in Swagger"""  # noqa: E501

        self._can_create_new_api_keys = None
        self._can_delete_api_keys = None
        self._can_edit_api_key_properties = None
        self._can_view_api_keys = None
        self.discriminator = None

        if can_create_new_api_keys is not None:
            self.can_create_new_api_keys = can_create_new_api_keys
        if can_delete_api_keys is not None:
            self.can_delete_api_keys = can_delete_api_keys
        if can_edit_api_key_properties is not None:
            self.can_edit_api_key_properties = can_edit_api_key_properties
        if can_view_api_keys is not None:
            self.can_view_api_keys = can_view_api_keys

    @property
    def can_create_new_api_keys(self):
        """Gets the can_create_new_api_keys of this ApiKeyRights.  # noqa: E501

        Right to create new api keys.  # noqa: E501

        :return: The can_create_new_api_keys of this ApiKeyRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_new_api_keys

    @can_create_new_api_keys.setter
    def can_create_new_api_keys(self, can_create_new_api_keys):
        """Sets the can_create_new_api_keys of this ApiKeyRights.

        Right to create new api keys.  # noqa: E501

        :param can_create_new_api_keys: The can_create_new_api_keys of this ApiKeyRights.  # noqa: E501
        :type: bool
        """

        self._can_create_new_api_keys = can_create_new_api_keys

    @property
    def can_delete_api_keys(self):
        """Gets the can_delete_api_keys of this ApiKeyRights.  # noqa: E501

        Right to delete api keys.  # noqa: E501

        :return: The can_delete_api_keys of this ApiKeyRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_api_keys

    @can_delete_api_keys.setter
    def can_delete_api_keys(self, can_delete_api_keys):
        """Sets the can_delete_api_keys of this ApiKeyRights.

        Right to delete api keys.  # noqa: E501

        :param can_delete_api_keys: The can_delete_api_keys of this ApiKeyRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_api_keys = can_delete_api_keys

    @property
    def can_edit_api_key_properties(self):
        """Gets the can_edit_api_key_properties of this ApiKeyRights.  # noqa: E501

        Right to edit api keys.  # noqa: E501

        :return: The can_edit_api_key_properties of this ApiKeyRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_api_key_properties

    @can_edit_api_key_properties.setter
    def can_edit_api_key_properties(self, can_edit_api_key_properties):
        """Sets the can_edit_api_key_properties of this ApiKeyRights.

        Right to edit api keys.  # noqa: E501

        :param can_edit_api_key_properties: The can_edit_api_key_properties of this ApiKeyRights.  # noqa: E501
        :type: bool
        """

        self._can_edit_api_key_properties = can_edit_api_key_properties

    @property
    def can_view_api_keys(self):
        """Gets the can_view_api_keys of this ApiKeyRights.  # noqa: E501

        Right to view api keys.  # noqa: E501

        :return: The can_view_api_keys of this ApiKeyRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_api_keys

    @can_view_api_keys.setter
    def can_view_api_keys(self, can_view_api_keys):
        """Sets the can_view_api_keys of this ApiKeyRights.

        Right to view api keys.  # noqa: E501

        :param can_view_api_keys: The can_view_api_keys of this ApiKeyRights.  # noqa: E501
        :type: bool
        """

        self._can_view_api_keys = can_view_api_keys

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
        if issubclass(ApiKeyRights, dict):
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
        if not isinstance(other, ApiKeyRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

