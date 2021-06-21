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


class ComputerGroup(object):
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
        'type': 'str',
        'name': 'str',
        'description': 'str',
        'parent_group_id': 'int',
        'directory_id': 'int',
        'external_id': 'str',
        'virtual_id': 'int',
        'virtual_type': 'int',
        'virtual_name': 'str',
        'cloud_type': 'str',
        'cloud_resource_type': 'str',
        'cloud_id': 'int',
        'amazon_account_id': 'int',
        'amazon_region_id': 'int',
        'amazon_vpcid': 'int',
        'amazon_subnet_id': 'int',
        'amazon_workspaces_id': 'int',
        'amazon_directory_id': 'int',
        'id': 'int'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'description': 'description',
        'parent_group_id': 'parentGroupID',
        'directory_id': 'directoryID',
        'external_id': 'externalID',
        'virtual_id': 'virtualID',
        'virtual_type': 'virtualType',
        'virtual_name': 'virtualName',
        'cloud_type': 'cloudType',
        'cloud_resource_type': 'cloudResourceType',
        'cloud_id': 'cloudID',
        'amazon_account_id': 'amazonAccountID',
        'amazon_region_id': 'amazonRegionID',
        'amazon_vpcid': 'amazonVPCID',
        'amazon_subnet_id': 'amazonSubnetID',
        'amazon_workspaces_id': 'amazonWorkspacesID',
        'amazon_directory_id': 'amazonDirectoryID',
        'id': 'ID'
    }

    def __init__(self, type=None, name=None, description=None, parent_group_id=None, directory_id=None, external_id=None, virtual_id=None, virtual_type=None, virtual_name=None, cloud_type=None, cloud_resource_type=None, cloud_id=None, amazon_account_id=None, amazon_region_id=None, amazon_vpcid=None, amazon_subnet_id=None, amazon_workspaces_id=None, amazon_directory_id=None, id=None):  # noqa: E501
        """ComputerGroup - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._name = None
        self._description = None
        self._parent_group_id = None
        self._directory_id = None
        self._external_id = None
        self._virtual_id = None
        self._virtual_type = None
        self._virtual_name = None
        self._cloud_type = None
        self._cloud_resource_type = None
        self._cloud_id = None
        self._amazon_account_id = None
        self._amazon_region_id = None
        self._amazon_vpcid = None
        self._amazon_subnet_id = None
        self._amazon_workspaces_id = None
        self._amazon_directory_id = None
        self._id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if parent_group_id is not None:
            self.parent_group_id = parent_group_id
        if directory_id is not None:
            self.directory_id = directory_id
        if external_id is not None:
            self.external_id = external_id
        if virtual_id is not None:
            self.virtual_id = virtual_id
        if virtual_type is not None:
            self.virtual_type = virtual_type
        if virtual_name is not None:
            self.virtual_name = virtual_name
        if cloud_type is not None:
            self.cloud_type = cloud_type
        if cloud_resource_type is not None:
            self.cloud_resource_type = cloud_resource_type
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if amazon_account_id is not None:
            self.amazon_account_id = amazon_account_id
        if amazon_region_id is not None:
            self.amazon_region_id = amazon_region_id
        if amazon_vpcid is not None:
            self.amazon_vpcid = amazon_vpcid
        if amazon_subnet_id is not None:
            self.amazon_subnet_id = amazon_subnet_id
        if amazon_workspaces_id is not None:
            self.amazon_workspaces_id = amazon_workspaces_id
        if amazon_directory_id is not None:
            self.amazon_directory_id = amazon_directory_id
        if id is not None:
            self.id = id

    @property
    def type(self):
        """Gets the type of this ComputerGroup.  # noqa: E501

        Specifies what type the ComputerGroup is. Defaults to `folder`  # noqa: E501

        :return: The type of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComputerGroup.

        Specifies what type the ComputerGroup is. Defaults to `folder`  # noqa: E501

        :param type: The type of this ComputerGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["ad-add-directory", "ad-folder-network", "aws-region", "aws-vpc", "aws-subnet", "aws-workspaces", "aws-directory", "azure-top", "azure-group", "gcp-connector", "gcp-project", "cloud-provider-top", "vcloud-top", "aws-account", "vm-group", "vcloud-provider_datacenter", "vcloud-vapp", "vcenters-top", "vcenter-folder-network", "vmware-datacenter", "vcenter-cluster-group", "external-group", "folder", "root"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this ComputerGroup.  # noqa: E501

        Name of the ComputerGroup. Searchable as String.  # noqa: E501

        :return: The name of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputerGroup.

        Name of the ComputerGroup. Searchable as String.  # noqa: E501

        :param name: The name of this ComputerGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ComputerGroup.  # noqa: E501

        Description of the ComputerGroup. Searchable as String.  # noqa: E501

        :return: The description of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComputerGroup.

        Description of the ComputerGroup. Searchable as String.  # noqa: E501

        :param description: The description of this ComputerGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this ComputerGroup.  # noqa: E501

        ID of the ComputerGroup's parent group. Empty if the parent is a root ComputerGroup. ComputerGroup will be a root group unless a valid value for `parentGroupID` is set. Searchable as Numeric.  # noqa: E501

        :return: The parent_group_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this ComputerGroup.

        ID of the ComputerGroup's parent group. Empty if the parent is a root ComputerGroup. ComputerGroup will be a root group unless a valid value for `parentGroupID` is set. Searchable as Numeric.  # noqa: E501

        :param parent_group_id: The parent_group_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._parent_group_id = parent_group_id

    @property
    def directory_id(self):
        """Gets the directory_id of this ComputerGroup.  # noqa: E501

        ID of the ComputerGroup's directory server. Set to `0` if the group is not a directory server. Searchable as Numeric.  # noqa: E501

        :return: The directory_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this ComputerGroup.

        ID of the ComputerGroup's directory server. Set to `0` if the group is not a directory server. Searchable as Numeric.  # noqa: E501

        :param directory_id: The directory_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._directory_id = directory_id

    @property
    def external_id(self):
        """Gets the external_id of this ComputerGroup.  # noqa: E501

        External ID of the ComputerGroup. Empty if the ComputerGroup is not created/managed by a cloud account. Searchable as String.  # noqa: E501

        :return: The external_id of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ComputerGroup.

        External ID of the ComputerGroup. Empty if the ComputerGroup is not created/managed by a cloud account. Searchable as String.  # noqa: E501

        :param external_id: The external_id of this ComputerGroup.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def virtual_id(self):
        """Gets the virtual_id of this ComputerGroup.  # noqa: E501

        ID of the ComputerGroup as it exists in VMware vCloud. Set to `0` if the ComputerGroup is not from vCloud. Searchable as Numeric.  # noqa: E501

        :return: The virtual_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._virtual_id

    @virtual_id.setter
    def virtual_id(self, virtual_id):
        """Sets the virtual_id of this ComputerGroup.

        ID of the ComputerGroup as it exists in VMware vCloud. Set to `0` if the ComputerGroup is not from vCloud. Searchable as Numeric.  # noqa: E501

        :param virtual_id: The virtual_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._virtual_id = virtual_id

    @property
    def virtual_type(self):
        """Gets the virtual_type of this ComputerGroup.  # noqa: E501

        Type of the ComputerGroup as it exists in VMware vCloud. Set to `0` if the ComputerGroup is not from vCloud. Searchable as Numeric.  # noqa: E501

        :return: The virtual_type of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._virtual_type

    @virtual_type.setter
    def virtual_type(self, virtual_type):
        """Sets the virtual_type of this ComputerGroup.

        Type of the ComputerGroup as it exists in VMware vCloud. Set to `0` if the ComputerGroup is not from vCloud. Searchable as Numeric.  # noqa: E501

        :param virtual_type: The virtual_type of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._virtual_type = virtual_type

    @property
    def virtual_name(self):
        """Gets the virtual_name of this ComputerGroup.  # noqa: E501

        Name of the ComputerGroup as it exists in VMware vCloud. Ignored if the ComputerGroup is not from vCloud. Searchable as String.  # noqa: E501

        :return: The virtual_name of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._virtual_name

    @virtual_name.setter
    def virtual_name(self, virtual_name):
        """Sets the virtual_name of this ComputerGroup.

        Name of the ComputerGroup as it exists in VMware vCloud. Ignored if the ComputerGroup is not from vCloud. Searchable as String.  # noqa: E501

        :param virtual_name: The virtual_name of this ComputerGroup.  # noqa: E501
        :type: str
        """

        self._virtual_name = virtual_name

    @property
    def cloud_type(self):
        """Gets the cloud_type of this ComputerGroup.  # noqa: E501

        Cloud platform of the ComputerGroup.  Ignored if the ComputerGroup does not represent a cloud container. Searchable as Choice.  # noqa: E501

        :return: The cloud_type of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this ComputerGroup.

        Cloud platform of the ComputerGroup.  Ignored if the ComputerGroup does not represent a cloud container. Searchable as Choice.  # noqa: E501

        :param cloud_type: The cloud_type of this ComputerGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["amazon", "vcloud-private-cloud", "azure", "azure-arm", "gcp"]  # noqa: E501
        if cloud_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cloud_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_type, allowed_values)
            )

        self._cloud_type = cloud_type

    @property
    def cloud_resource_type(self):
        """Gets the cloud_resource_type of this ComputerGroup.  # noqa: E501

        Cloud container type of the ComputerGroup. This is platform dependent. Ignored if the ComputerGroup does not represent a cloud container. Searchable as Numeric.  # noqa: E501

        :return: The cloud_resource_type of this ComputerGroup.  # noqa: E501
        :rtype: str
        """
        return self._cloud_resource_type

    @cloud_resource_type.setter
    def cloud_resource_type(self, cloud_resource_type):
        """Sets the cloud_resource_type of this ComputerGroup.

        Cloud container type of the ComputerGroup. This is platform dependent. Ignored if the ComputerGroup does not represent a cloud container. Searchable as Numeric.  # noqa: E501

        :param cloud_resource_type: The cloud_resource_type of this ComputerGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["physical", "top-level", "partition", "aws-ec2-instance", "aws-workspace", "vcloud-organization", "vcloud-catalog", "vcloud-networks", "vcloud-virtual-data-center", "vcloud-virtual-application", "vcloud-virtual-application-template", "vcloud-virtual-machine", "azure-instance", "azure-arm-instance"]  # noqa: E501
        if cloud_resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cloud_resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_resource_type, allowed_values)
            )

        self._cloud_resource_type = cloud_resource_type

    @property
    def cloud_id(self):
        """Gets the cloud_id of this ComputerGroup.  # noqa: E501

        Cloud container ID of the ComputerGroup. Ignored if the ComputerGroup does not represent a cloud container. Searchable as Numeric.  # noqa: E501

        :return: The cloud_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this ComputerGroup.

        Cloud container ID of the ComputerGroup. Ignored if the ComputerGroup does not represent a cloud container. Searchable as Numeric.  # noqa: E501

        :param cloud_id: The cloud_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._cloud_id = cloud_id

    @property
    def amazon_account_id(self):
        """Gets the amazon_account_id of this ComputerGroup.  # noqa: E501

        Amazon Web Services account ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services account. Searchable as Numeric.  # noqa: E501

        :return: The amazon_account_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._amazon_account_id

    @amazon_account_id.setter
    def amazon_account_id(self, amazon_account_id):
        """Sets the amazon_account_id of this ComputerGroup.

        Amazon Web Services account ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services account. Searchable as Numeric.  # noqa: E501

        :param amazon_account_id: The amazon_account_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._amazon_account_id = amazon_account_id

    @property
    def amazon_region_id(self):
        """Gets the amazon_region_id of this ComputerGroup.  # noqa: E501

        Amazon Web Services region ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services region. amazonWorkspacesID will be used instead if the ComputerGroup represents an Amazon Web Services WorkSpaces node. Searchable as Numeric.  # noqa: E501

        :return: The amazon_region_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._amazon_region_id

    @amazon_region_id.setter
    def amazon_region_id(self, amazon_region_id):
        """Sets the amazon_region_id of this ComputerGroup.

        Amazon Web Services region ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services region. amazonWorkspacesID will be used instead if the ComputerGroup represents an Amazon Web Services WorkSpaces node. Searchable as Numeric.  # noqa: E501

        :param amazon_region_id: The amazon_region_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._amazon_region_id = amazon_region_id

    @property
    def amazon_vpcid(self):
        """Gets the amazon_vpcid of this ComputerGroup.  # noqa: E501

        Amazon Web Services Virtual Private Cloud ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services Virtual Private Cloud. Searchable as Numeric.  # noqa: E501

        :return: The amazon_vpcid of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._amazon_vpcid

    @amazon_vpcid.setter
    def amazon_vpcid(self, amazon_vpcid):
        """Sets the amazon_vpcid of this ComputerGroup.

        Amazon Web Services Virtual Private Cloud ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services Virtual Private Cloud. Searchable as Numeric.  # noqa: E501

        :param amazon_vpcid: The amazon_vpcid of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._amazon_vpcid = amazon_vpcid

    @property
    def amazon_subnet_id(self):
        """Gets the amazon_subnet_id of this ComputerGroup.  # noqa: E501

        Amazon Web Services subnet ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services subnet. Searchable as Numeric.  # noqa: E501

        :return: The amazon_subnet_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._amazon_subnet_id

    @amazon_subnet_id.setter
    def amazon_subnet_id(self, amazon_subnet_id):
        """Sets the amazon_subnet_id of this ComputerGroup.

        Amazon Web Services subnet ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services subnet. Searchable as Numeric.  # noqa: E501

        :param amazon_subnet_id: The amazon_subnet_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._amazon_subnet_id = amazon_subnet_id

    @property
    def amazon_workspaces_id(self):
        """Gets the amazon_workspaces_id of this ComputerGroup.  # noqa: E501

        Amazon Web Services WorkSpaces ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services WorkSpace. Will be used instead of amazonRegionID if the ComputerGroup represents a WorkSpaces node under a region. Searchable as Numeric.  # noqa: E501

        :return: The amazon_workspaces_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._amazon_workspaces_id

    @amazon_workspaces_id.setter
    def amazon_workspaces_id(self, amazon_workspaces_id):
        """Sets the amazon_workspaces_id of this ComputerGroup.

        Amazon Web Services WorkSpaces ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services WorkSpace. Will be used instead of amazonRegionID if the ComputerGroup represents a WorkSpaces node under a region. Searchable as Numeric.  # noqa: E501

        :param amazon_workspaces_id: The amazon_workspaces_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._amazon_workspaces_id = amazon_workspaces_id

    @property
    def amazon_directory_id(self):
        """Gets the amazon_directory_id of this ComputerGroup.  # noqa: E501

        Amazon Web Services directory ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services directory. Searchable as Numeric.  # noqa: E501

        :return: The amazon_directory_id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._amazon_directory_id

    @amazon_directory_id.setter
    def amazon_directory_id(self, amazon_directory_id):
        """Sets the amazon_directory_id of this ComputerGroup.

        Amazon Web Services directory ID of the ComputerGroup. Set to `0` if the ComputerGroup does not represent an Amazon Web Services directory. Searchable as Numeric.  # noqa: E501

        :param amazon_directory_id: The amazon_directory_id of this ComputerGroup.  # noqa: E501
        :type: int
        """

        self._amazon_directory_id = amazon_directory_id

    @property
    def id(self):
        """Gets the id of this ComputerGroup.  # noqa: E501

        ID of the ComputerGroup. Searchable as ID.  # noqa: E501

        :return: The id of this ComputerGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComputerGroup.

        ID of the ComputerGroup. Searchable as ID.  # noqa: E501

        :param id: The id of this ComputerGroup.  # noqa: E501
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
        if issubclass(ComputerGroup, dict):
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
        if not isinstance(other, ComputerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

