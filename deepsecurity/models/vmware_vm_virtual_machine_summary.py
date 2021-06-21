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


class VmwareVMVirtualMachineSummary(object):
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
        'operating_system': 'str',
        'memory': 'str',
        'vmware_tools': 'str',
        'bios_uuid': 'str',
        'state': 'str',
        'notes': 'list[str]',
        'cpu': 'str',
        'v_center_uuid': 'str',
        'nsx_security_groups': 'list[str]',
        'ip_address': 'str',
        'dns_name': 'str'
    }

    attribute_map = {
        'operating_system': 'operatingSystem',
        'memory': 'memory',
        'vmware_tools': 'vmwareTools',
        'bios_uuid': 'biosUUID',
        'state': 'state',
        'notes': 'notes',
        'cpu': 'CPU',
        'v_center_uuid': 'vCenterUUID',
        'nsx_security_groups': 'NSXSecurityGroups',
        'ip_address': 'IPAddress',
        'dns_name': 'DNSName'
    }

    def __init__(self, operating_system=None, memory=None, vmware_tools=None, bios_uuid=None, state=None, notes=None, cpu=None, v_center_uuid=None, nsx_security_groups=None, ip_address=None, dns_name=None):  # noqa: E501
        """VmwareVMVirtualMachineSummary - a model defined in Swagger"""  # noqa: E501

        self._operating_system = None
        self._memory = None
        self._vmware_tools = None
        self._bios_uuid = None
        self._state = None
        self._notes = None
        self._cpu = None
        self._v_center_uuid = None
        self._nsx_security_groups = None
        self._ip_address = None
        self._dns_name = None
        self.discriminator = None

        if operating_system is not None:
            self.operating_system = operating_system
        if memory is not None:
            self.memory = memory
        if vmware_tools is not None:
            self.vmware_tools = vmware_tools
        if bios_uuid is not None:
            self.bios_uuid = bios_uuid
        if state is not None:
            self.state = state
        if notes is not None:
            self.notes = notes
        if cpu is not None:
            self.cpu = cpu
        if v_center_uuid is not None:
            self.v_center_uuid = v_center_uuid
        if nsx_security_groups is not None:
            self.nsx_security_groups = nsx_security_groups
        if ip_address is not None:
            self.ip_address = ip_address
        if dns_name is not None:
            self.dns_name = dns_name

    @property
    def operating_system(self):
        """Gets the operating_system of this VmwareVMVirtualMachineSummary.  # noqa: E501

        Operating system, for example: \"Microsoft Windows Server 2012 (64-bit)\". Searchable as String.  # noqa: E501

        :return: The operating_system of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this VmwareVMVirtualMachineSummary.

        Operating system, for example: \"Microsoft Windows Server 2012 (64-bit)\". Searchable as String.  # noqa: E501

        :param operating_system: The operating_system of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

    @property
    def memory(self):
        """Gets the memory of this VmwareVMVirtualMachineSummary.  # noqa: E501

        Memory allocation, for example: \"12,288 MB\".  # noqa: E501

        :return: The memory of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this VmwareVMVirtualMachineSummary.

        Memory allocation, for example: \"12,288 MB\".  # noqa: E501

        :param memory: The memory of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._memory = memory

    @property
    def vmware_tools(self):
        """Gets the vmware_tools of this VmwareVMVirtualMachineSummary.  # noqa: E501

        VMware tools status, for example: \"OK\".  # noqa: E501

        :return: The vmware_tools of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._vmware_tools

    @vmware_tools.setter
    def vmware_tools(self, vmware_tools):
        """Sets the vmware_tools of this VmwareVMVirtualMachineSummary.

        VMware tools status, for example: \"OK\".  # noqa: E501

        :param vmware_tools: The vmware_tools of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._vmware_tools = vmware_tools

    @property
    def bios_uuid(self):
        """Gets the bios_uuid of this VmwareVMVirtualMachineSummary.  # noqa: E501

        BIOS UUID, for example: \"421e1137-5c49-56e4-246d-9bf7637e69f5\". Searchable as String.  # noqa: E501

        :return: The bios_uuid of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._bios_uuid

    @bios_uuid.setter
    def bios_uuid(self, bios_uuid):
        """Sets the bios_uuid of this VmwareVMVirtualMachineSummary.

        BIOS UUID, for example: \"421e1137-5c49-56e4-246d-9bf7637e69f5\". Searchable as String.  # noqa: E501

        :param bios_uuid: The bios_uuid of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._bios_uuid = bios_uuid

    @property
    def state(self):
        """Gets the state of this VmwareVMVirtualMachineSummary.  # noqa: E501

        Power state, for example: \"Powered On\".  # noqa: E501

        :return: The state of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VmwareVMVirtualMachineSummary.

        Power state, for example: \"Powered On\".  # noqa: E501

        :param state: The state of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def notes(self):
        """Gets the notes of this VmwareVMVirtualMachineSummary.  # noqa: E501

        Notes associated with the VM.  # noqa: E501

        :return: The notes of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this VmwareVMVirtualMachineSummary.

        Notes associated with the VM.  # noqa: E501

        :param notes: The notes of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: list[str]
        """

        self._notes = notes

    @property
    def cpu(self):
        """Gets the cpu of this VmwareVMVirtualMachineSummary.  # noqa: E501

        Number and type of CPUs, for example: \"4 vCPU\". Searchable as Numeric.  # noqa: E501

        :return: The cpu of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this VmwareVMVirtualMachineSummary.

        Number and type of CPUs, for example: \"4 vCPU\". Searchable as Numeric.  # noqa: E501

        :param cpu: The cpu of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._cpu = cpu

    @property
    def v_center_uuid(self):
        """Gets the v_center_uuid of this VmwareVMVirtualMachineSummary.  # noqa: E501


        :return: The v_center_uuid of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._v_center_uuid

    @v_center_uuid.setter
    def v_center_uuid(self, v_center_uuid):
        """Sets the v_center_uuid of this VmwareVMVirtualMachineSummary.


        :param v_center_uuid: The v_center_uuid of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._v_center_uuid = v_center_uuid

    @property
    def nsx_security_groups(self):
        """Gets the nsx_security_groups of this VmwareVMVirtualMachineSummary.  # noqa: E501


        :return: The nsx_security_groups of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._nsx_security_groups

    @nsx_security_groups.setter
    def nsx_security_groups(self, nsx_security_groups):
        """Sets the nsx_security_groups of this VmwareVMVirtualMachineSummary.


        :param nsx_security_groups: The nsx_security_groups of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: list[str]
        """

        self._nsx_security_groups = nsx_security_groups

    @property
    def ip_address(self):
        """Gets the ip_address of this VmwareVMVirtualMachineSummary.  # noqa: E501


        :return: The ip_address of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this VmwareVMVirtualMachineSummary.


        :param ip_address: The ip_address of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def dns_name(self):
        """Gets the dns_name of this VmwareVMVirtualMachineSummary.  # noqa: E501


        :return: The dns_name of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :rtype: str
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this VmwareVMVirtualMachineSummary.


        :param dns_name: The dns_name of this VmwareVMVirtualMachineSummary.  # noqa: E501
        :type: str
        """

        self._dns_name = dns_name

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
        if issubclass(VmwareVMVirtualMachineSummary, dict):
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
        if not isinstance(other, VmwareVMVirtualMachineSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

