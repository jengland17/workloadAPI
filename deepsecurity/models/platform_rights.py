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

from deepsecurity.models.administrator_rights import AdministratorRights  # noqa: F401,E501
from deepsecurity.models.administrator_role_rights import AdministratorRoleRights  # noqa: F401,E501
from deepsecurity.models.agent_version_control_rights import AgentVersionControlRights  # noqa: F401,E501
from deepsecurity.models.alert_configuration_rights import AlertConfigurationRights  # noqa: F401,E501
from deepsecurity.models.alert_rights import AlertRights  # noqa: F401,E501
from deepsecurity.models.api_key_rights import ApiKeyRights  # noqa: F401,E501
from deepsecurity.models.asset_value_rights import AssetValueRights  # noqa: F401,E501
from deepsecurity.models.certificate_rights import CertificateRights  # noqa: F401,E501
from deepsecurity.models.computer_rights import ComputerRights  # noqa: F401,E501
from deepsecurity.models.contact_rights import ContactRights  # noqa: F401,E501
from deepsecurity.models.diagnostic_rights import DiagnosticRights  # noqa: F401,E501
from deepsecurity.models.expert_setting_rights import ExpertSettingRights  # noqa: F401,E501
from deepsecurity.models.ip_list_rights import IpListRights  # noqa: F401,E501
from deepsecurity.models.license_rights import LicenseRights  # noqa: F401,E501
from deepsecurity.models.multi_tenant_rights import MultiTenantRights  # noqa: F401,E501
from deepsecurity.models.policy_rights import PolicyRights  # noqa: F401,E501
from deepsecurity.models.port_list_rights import PortListRights  # noqa: F401,E501
from deepsecurity.models.proxy_rights import ProxyRights  # noqa: F401,E501
from deepsecurity.models.relay_group_rights import RelayGroupRights  # noqa: F401,E501
from deepsecurity.models.saml_identity_provider_rights import SamlIdentityProviderRights  # noqa: F401,E501
from deepsecurity.models.scan_cache_rights import ScanCacheRights  # noqa: F401,E501
from deepsecurity.models.schedule_rights import ScheduleRights  # noqa: F401,E501
from deepsecurity.models.scheduled_task_rights import ScheduledTaskRights  # noqa: F401,E501
from deepsecurity.models.setting_rights import SettingRights  # noqa: F401,E501
from deepsecurity.models.syslog_configuration_rights import SyslogConfigurationRights  # noqa: F401,E501
from deepsecurity.models.system_information_rights import SystemInformationRights  # noqa: F401,E501
from deepsecurity.models.tagging_rights import TaggingRights  # noqa: F401,E501
from deepsecurity.models.update_rights import UpdateRights  # noqa: F401,E501


