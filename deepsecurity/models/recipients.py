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


class Recipients(object):
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
        'all_administrators_and_contacts': 'bool',
        'administrator_ids': 'list[int]',
        'contact_ids': 'list[int]'
    }

    attribute_map = {
        'all_administrators_and_contacts': 'allAdministratorsAndContacts',
        'administrator_ids': 'administratorIDs',
        'contact_ids': 'contactIDs'
    }

    def __init__(self, all_administrators_and_contacts=None, administrator_ids=None, contact_ids=None):  # noqa: E501
        """Recipients - a model defined in Swagger"""  # noqa: E501

        self._all_administrators_and_contacts = None
        self._administrator_ids = None
        self._contact_ids = None
        self.discriminator = None

        if all_administrators_and_contacts is not None:
            self.all_administrators_and_contacts = all_administrators_and_contacts
        if administrator_ids is not None:
            self.administrator_ids = administrator_ids
        if contact_ids is not None:
            self.contact_ids = contact_ids

    @property
    def all_administrators_and_contacts(self):
        """Gets the all_administrators_and_contacts of this Recipients.  # noqa: E501

        Send to all administrators and contacts with a valid email address.  # noqa: E501

        :return: The all_administrators_and_contacts of this Recipients.  # noqa: E501
        :rtype: bool
        """
        return self._all_administrators_and_contacts

    @all_administrators_and_contacts.setter
    def all_administrators_and_contacts(self, all_administrators_and_contacts):
        """Sets the all_administrators_and_contacts of this Recipients.

        Send to all administrators and contacts with a valid email address.  # noqa: E501

        :param all_administrators_and_contacts: The all_administrators_and_contacts of this Recipients.  # noqa: E501
        :type: bool
        """

        self._all_administrators_and_contacts = all_administrators_and_contacts

    @property
    def administrator_ids(self):
        """Gets the administrator_ids of this Recipients.  # noqa: E501

        List of recipient administrators IDs.  # noqa: E501

        :return: The administrator_ids of this Recipients.  # noqa: E501
        :rtype: list[int]
        """
        return self._administrator_ids

    @administrator_ids.setter
    def administrator_ids(self, administrator_ids):
        """Sets the administrator_ids of this Recipients.

        List of recipient administrators IDs.  # noqa: E501

        :param administrator_ids: The administrator_ids of this Recipients.  # noqa: E501
        :type: list[int]
        """

        self._administrator_ids = administrator_ids

    @property
    def contact_ids(self):
        """Gets the contact_ids of this Recipients.  # noqa: E501

        List of recipient contact IDs.  # noqa: E501

        :return: The contact_ids of this Recipients.  # noqa: E501
        :rtype: list[int]
        """
        return self._contact_ids

    @contact_ids.setter
    def contact_ids(self, contact_ids):
        """Sets the contact_ids of this Recipients.

        List of recipient contact IDs.  # noqa: E501

        :param contact_ids: The contact_ids of this Recipients.  # noqa: E501
        :type: list[int]
        """

        self._contact_ids = contact_ids

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
        if issubclass(Recipients, dict):
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
        if not isinstance(other, Recipients):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
