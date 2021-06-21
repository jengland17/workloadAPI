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


class InterfaceType(object):
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
        'name': 'str',
        'description': 'str',
        'matches': 'list[str]',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'matches': 'matches',
        'id': 'ID'
    }

    def __init__(self, name=None, description=None, matches=None, id=None):  # noqa: E501
        """InterfaceType - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._matches = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if matches is not None:
            self.matches = matches
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this InterfaceType.  # noqa: E501

        Name of the InterfaceType. Searchable as String.  # noqa: E501

        :return: The name of this InterfaceType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InterfaceType.

        Name of the InterfaceType. Searchable as String.  # noqa: E501

        :param name: The name of this InterfaceType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this InterfaceType.  # noqa: E501

        Description of the InterfaceType. Searchable as String.  # noqa: E501

        :return: The description of this InterfaceType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InterfaceType.

        Description of the InterfaceType. Searchable as String.  # noqa: E501

        :param description: The description of this InterfaceType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def matches(self):
        """Gets the matches of this InterfaceType.  # noqa: E501

        String patterns to match with Interface names and display names. One pattern per line. The `*` character can be used for wildcard matches. Searchable as String.  # noqa: E501

        :return: The matches of this InterfaceType.  # noqa: E501
        :rtype: list[str]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this InterfaceType.

        String patterns to match with Interface names and display names. One pattern per line. The `*` character can be used for wildcard matches. Searchable as String.  # noqa: E501

        :param matches: The matches of this InterfaceType.  # noqa: E501
        :type: list[str]
        """

        self._matches = matches

    @property
    def id(self):
        """Gets the id of this InterfaceType.  # noqa: E501

        ID of the InterfaceType. Searchable as ID.  # noqa: E501

        :return: The id of this InterfaceType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterfaceType.

        ID of the InterfaceType. Searchable as ID.  # noqa: E501

        :param id: The id of this InterfaceType.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(InterfaceType, dict):
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
        if not isinstance(other, InterfaceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

