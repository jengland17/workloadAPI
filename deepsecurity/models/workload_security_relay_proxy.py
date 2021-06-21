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


class WorkloadSecurityRelayProxy(object):
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
        'host': 'str',
        'port': 'int',
        'user': 'str',
        'password': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'user': 'user',
        'password': 'password'
    }

    def __init__(self, host=None, port=None, user=None, password=None):  # noqa: E501
        """WorkloadSecurityRelayProxy - a model defined in Swagger"""  # noqa: E501

        self._host = None
        self._port = None
        self._user = None
        self._password = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password

    @property
    def host(self):
        """Gets the host of this WorkloadSecurityRelayProxy.  # noqa: E501

        The hostname of the Proxy.  # noqa: E501

        :return: The host of this WorkloadSecurityRelayProxy.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this WorkloadSecurityRelayProxy.

        The hostname of the Proxy.  # noqa: E501

        :param host: The host of this WorkloadSecurityRelayProxy.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this WorkloadSecurityRelayProxy.  # noqa: E501

        The port of the Proxy.  # noqa: E501

        :return: The port of this WorkloadSecurityRelayProxy.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this WorkloadSecurityRelayProxy.

        The port of the Proxy.  # noqa: E501

        :param port: The port of this WorkloadSecurityRelayProxy.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def user(self):
        """Gets the user of this WorkloadSecurityRelayProxy.  # noqa: E501

        The username for the Proxy.  # noqa: E501

        :return: The user of this WorkloadSecurityRelayProxy.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WorkloadSecurityRelayProxy.

        The username for the Proxy.  # noqa: E501

        :param user: The user of this WorkloadSecurityRelayProxy.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def password(self):
        """Gets the password of this WorkloadSecurityRelayProxy.  # noqa: E501

        The password for the Proxy.  # noqa: E501

        :return: The password of this WorkloadSecurityRelayProxy.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WorkloadSecurityRelayProxy.

        The password for the Proxy.  # noqa: E501

        :param password: The password of this WorkloadSecurityRelayProxy.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(WorkloadSecurityRelayProxy, dict):
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
        if not isinstance(other, WorkloadSecurityRelayProxy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