class PlatformRights(object):
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
        'administrator_rights': 'AdministratorRights',
        'administrator_role_rights': 'AdministratorRoleRights',
        'agent_version_control_rights': 'AgentVersionControlRights',
        'alert_configuration_rights': 'AlertConfigurationRights',
        'alert_rights': 'AlertRights',
        'certificate_rights': 'CertificateRights',
        'computer_rights': 'ComputerRights',
        'contact_rights': 'ContactRights',
        'diagnostic_rights': 'DiagnosticRights',
        'asset_value_rights': 'AssetValueRights',
        'license_rights': 'LicenseRights',
        'multi_tenant_rights': 'MultiTenantRights',
        'policy_rights': 'PolicyRights',
        'port_list_rights': 'PortListRights',
        'proxy_rights': 'ProxyRights',
        'relay_group_rights': 'RelayGroupRights',
        'scan_cache_rights': 'ScanCacheRights',
        'scheduled_task_rights': 'ScheduledTaskRights',
        'schedule_rights': 'ScheduleRights',
        'setting_rights': 'SettingRights',
        'expert_setting_rights': 'ExpertSettingRights',
        'syslog_configuration_rights': 'SyslogConfigurationRights',
        'system_information_rights': 'SystemInformationRights',
        'tagging_rights': 'TaggingRights',
        'update_rights': 'UpdateRights',
        'apikey_rights': 'ApiKeyRights',
        'iplist_rights': 'IpListRights',
        'samlidentity_provider_rights': 'SamlIdentityProviderRights'
    }

    attribute_map = {
        'administrator_rights': 'administratorRights',
        'administrator_role_rights': 'administratorRoleRights',
        'agent_version_control_rights': 'agentVersionControlRights',
        'alert_configuration_rights': 'alertConfigurationRights',
        'alert_rights': 'alertRights',
        'certificate_rights': 'certificateRights',
        'computer_rights': 'computerRights',
        'contact_rights': 'contactRights',
        'diagnostic_rights': 'diagnosticRights',
        'asset_value_rights': 'assetValueRights',
        'license_rights': 'licenseRights',
        'multi_tenant_rights': 'multiTenantRights',
        'policy_rights': 'policyRights',
        'port_list_rights': 'portListRights',
        'proxy_rights': 'proxyRights',
        'relay_group_rights': 'relayGroupRights',
        'scan_cache_rights': 'scanCacheRights',
        'scheduled_task_rights': 'scheduledTaskRights',
        'schedule_rights': 'scheduleRights',
        'setting_rights': 'settingRights',
        'expert_setting_rights': 'expertSettingRights',
        'syslog_configuration_rights': 'syslogConfigurationRights',
        'system_information_rights': 'systemInformationRights',
        'tagging_rights': 'taggingRights',
        'update_rights': 'updateRights',
        'apikey_rights': 'apikeyRights',
        'iplist_rights': 'iplistRights',
        'samlidentity_provider_rights': 'samlidentityProviderRights'
    }

    def __init__(self, administrator_rights=None, administrator_role_rights=None, agent_version_control_rights=None, alert_configuration_rights=None, alert_rights=None, certificate_rights=None, computer_rights=None, contact_rights=None, diagnostic_rights=None, asset_value_rights=None, license_rights=None, multi_tenant_rights=None, policy_rights=None, port_list_rights=None, proxy_rights=None, relay_group_rights=None, scan_cache_rights=None, scheduled_task_rights=None, schedule_rights=None, setting_rights=None, expert_setting_rights=None, syslog_configuration_rights=None, system_information_rights=None, tagging_rights=None, update_rights=None, apikey_rights=None, iplist_rights=None, samlidentity_provider_rights=None):  # noqa: E501
        """PlatformRights - a model defined in Swagger"""  # noqa: E501

        self._administrator_rights = None
        self._administrator_role_rights = None
        self._agent_version_control_rights = None
        self._alert_configuration_rights = None
        self._alert_rights = None
        self._certificate_rights = None
        self._computer_rights = None
        self._contact_rights = None
        self._diagnostic_rights = None
        self._asset_value_rights = None
        self._license_rights = None
        self._multi_tenant_rights = None
        self._policy_rights = None
        self._port_list_rights = None
        self._proxy_rights = None
        self._relay_group_rights = None
        self._scan_cache_rights = None
        self._scheduled_task_rights = None
        self._schedule_rights = None
        self._setting_rights = None
        self._expert_setting_rights = None
        self._syslog_configuration_rights = None
        self._system_information_rights = None
        self._tagging_rights = None
        self._update_rights = None
        self._apikey_rights = None
        self._iplist_rights = None
        self._samlidentity_provider_rights = None
        self.discriminator = None

        if administrator_rights is not None:
            self.administrator_rights = administrator_rights
        if administrator_role_rights is not None:
            self.administrator_role_rights = administrator_role_rights
        if agent_version_control_rights is not None:
            self.agent_version_control_rights = agent_version_control_rights
        if alert_configuration_rights is not None:
            self.alert_configuration_rights = alert_configuration_rights
        if alert_rights is not None:
            self.alert_rights = alert_rights
        if certificate_rights is not None:
            self.certificate_rights = certificate_rights
        if computer_rights is not None:
            self.computer_rights = computer_rights
        if contact_rights is not None:
            self.contact_rights = contact_rights
        if diagnostic_rights is not None:
            self.diagnostic_rights = diagnostic_rights
        if asset_value_rights is not None:
            self.asset_value_rights = asset_value_rights
        if license_rights is not None:
            self.license_rights = license_rights
        if multi_tenant_rights is not None:
            self.multi_tenant_rights = multi_tenant_rights
        if policy_rights is not None:
            self.policy_rights = policy_rights
        if port_list_rights is not None:
            self.port_list_rights = port_list_rights
        if proxy_rights is not None:
            self.proxy_rights = proxy_rights
        if relay_group_rights is not None:
            self.relay_group_rights = relay_group_rights
        if scan_cache_rights is not None:
            self.scan_cache_rights = scan_cache_rights
        if scheduled_task_rights is not None:
            self.scheduled_task_rights = scheduled_task_rights
        if schedule_rights is not None:
            self.schedule_rights = schedule_rights
        if setting_rights is not None:
            self.setting_rights = setting_rights
        if expert_setting_rights is not None:
            self.expert_setting_rights = expert_setting_rights
        if syslog_configuration_rights is not None:
            self.syslog_configuration_rights = syslog_configuration_rights
        if system_information_rights is not None:
            self.system_information_rights = system_information_rights
        if tagging_rights is not None:
            self.tagging_rights = tagging_rights
        if update_rights is not None:
            self.update_rights = update_rights
        if apikey_rights is not None:
            self.apikey_rights = apikey_rights
        if iplist_rights is not None:
            self.iplist_rights = iplist_rights
        if samlidentity_provider_rights is not None:
            self.samlidentity_provider_rights = samlidentity_provider_rights

    @property
    def administrator_rights(self):
        """Gets the administrator_rights of this PlatformRights.  # noqa: E501

        Rights related to administrators.  # noqa: E501

        :return: The administrator_rights of this PlatformRights.  # noqa: E501
        :rtype: AdministratorRights
        """
        return self._administrator_rights

    @administrator_rights.setter
    def administrator_rights(self, administrator_rights):
        """Sets the administrator_rights of this PlatformRights.

        Rights related to administrators.  # noqa: E501

        :param administrator_rights: The administrator_rights of this PlatformRights.  # noqa: E501
        :type: AdministratorRights
        """

        self._administrator_rights = administrator_rights

    @property
    def administrator_role_rights(self):
        """Gets the administrator_role_rights of this PlatformRights.  # noqa: E501

        Rights related to administrator roles.  # noqa: E501

        :return: The administrator_role_rights of this PlatformRights.  # noqa: E501
        :rtype: AdministratorRoleRights
        """
        return self._administrator_role_rights

    @administrator_role_rights.setter
    def administrator_role_rights(self, administrator_role_rights):
        """Sets the administrator_role_rights of this PlatformRights.

        Rights related to administrator roles.  # noqa: E501

        :param administrator_role_rights: The administrator_role_rights of this PlatformRights.  # noqa: E501
        :type: AdministratorRoleRights
        """

        self._administrator_role_rights = administrator_role_rights

    @property
    def agent_version_control_rights(self):
        """Gets the agent_version_control_rights of this PlatformRights.  # noqa: E501

        Rights related to agent version controls.  # noqa: E501

        :return: The agent_version_control_rights of this PlatformRights.  # noqa: E501
        :rtype: AgentVersionControlRights
        """
        return self._agent_version_control_rights

    @agent_version_control_rights.setter
    def agent_version_control_rights(self, agent_version_control_rights):
        """Sets the agent_version_control_rights of this PlatformRights.

        Rights related to agent version controls.  # noqa: E501

        :param agent_version_control_rights: The agent_version_control_rights of this PlatformRights.  # noqa: E501
        :type: AgentVersionControlRights
        """

        self._agent_version_control_rights = agent_version_control_rights

    @property
    def alert_configuration_rights(self):
        """Gets the alert_configuration_rights of this PlatformRights.  # noqa: E501

        Rights related to alert configurations.  # noqa: E501

        :return: The alert_configuration_rights of this PlatformRights.  # noqa: E501
        :rtype: AlertConfigurationRights
        """
        return self._alert_configuration_rights

    @alert_configuration_rights.setter
    def alert_configuration_rights(self, alert_configuration_rights):
        """Sets the alert_configuration_rights of this PlatformRights.

        Rights related to alert configurations.  # noqa: E501

        :param alert_configuration_rights: The alert_configuration_rights of this PlatformRights.  # noqa: E501
        :type: AlertConfigurationRights
        """

        self._alert_configuration_rights = alert_configuration_rights

    @property
    def alert_rights(self):
        """Gets the alert_rights of this PlatformRights.  # noqa: E501

        Rights related to alerts.  # noqa: E501

        :return: The alert_rights of this PlatformRights.  # noqa: E501
        :rtype: AlertRights
        """
        return self._alert_rights

    @alert_rights.setter
    def alert_rights(self, alert_rights):
        """Sets the alert_rights of this PlatformRights.

        Rights related to alerts.  # noqa: E501

        :param alert_rights: The alert_rights of this PlatformRights.  # noqa: E501
        :type: AlertRights
        """

        self._alert_rights = alert_rights

    @property
    def certificate_rights(self):
        """Gets the certificate_rights of this PlatformRights.  # noqa: E501

        Rights related to certificates.  # noqa: E501

        :return: The certificate_rights of this PlatformRights.  # noqa: E501
        :rtype: CertificateRights
        """
        return self._certificate_rights

    @certificate_rights.setter
    def certificate_rights(self, certificate_rights):
        """Sets the certificate_rights of this PlatformRights.

        Rights related to certificates.  # noqa: E501

        :param certificate_rights: The certificate_rights of this PlatformRights.  # noqa: E501
        :type: CertificateRights
        """

        self._certificate_rights = certificate_rights

    @property
    def computer_rights(self):
        """Gets the computer_rights of this PlatformRights.  # noqa: E501

        Rights related to computers.  # noqa: E501

        :return: The computer_rights of this PlatformRights.  # noqa: E501
        :rtype: ComputerRights
        """
        return self._computer_rights

    @computer_rights.setter
    def computer_rights(self, computer_rights):
        """Sets the computer_rights of this PlatformRights.

        Rights related to computers.  # noqa: E501

        :param computer_rights: The computer_rights of this PlatformRights.  # noqa: E501
        :type: ComputerRights
        """

        self._computer_rights = computer_rights

    @property
    def contact_rights(self):
        """Gets the contact_rights of this PlatformRights.  # noqa: E501

        Rights related to contacts.  # noqa: E501

        :return: The contact_rights of this PlatformRights.  # noqa: E501
        :rtype: ContactRights
        """
        return self._contact_rights

    @contact_rights.setter
    def contact_rights(self, contact_rights):
        """Sets the contact_rights of this PlatformRights.

        Rights related to contacts.  # noqa: E501

        :param contact_rights: The contact_rights of this PlatformRights.  # noqa: E501
        :type: ContactRights
        """

        self._contact_rights = contact_rights

    @property
    def diagnostic_rights(self):
        """Gets the diagnostic_rights of this PlatformRights.  # noqa: E501

        Rights related to diagnostics.  # noqa: E501

        :return: The diagnostic_rights of this PlatformRights.  # noqa: E501
        :rtype: DiagnosticRights
        """
        return self._diagnostic_rights

    @diagnostic_rights.setter
    def diagnostic_rights(self, diagnostic_rights):
        """Sets the diagnostic_rights of this PlatformRights.

        Rights related to diagnostics.  # noqa: E501

        :param diagnostic_rights: The diagnostic_rights of this PlatformRights.  # noqa: E501
        :type: DiagnosticRights
        """

        self._diagnostic_rights = diagnostic_rights

    @property
    def asset_value_rights(self):
        """Gets the asset_value_rights of this PlatformRights.  # noqa: E501

        Rights related to asset values.  # noqa: E501

        :return: The asset_value_rights of this PlatformRights.  # noqa: E501
        :rtype: AssetValueRights
        """
        return self._asset_value_rights

    @asset_value_rights.setter
    def asset_value_rights(self, asset_value_rights):
        """Sets the asset_value_rights of this PlatformRights.

        Rights related to asset values.  # noqa: E501

        :param asset_value_rights: The asset_value_rights of this PlatformRights.  # noqa: E501
        :type: AssetValueRights
        """

        self._asset_value_rights = asset_value_rights

    @property
    def license_rights(self):
        """Gets the license_rights of this PlatformRights.  # noqa: E501

        Rights related to licenses.  # noqa: E501

        :return: The license_rights of this PlatformRights.  # noqa: E501
        :rtype: LicenseRights
        """
        return self._license_rights

    @license_rights.setter
    def license_rights(self, license_rights):
        """Sets the license_rights of this PlatformRights.

        Rights related to licenses.  # noqa: E501

        :param license_rights: The license_rights of this PlatformRights.  # noqa: E501
        :type: LicenseRights
        """

        self._license_rights = license_rights

    @property
    def multi_tenant_rights(self):
        """Gets the multi_tenant_rights of this PlatformRights.  # noqa: E501

        Rights related to multi-tenant administration.  # noqa: E501

        :return: The multi_tenant_rights of this PlatformRights.  # noqa: E501
        :rtype: MultiTenantRights
        """
        return self._multi_tenant_rights

    @multi_tenant_rights.setter
    def multi_tenant_rights(self, multi_tenant_rights):
        """Sets the multi_tenant_rights of this PlatformRights.

        Rights related to multi-tenant administration.  # noqa: E501

        :param multi_tenant_rights: The multi_tenant_rights of this PlatformRights.  # noqa: E501
        :type: MultiTenantRights
        """

        self._multi_tenant_rights = multi_tenant_rights

    @property
    def policy_rights(self):
        """Gets the policy_rights of this PlatformRights.  # noqa: E501

        Rights related to policies.  # noqa: E501

        :return: The policy_rights of this PlatformRights.  # noqa: E501
        :rtype: PolicyRights
        """
        return self._policy_rights

    @policy_rights.setter
    def policy_rights(self, policy_rights):
        """Sets the policy_rights of this PlatformRights.

        Rights related to policies.  # noqa: E501

        :param policy_rights: The policy_rights of this PlatformRights.  # noqa: E501
        :type: PolicyRights
        """

        self._policy_rights = policy_rights

    @property
    def port_list_rights(self):
        """Gets the port_list_rights of this PlatformRights.  # noqa: E501

        Rights related to port lists.  # noqa: E501

        :return: The port_list_rights of this PlatformRights.  # noqa: E501
        :rtype: PortListRights
        """
        return self._port_list_rights

    @port_list_rights.setter
    def port_list_rights(self, port_list_rights):
        """Sets the port_list_rights of this PlatformRights.

        Rights related to port lists.  # noqa: E501

        :param port_list_rights: The port_list_rights of this PlatformRights.  # noqa: E501
        :type: PortListRights
        """

        self._port_list_rights = port_list_rights

    @property
    def proxy_rights(self):
        """Gets the proxy_rights of this PlatformRights.  # noqa: E501

        Rights related to proxies.  # noqa: E501

        :return: The proxy_rights of this PlatformRights.  # noqa: E501
        :rtype: ProxyRights
        """
        return self._proxy_rights

    @proxy_rights.setter
    def proxy_rights(self, proxy_rights):
        """Sets the proxy_rights of this PlatformRights.

        Rights related to proxies.  # noqa: E501

        :param proxy_rights: The proxy_rights of this PlatformRights.  # noqa: E501
        :type: ProxyRights
        """

        self._proxy_rights = proxy_rights

    @property
    def relay_group_rights(self):
        """Gets the relay_group_rights of this PlatformRights.  # noqa: E501

        Rights related to relay groups.  # noqa: E501

        :return: The relay_group_rights of this PlatformRights.  # noqa: E501
        :rtype: RelayGroupRights
        """
        return self._relay_group_rights

    @relay_group_rights.setter
    def relay_group_rights(self, relay_group_rights):
        """Sets the relay_group_rights of this PlatformRights.

        Rights related to relay groups.  # noqa: E501

        :param relay_group_rights: The relay_group_rights of this PlatformRights.  # noqa: E501
        :type: RelayGroupRights
        """

        self._relay_group_rights = relay_group_rights

    @property
    def scan_cache_rights(self):
        """Gets the scan_cache_rights of this PlatformRights.  # noqa: E501

        Rights related to scan cache configurations.  # noqa: E501

        :return: The scan_cache_rights of this PlatformRights.  # noqa: E501
        :rtype: ScanCacheRights
        """
        return self._scan_cache_rights

    @scan_cache_rights.setter
    def scan_cache_rights(self, scan_cache_rights):
        """Sets the scan_cache_rights of this PlatformRights.

        Rights related to scan cache configurations.  # noqa: E501

        :param scan_cache_rights: The scan_cache_rights of this PlatformRights.  # noqa: E501
        :type: ScanCacheRights
        """

        self._scan_cache_rights = scan_cache_rights

    @property
    def scheduled_task_rights(self):
        """Gets the scheduled_task_rights of this PlatformRights.  # noqa: E501

        Rights related to scheduled tasks.  # noqa: E501

        :return: The scheduled_task_rights of this PlatformRights.  # noqa: E501
        :rtype: ScheduledTaskRights
        """
        return self._scheduled_task_rights

    @scheduled_task_rights.setter
    def scheduled_task_rights(self, scheduled_task_rights):
        """Sets the scheduled_task_rights of this PlatformRights.

        Rights related to scheduled tasks.  # noqa: E501

        :param scheduled_task_rights: The scheduled_task_rights of this PlatformRights.  # noqa: E501
        :type: ScheduledTaskRights
        """

        self._scheduled_task_rights = scheduled_task_rights

    @property
    def schedule_rights(self):
        """Gets the schedule_rights of this PlatformRights.  # noqa: E501

        Rights related to schedules.  # noqa: E501

        :return: The schedule_rights of this PlatformRights.  # noqa: E501
        :rtype: ScheduleRights
        """
        return self._schedule_rights

    @schedule_rights.setter
    def schedule_rights(self, schedule_rights):
        """Sets the schedule_rights of this PlatformRights.

        Rights related to schedules.  # noqa: E501

        :param schedule_rights: The schedule_rights of this PlatformRights.  # noqa: E501
        :type: ScheduleRights
        """

        self._schedule_rights = schedule_rights

    @property
    def setting_rights(self):
        """Gets the setting_rights of this PlatformRights.  # noqa: E501

        Rights related to settings.  # noqa: E501

        :return: The setting_rights of this PlatformRights.  # noqa: E501
        :rtype: SettingRights
        """
        return self._setting_rights

    @setting_rights.setter
    def setting_rights(self, setting_rights):
        """Sets the setting_rights of this PlatformRights.

        Rights related to settings.  # noqa: E501

        :param setting_rights: The setting_rights of this PlatformRights.  # noqa: E501
        :type: SettingRights
        """

        self._setting_rights = setting_rights

    @property
    def expert_setting_rights(self):
        """Gets the expert_setting_rights of this PlatformRights.  # noqa: E501

        Rights related to expert settings.  # noqa: E501

        :return: The expert_setting_rights of this PlatformRights.  # noqa: E501
        :rtype: ExpertSettingRights
        """
        return self._expert_setting_rights

    @expert_setting_rights.setter
    def expert_setting_rights(self, expert_setting_rights):
        """Sets the expert_setting_rights of this PlatformRights.

        Rights related to expert settings.  # noqa: E501

        :param expert_setting_rights: The expert_setting_rights of this PlatformRights.  # noqa: E501
        :type: ExpertSettingRights
        """

        self._expert_setting_rights = expert_setting_rights

    @property
    def syslog_configuration_rights(self):
        """Gets the syslog_configuration_rights of this PlatformRights.  # noqa: E501

        Rights related to syslog configurations.  # noqa: E501

        :return: The syslog_configuration_rights of this PlatformRights.  # noqa: E501
        :rtype: SyslogConfigurationRights
        """
        return self._syslog_configuration_rights

    @syslog_configuration_rights.setter
    def syslog_configuration_rights(self, syslog_configuration_rights):
        """Sets the syslog_configuration_rights of this PlatformRights.

        Rights related to syslog configurations.  # noqa: E501

        :param syslog_configuration_rights: The syslog_configuration_rights of this PlatformRights.  # noqa: E501
        :type: SyslogConfigurationRights
        """

        self._syslog_configuration_rights = syslog_configuration_rights

    @property
    def system_information_rights(self):
        """Gets the system_information_rights of this PlatformRights.  # noqa: E501

        Rights related to system information.  # noqa: E501

        :return: The system_information_rights of this PlatformRights.  # noqa: E501
        :rtype: SystemInformationRights
        """
        return self._system_information_rights

    @system_information_rights.setter
    def system_information_rights(self, system_information_rights):
        """Sets the system_information_rights of this PlatformRights.

        Rights related to system information.  # noqa: E501

        :param system_information_rights: The system_information_rights of this PlatformRights.  # noqa: E501
        :type: SystemInformationRights
        """

        self._system_information_rights = system_information_rights

    @property
    def tagging_rights(self):
        """Gets the tagging_rights of this PlatformRights.  # noqa: E501

        Rights related to tagging.  # noqa: E501

        :return: The tagging_rights of this PlatformRights.  # noqa: E501
        :rtype: TaggingRights
        """
        return self._tagging_rights

    @tagging_rights.setter
    def tagging_rights(self, tagging_rights):
        """Sets the tagging_rights of this PlatformRights.

        Rights related to tagging.  # noqa: E501

        :param tagging_rights: The tagging_rights of this PlatformRights.  # noqa: E501
        :type: TaggingRights
        """

        self._tagging_rights = tagging_rights

    @property
    def update_rights(self):
        """Gets the update_rights of this PlatformRights.  # noqa: E501

        Rights related to updates.  # noqa: E501

        :return: The update_rights of this PlatformRights.  # noqa: E501
        :rtype: UpdateRights
        """
        return self._update_rights

    @update_rights.setter
    def update_rights(self, update_rights):
        """Sets the update_rights of this PlatformRights.

        Rights related to updates.  # noqa: E501

        :param update_rights: The update_rights of this PlatformRights.  # noqa: E501
        :type: UpdateRights
        """

        self._update_rights = update_rights

    @property
    def apikey_rights(self):
        """Gets the apikey_rights of this PlatformRights.  # noqa: E501


        :return: The apikey_rights of this PlatformRights.  # noqa: E501
        :rtype: ApiKeyRights
        """
        return self._apikey_rights

    @apikey_rights.setter
    def apikey_rights(self, apikey_rights):
        """Sets the apikey_rights of this PlatformRights.


        :param apikey_rights: The apikey_rights of this PlatformRights.  # noqa: E501
        :type: ApiKeyRights
        """

        self._apikey_rights = apikey_rights

    @property
    def iplist_rights(self):
        """Gets the iplist_rights of this PlatformRights.  # noqa: E501


        :return: The iplist_rights of this PlatformRights.  # noqa: E501
        :rtype: IpListRights
        """
        return self._iplist_rights

    @iplist_rights.setter
    def iplist_rights(self, iplist_rights):
        """Sets the iplist_rights of this PlatformRights.


        :param iplist_rights: The iplist_rights of this PlatformRights.  # noqa: E501
        :type: IpListRights
        """

        self._iplist_rights = iplist_rights

    @property
    def samlidentity_provider_rights(self):
        """Gets the samlidentity_provider_rights of this PlatformRights.  # noqa: E501


        :return: The samlidentity_provider_rights of this PlatformRights.  # noqa: E501
        :rtype: SamlIdentityProviderRights
        """
        return self._samlidentity_provider_rights

    @samlidentity_provider_rights.setter
    def samlidentity_provider_rights(self, samlidentity_provider_rights):
        """Sets the samlidentity_provider_rights of this PlatformRights.


        :param samlidentity_provider_rights: The samlidentity_provider_rights of this PlatformRights.  # noqa: E501
        :type: SamlIdentityProviderRights
        """

        self._samlidentity_provider_rights = samlidentity_provider_rights

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
        if issubclass(PlatformRights, dict):
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
        if not isinstance(other, PlatformRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

