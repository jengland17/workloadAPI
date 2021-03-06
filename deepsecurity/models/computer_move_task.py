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

from deepsecurity.models.workload_security_proxy import WorkloadSecurityProxy  # noqa: F401,E501
from deepsecurity.models.workload_security_relay_proxy import WorkloadSecurityRelayProxy  # noqa: F401,E501


class ComputerMoveTask(object):
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
        'computer_id': 'int',
        'workload_security_policy_id': 'int',
        'workload_security_computer_group_id': 'int',
        'workload_security_relay_group_id': 'int',
        'workload_security_proxy': 'WorkloadSecurityProxy',
        'workload_security_relay_proxy': 'WorkloadSecurityRelayProxy',
        'move_state': 'str',
        'id': 'int'
    }

    attribute_map = {
        'computer_id': 'computerID',
        'workload_security_policy_id': 'workloadSecurityPolicyID',
        'workload_security_computer_group_id': 'workloadSecurityComputerGroupID',
        'workload_security_relay_group_id': 'workloadSecurityRelayGroupID',
        'workload_security_proxy': 'workloadSecurityProxy',
        'workload_security_relay_proxy': 'workloadSecurityRelayProxy',
        'move_state': 'moveState',
        'id': 'ID'
    }

    def __init__(self, computer_id=None, workload_security_policy_id=None, workload_security_computer_group_id=None, workload_security_relay_group_id=None, workload_security_proxy=None, workload_security_relay_proxy=None, move_state=None, id=None):  # noqa: E501
        """ComputerMoveTask - a model defined in Swagger"""  # noqa: E501

        self._computer_id = None
        self._workload_security_policy_id = None
        self._workload_security_computer_group_id = None
        self._workload_security_relay_group_id = None
        self._workload_security_proxy = None
        self._workload_security_relay_proxy = None
        self._move_state = None
        self._id = None
        self.discriminator = None

        if computer_id is not None:
            self.computer_id = computer_id
        if workload_security_policy_id is not None:
            self.workload_security_policy_id = workload_security_policy_id
        if workload_security_computer_group_id is not None:
            self.workload_security_computer_group_id = workload_security_computer_group_id
        if workload_security_relay_group_id is not None:
            self.workload_security_relay_group_id = workload_security_relay_group_id
        if workload_security_proxy is not None:
            self.workload_security_proxy = workload_security_proxy
        if workload_security_relay_proxy is not None:
            self.workload_security_relay_proxy = workload_security_relay_proxy
        if move_state is not None:
            self.move_state = move_state
        if id is not None:
            self.id = id

    @property
    def computer_id(self):
        """Gets the computer_id of this ComputerMoveTask.  # noqa: E501

        Target computer to move. Searchable as Numeric.  # noqa: E501

        :return: The computer_id of this ComputerMoveTask.  # noqa: E501
        :rtype: int
        """
        return self._computer_id

    @computer_id.setter
    def computer_id(self, computer_id):
        """Sets the computer_id of this ComputerMoveTask.

        Target computer to move. Searchable as Numeric.  # noqa: E501

        :param computer_id: The computer_id of this ComputerMoveTask.  # noqa: E501
        :type: int
        """

        self._computer_id = computer_id

    @property
    def workload_security_policy_id(self):
        """Gets the workload_security_policy_id of this ComputerMoveTask.  # noqa: E501

        Policy ID on the Workload Security.  # noqa: E501

        :return: The workload_security_policy_id of this ComputerMoveTask.  # noqa: E501
        :rtype: int
        """
        return self._workload_security_policy_id

    @workload_security_policy_id.setter
    def workload_security_policy_id(self, workload_security_policy_id):
        """Sets the workload_security_policy_id of this ComputerMoveTask.

        Policy ID on the Workload Security.  # noqa: E501

        :param workload_security_policy_id: The workload_security_policy_id of this ComputerMoveTask.  # noqa: E501
        :type: int
        """

        self._workload_security_policy_id = workload_security_policy_id

    @property
    def workload_security_computer_group_id(self):
        """Gets the workload_security_computer_group_id of this ComputerMoveTask.  # noqa: E501

        Computer Group ID on the Workload Security.  # noqa: E501

        :return: The workload_security_computer_group_id of this ComputerMoveTask.  # noqa: E501
        :rtype: int
        """
        return self._workload_security_computer_group_id

    @workload_security_computer_group_id.setter
    def workload_security_computer_group_id(self, workload_security_computer_group_id):
        """Sets the workload_security_computer_group_id of this ComputerMoveTask.

        Computer Group ID on the Workload Security.  # noqa: E501

        :param workload_security_computer_group_id: The workload_security_computer_group_id of this ComputerMoveTask.  # noqa: E501
        :type: int
        """

        self._workload_security_computer_group_id = workload_security_computer_group_id

    @property
    def workload_security_relay_group_id(self):
        """Gets the workload_security_relay_group_id of this ComputerMoveTask.  # noqa: E501

        Relay Group ID on the Workload Security.  # noqa: E501

        :return: The workload_security_relay_group_id of this ComputerMoveTask.  # noqa: E501
        :rtype: int
        """
        return self._workload_security_relay_group_id

    @workload_security_relay_group_id.setter
    def workload_security_relay_group_id(self, workload_security_relay_group_id):
        """Sets the workload_security_relay_group_id of this ComputerMoveTask.

        Relay Group ID on the Workload Security.  # noqa: E501

        :param workload_security_relay_group_id: The workload_security_relay_group_id of this ComputerMoveTask.  # noqa: E501
        :type: int
        """

        self._workload_security_relay_group_id = workload_security_relay_group_id

    @property
    def workload_security_proxy(self):
        """Gets the workload_security_proxy of this ComputerMoveTask.  # noqa: E501

        Workload Security Proxy for agent.  # noqa: E501

        :return: The workload_security_proxy of this ComputerMoveTask.  # noqa: E501
        :rtype: WorkloadSecurityProxy
        """
        return self._workload_security_proxy

    @workload_security_proxy.setter
    def workload_security_proxy(self, workload_security_proxy):
        """Sets the workload_security_proxy of this ComputerMoveTask.

        Workload Security Proxy for agent.  # noqa: E501

        :param workload_security_proxy: The workload_security_proxy of this ComputerMoveTask.  # noqa: E501
        :type: WorkloadSecurityProxy
        """

        self._workload_security_proxy = workload_security_proxy

    @property
    def workload_security_relay_proxy(self):
        """Gets the workload_security_relay_proxy of this ComputerMoveTask.  # noqa: E501

        Workload Security Relay Proxy of agent.  # noqa: E501

        :return: The workload_security_relay_proxy of this ComputerMoveTask.  # noqa: E501
        :rtype: WorkloadSecurityRelayProxy
        """
        return self._workload_security_relay_proxy

    @workload_security_relay_proxy.setter
    def workload_security_relay_proxy(self, workload_security_relay_proxy):
        """Sets the workload_security_relay_proxy of this ComputerMoveTask.

        Workload Security Relay Proxy of agent.  # noqa: E501

        :param workload_security_relay_proxy: The workload_security_relay_proxy of this ComputerMoveTask.  # noqa: E501
        :type: WorkloadSecurityRelayProxy
        """

        self._workload_security_relay_proxy = workload_security_relay_proxy

    @property
    def move_state(self):
        """Gets the move_state of this ComputerMoveTask.  # noqa: E501

        Move status  # noqa: E501

        :return: The move_state of this ComputerMoveTask.  # noqa: E501
        :rtype: str
        """
        return self._move_state

    @move_state.setter
    def move_state(self, move_state):
        """Sets the move_state of this ComputerMoveTask.

        Move status  # noqa: E501

        :param move_state: The move_state of this ComputerMoveTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["move-requested", "moving", "move-complete", "move-failed", "move-failed-no-response", "move-failed-activation-failed", "move-failed-unmanaged"]  # noqa: E501
        if move_state not in allowed_values:
            raise ValueError(
                "Invalid value for `move_state` ({0}), must be one of {1}"  # noqa: E501
                .format(move_state, allowed_values)
            )

        self._move_state = move_state

    @property
    def id(self):
        """Gets the id of this ComputerMoveTask.  # noqa: E501

        ID of the ComputerMoveTask.  # noqa: E501

        :return: The id of this ComputerMoveTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComputerMoveTask.

        ID of the ComputerMoveTask.  # noqa: E501

        :param id: The id of this ComputerMoveTask.  # noqa: E501
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
        if issubclass(ComputerMoveTask, dict):
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
        if not isinstance(other, ComputerMoveTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

