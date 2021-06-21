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


class IntrusionPreventionRule(object):
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
        'minimum_agent_version': 'str',
        'application_type_id': 'int',
        'priority': 'str',
        'severity': 'str',
        'detect_only': 'bool',
        'event_logging_disabled': 'bool',
        'generate_event_on_packet_drop': 'bool',
        'always_include_packet_data': 'bool',
        'debug_mode_enabled': 'bool',
        'type': 'str',
        'original_issue': 'int',
        'last_updated': 'int',
        'identifier': 'str',
        'template': 'str',
        'signature': 'str',
        'start': 'str',
        'patterns': 'list[str]',
        'end': 'str',
        'case_sensitive': 'bool',
        'condition': 'str',
        'action': 'str',
        'custom_xml': 'str',
        'alert_enabled': 'bool',
        'schedule_id': 'int',
        'context_id': 'int',
        'recommendations_mode': 'str',
        'can_be_assigned_alone': 'bool',
        'depends_on_rule_ids': 'list[int]',
        'id': 'int',
        'cvss_score': 'str',
        'cve': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'minimum_agent_version': 'minimumAgentVersion',
        'application_type_id': 'applicationTypeID',
        'priority': 'priority',
        'severity': 'severity',
        'detect_only': 'detectOnly',
        'event_logging_disabled': 'eventLoggingDisabled',
        'generate_event_on_packet_drop': 'generateEventOnPacketDrop',
        'always_include_packet_data': 'alwaysIncludePacketData',
        'debug_mode_enabled': 'debugModeEnabled',
        'type': 'type',
        'original_issue': 'originalIssue',
        'last_updated': 'lastUpdated',
        'identifier': 'identifier',
        'template': 'template',
        'signature': 'signature',
        'start': 'start',
        'patterns': 'patterns',
        'end': 'end',
        'case_sensitive': 'caseSensitive',
        'condition': 'condition',
        'action': 'action',
        'custom_xml': 'customXML',
        'alert_enabled': 'alertEnabled',
        'schedule_id': 'scheduleID',
        'context_id': 'contextID',
        'recommendations_mode': 'recommendationsMode',
        'can_be_assigned_alone': 'canBeAssignedAlone',
        'depends_on_rule_ids': 'dependsOnRuleIDs',
        'id': 'ID',
        'cvss_score': 'CVSSScore',
        'cve': 'CVE'
    }

    def __init__(self, name=None, description=None, minimum_agent_version=None, application_type_id=None, priority=None, severity=None, detect_only=None, event_logging_disabled=None, generate_event_on_packet_drop=None, always_include_packet_data=None, debug_mode_enabled=None, type=None, original_issue=None, last_updated=None, identifier=None, template=None, signature=None, start=None, patterns=None, end=None, case_sensitive=None, condition=None, action=None, custom_xml=None, alert_enabled=None, schedule_id=None, context_id=None, recommendations_mode=None, can_be_assigned_alone=None, depends_on_rule_ids=None, id=None, cvss_score=None, cve=None):  # noqa: E501
        """IntrusionPreventionRule - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._minimum_agent_version = None
        self._application_type_id = None
        self._priority = None
        self._severity = None
        self._detect_only = None
        self._event_logging_disabled = None
        self._generate_event_on_packet_drop = None
        self._always_include_packet_data = None
        self._debug_mode_enabled = None
        self._type = None
        self._original_issue = None
        self._last_updated = None
        self._identifier = None
        self._template = None
        self._signature = None
        self._start = None
        self._patterns = None
        self._end = None
        self._case_sensitive = None
        self._condition = None
        self._action = None
        self._custom_xml = None
        self._alert_enabled = None
        self._schedule_id = None
        self._context_id = None
        self._recommendations_mode = None
        self._can_be_assigned_alone = None
        self._depends_on_rule_ids = None
        self._id = None
        self._cvss_score = None
        self._cve = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if minimum_agent_version is not None:
            self.minimum_agent_version = minimum_agent_version
        if application_type_id is not None:
            self.application_type_id = application_type_id
        if priority is not None:
            self.priority = priority
        if severity is not None:
            self.severity = severity
        if detect_only is not None:
            self.detect_only = detect_only
        if event_logging_disabled is not None:
            self.event_logging_disabled = event_logging_disabled
        if generate_event_on_packet_drop is not None:
            self.generate_event_on_packet_drop = generate_event_on_packet_drop
        if always_include_packet_data is not None:
            self.always_include_packet_data = always_include_packet_data
        if debug_mode_enabled is not None:
            self.debug_mode_enabled = debug_mode_enabled
        if type is not None:
            self.type = type
        if original_issue is not None:
            self.original_issue = original_issue
        if last_updated is not None:
            self.last_updated = last_updated
        if identifier is not None:
            self.identifier = identifier
        if template is not None:
            self.template = template
        if signature is not None:
            self.signature = signature
        if start is not None:
            self.start = start
        if patterns is not None:
            self.patterns = patterns
        if end is not None:
            self.end = end
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if condition is not None:
            self.condition = condition
        if action is not None:
            self.action = action
        if custom_xml is not None:
            self.custom_xml = custom_xml
        if alert_enabled is not None:
            self.alert_enabled = alert_enabled
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if context_id is not None:
            self.context_id = context_id
        if recommendations_mode is not None:
            self.recommendations_mode = recommendations_mode
        if can_be_assigned_alone is not None:
            self.can_be_assigned_alone = can_be_assigned_alone
        if depends_on_rule_ids is not None:
            self.depends_on_rule_ids = depends_on_rule_ids
        if id is not None:
            self.id = id
        if cvss_score is not None:
            self.cvss_score = cvss_score
        if cve is not None:
            self.cve = cve

    @property
    def name(self):
        """Gets the name of this IntrusionPreventionRule.  # noqa: E501

        Name of the IntrusionPreventionRule. Searchable as String.  # noqa: E501

        :return: The name of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntrusionPreventionRule.

        Name of the IntrusionPreventionRule. Searchable as String.  # noqa: E501

        :param name: The name of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this IntrusionPreventionRule.  # noqa: E501

        Description of the IntrusionPreventionRule. Searchable as String.  # noqa: E501

        :return: The description of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IntrusionPreventionRule.

        Description of the IntrusionPreventionRule. Searchable as String.  # noqa: E501

        :param description: The description of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def minimum_agent_version(self):
        """Gets the minimum_agent_version of this IntrusionPreventionRule.  # noqa: E501

        Version of the Deep Security agent or appliance required to support the rule. Searchable as String.  # noqa: E501

        :return: The minimum_agent_version of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._minimum_agent_version

    @minimum_agent_version.setter
    def minimum_agent_version(self, minimum_agent_version):
        """Sets the minimum_agent_version of this IntrusionPreventionRule.

        Version of the Deep Security agent or appliance required to support the rule. Searchable as String.  # noqa: E501

        :param minimum_agent_version: The minimum_agent_version of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._minimum_agent_version = minimum_agent_version

    @property
    def application_type_id(self):
        """Gets the application_type_id of this IntrusionPreventionRule.  # noqa: E501

        ID of the application type for the IntrusionPreventionRule. Searchable as Numeric.  # noqa: E501

        :return: The application_type_id of this IntrusionPreventionRule.  # noqa: E501
        :rtype: int
        """
        return self._application_type_id

    @application_type_id.setter
    def application_type_id(self, application_type_id):
        """Sets the application_type_id of this IntrusionPreventionRule.

        ID of the application type for the IntrusionPreventionRule. Searchable as Numeric.  # noqa: E501

        :param application_type_id: The application_type_id of this IntrusionPreventionRule.  # noqa: E501
        :type: int
        """

        self._application_type_id = application_type_id

    @property
    def priority(self):
        """Gets the priority of this IntrusionPreventionRule.  # noqa: E501

        Priority level of the rule. Higher priority rules are applied before lower priority rules. Searchable as Choice.  # noqa: E501

        :return: The priority of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this IntrusionPreventionRule.

        Priority level of the rule. Higher priority rules are applied before lower priority rules. Searchable as Choice.  # noqa: E501

        :param priority: The priority of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["lowest", "low", "normal", "high", "highest"]  # noqa: E501
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def severity(self):
        """Gets the severity of this IntrusionPreventionRule.  # noqa: E501

        Severity level of the rule. Severity levels can be used as sorting criteria and affect event rankings. Searchable as Choice.  # noqa: E501

        :return: The severity of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this IntrusionPreventionRule.

        Severity level of the rule. Severity levels can be used as sorting criteria and affect event rankings. Searchable as Choice.  # noqa: E501

        :param severity: The severity of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["low", "medium", "high", "critical"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def detect_only(self):
        """Gets the detect_only of this IntrusionPreventionRule.  # noqa: E501

        In detect mode, the rule creates an event log and does not interfere with traffic.  # noqa: E501

        :return: The detect_only of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._detect_only

    @detect_only.setter
    def detect_only(self, detect_only):
        """Sets the detect_only of this IntrusionPreventionRule.

        In detect mode, the rule creates an event log and does not interfere with traffic.  # noqa: E501

        :param detect_only: The detect_only of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._detect_only = detect_only

    @property
    def event_logging_disabled(self):
        """Gets the event_logging_disabled of this IntrusionPreventionRule.  # noqa: E501

        Enable to prevent event logs from being created when the rule is triggered. Not available if detectOnly is true. Searchable as Boolean.  # noqa: E501

        :return: The event_logging_disabled of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._event_logging_disabled

    @event_logging_disabled.setter
    def event_logging_disabled(self, event_logging_disabled):
        """Sets the event_logging_disabled of this IntrusionPreventionRule.

        Enable to prevent event logs from being created when the rule is triggered. Not available if detectOnly is true. Searchable as Boolean.  # noqa: E501

        :param event_logging_disabled: The event_logging_disabled of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._event_logging_disabled = event_logging_disabled

    @property
    def generate_event_on_packet_drop(self):
        """Gets the generate_event_on_packet_drop of this IntrusionPreventionRule.  # noqa: E501

        Generate an event every time a packet is dropped for the rule. Not available if eventLoggingDisabled is true. Searchable as Boolean.  # noqa: E501

        :return: The generate_event_on_packet_drop of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._generate_event_on_packet_drop

    @generate_event_on_packet_drop.setter
    def generate_event_on_packet_drop(self, generate_event_on_packet_drop):
        """Sets the generate_event_on_packet_drop of this IntrusionPreventionRule.

        Generate an event every time a packet is dropped for the rule. Not available if eventLoggingDisabled is true. Searchable as Boolean.  # noqa: E501

        :param generate_event_on_packet_drop: The generate_event_on_packet_drop of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._generate_event_on_packet_drop = generate_event_on_packet_drop

    @property
    def always_include_packet_data(self):
        """Gets the always_include_packet_data of this IntrusionPreventionRule.  # noqa: E501

        Enabled to include package data in the event logs. Not available if eventLoggingDisabled is true. Searchable as Boolean.  # noqa: E501

        :return: The always_include_packet_data of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._always_include_packet_data

    @always_include_packet_data.setter
    def always_include_packet_data(self, always_include_packet_data):
        """Sets the always_include_packet_data of this IntrusionPreventionRule.

        Enabled to include package data in the event logs. Not available if eventLoggingDisabled is true. Searchable as Boolean.  # noqa: E501

        :param always_include_packet_data: The always_include_packet_data of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._always_include_packet_data = always_include_packet_data

    @property
    def debug_mode_enabled(self):
        """Gets the debug_mode_enabled of this IntrusionPreventionRule.  # noqa: E501

        Enable to log additional packets preceeding and following the packet that the rule detected. Not available if eventLoggingDisabled is true. Searchable as Boolean.  # noqa: E501

        :return: The debug_mode_enabled of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._debug_mode_enabled

    @debug_mode_enabled.setter
    def debug_mode_enabled(self, debug_mode_enabled):
        """Sets the debug_mode_enabled of this IntrusionPreventionRule.

        Enable to log additional packets preceeding and following the packet that the rule detected. Not available if eventLoggingDisabled is true. Searchable as Boolean.  # noqa: E501

        :param debug_mode_enabled: The debug_mode_enabled of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._debug_mode_enabled = debug_mode_enabled

    @property
    def type(self):
        """Gets the type of this IntrusionPreventionRule.  # noqa: E501

        Type of IntrusionPreventionRule. Searchable as Choice.  # noqa: E501

        :return: The type of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntrusionPreventionRule.

        Type of IntrusionPreventionRule. Searchable as Choice.  # noqa: E501

        :param type: The type of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["custom", "smart", "vulnerability", "exploit", "hidden", "policy", "info"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def original_issue(self):
        """Gets the original_issue of this IntrusionPreventionRule.  # noqa: E501

        Timestamp of the date the rule was released, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The original_issue of this IntrusionPreventionRule.  # noqa: E501
        :rtype: int
        """
        return self._original_issue

    @original_issue.setter
    def original_issue(self, original_issue):
        """Sets the original_issue of this IntrusionPreventionRule.

        Timestamp of the date the rule was released, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param original_issue: The original_issue of this IntrusionPreventionRule.  # noqa: E501
        :type: int
        """

        self._original_issue = original_issue

    @property
    def last_updated(self):
        """Gets the last_updated of this IntrusionPreventionRule.  # noqa: E501

        Timestamp of the last rule modification, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The last_updated of this IntrusionPreventionRule.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this IntrusionPreventionRule.

        Timestamp of the last rule modification, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param last_updated: The last_updated of this IntrusionPreventionRule.  # noqa: E501
        :type: int
        """

        self._last_updated = last_updated

    @property
    def identifier(self):
        """Gets the identifier of this IntrusionPreventionRule.  # noqa: E501

        Unique identification tag of the rule. Searchable as String.  # noqa: E501

        :return: The identifier of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this IntrusionPreventionRule.

        Unique identification tag of the rule. Searchable as String.  # noqa: E501

        :param identifier: The identifier of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def template(self):
        """Gets the template of this IntrusionPreventionRule.  # noqa: E501

        Type of template for the IntrusionPreventionRule. Applicable only to custom rules.  # noqa: E501

        :return: The template of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this IntrusionPreventionRule.

        Type of template for the IntrusionPreventionRule. Applicable only to custom rules.  # noqa: E501

        :param template: The template of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["signature", "start-end-patterns", "custom"]  # noqa: E501
        if template not in allowed_values:
            raise ValueError(
                "Invalid value for `template` ({0}), must be one of {1}"  # noqa: E501
                .format(template, allowed_values)
            )

        self._template = template

    @property
    def signature(self):
        """Gets the signature of this IntrusionPreventionRule.  # noqa: E501

        Signature of the rule. Applicable to custom rules with template type signature.  # noqa: E501

        :return: The signature of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this IntrusionPreventionRule.

        Signature of the rule. Applicable to custom rules with template type signature.  # noqa: E501

        :param signature: The signature of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def start(self):
        """Gets the start of this IntrusionPreventionRule.  # noqa: E501

        Start pattern of the rule. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :return: The start of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this IntrusionPreventionRule.

        Start pattern of the rule. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :param start: The start of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def patterns(self):
        """Gets the patterns of this IntrusionPreventionRule.  # noqa: E501

        Body patterns of the rule, which must be found between start and end patterns. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :return: The patterns of this IntrusionPreventionRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """Sets the patterns of this IntrusionPreventionRule.

        Body patterns of the rule, which must be found between start and end patterns. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :param patterns: The patterns of this IntrusionPreventionRule.  # noqa: E501
        :type: list[str]
        """

        self._patterns = patterns

    @property
    def end(self):
        """Gets the end of this IntrusionPreventionRule.  # noqa: E501

        End pattern of the rule. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :return: The end of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this IntrusionPreventionRule.

        End pattern of the rule. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :param end: The end of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this IntrusionPreventionRule.  # noqa: E501

        Enable to make signatures and patterns case sensitive. Applicable to custom rules with template type signature or start-end-patterns.  # noqa: E501

        :return: The case_sensitive of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this IntrusionPreventionRule.

        Enable to make signatures and patterns case sensitive. Applicable to custom rules with template type signature or start-end-patterns.  # noqa: E501

        :param case_sensitive: The case_sensitive of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

    @property
    def condition(self):
        """Gets the condition of this IntrusionPreventionRule.  # noqa: E501

        Condition to determine if the rule is triggered. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :return: The condition of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this IntrusionPreventionRule.

        Condition to determine if the rule is triggered. Applicable to custom rules with template type start-end-patterns.  # noqa: E501

        :param condition: The condition of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "any", "none"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def action(self):
        """Gets the action of this IntrusionPreventionRule.  # noqa: E501

        Action to apply if the rule is triggered. Applicable to custom rules with template type signature or start-end-patterns.  # noqa: E501

        :return: The action of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IntrusionPreventionRule.

        Action to apply if the rule is triggered. Applicable to custom rules with template type signature or start-end-patterns.  # noqa: E501

        :param action: The action of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["drop", "log-only"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def custom_xml(self):
        """Gets the custom_xml of this IntrusionPreventionRule.  # noqa: E501

        The custom XML used to define the rule. Applicable to custom rules with template type custom.  # noqa: E501

        :return: The custom_xml of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._custom_xml

    @custom_xml.setter
    def custom_xml(self, custom_xml):
        """Sets the custom_xml of this IntrusionPreventionRule.

        The custom XML used to define the rule. Applicable to custom rules with template type custom.  # noqa: E501

        :param custom_xml: The custom_xml of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._custom_xml = custom_xml

    @property
    def alert_enabled(self):
        """Gets the alert_enabled of this IntrusionPreventionRule.  # noqa: E501

        Enable to raise an alert when the rule logs an event. Searchable as Boolean.  # noqa: E501

        :return: The alert_enabled of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._alert_enabled

    @alert_enabled.setter
    def alert_enabled(self, alert_enabled):
        """Sets the alert_enabled of this IntrusionPreventionRule.

        Enable to raise an alert when the rule logs an event. Searchable as Boolean.  # noqa: E501

        :param alert_enabled: The alert_enabled of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._alert_enabled = alert_enabled

    @property
    def schedule_id(self):
        """Gets the schedule_id of this IntrusionPreventionRule.  # noqa: E501

        ID of the schedule which defines times during which the rule is active. Set to 0 to remove any assignment. Searchable as Numeric.  # noqa: E501

        :return: The schedule_id of this IntrusionPreventionRule.  # noqa: E501
        :rtype: int
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this IntrusionPreventionRule.

        ID of the schedule which defines times during which the rule is active. Set to 0 to remove any assignment. Searchable as Numeric.  # noqa: E501

        :param schedule_id: The schedule_id of this IntrusionPreventionRule.  # noqa: E501
        :type: int
        """

        self._schedule_id = schedule_id

    @property
    def context_id(self):
        """Gets the context_id of this IntrusionPreventionRule.  # noqa: E501

        ID of the context in which the rule is applied. Set to 0 to remove any assignment. Searchable as Numeric.  # noqa: E501

        :return: The context_id of this IntrusionPreventionRule.  # noqa: E501
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """Sets the context_id of this IntrusionPreventionRule.

        ID of the context in which the rule is applied. Set to 0 to remove any assignment. Searchable as Numeric.  # noqa: E501

        :param context_id: The context_id of this IntrusionPreventionRule.  # noqa: E501
        :type: int
        """

        self._context_id = context_id

    @property
    def recommendations_mode(self):
        """Gets the recommendations_mode of this IntrusionPreventionRule.  # noqa: E501

        Indicates whether recommendation scans consider the IntrusionPreventionRule. Can be set to enabled or ignored. Custom rules cannot be recommended. Searchable as Choice.  # noqa: E501

        :return: The recommendations_mode of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._recommendations_mode

    @recommendations_mode.setter
    def recommendations_mode(self, recommendations_mode):
        """Sets the recommendations_mode of this IntrusionPreventionRule.

        Indicates whether recommendation scans consider the IntrusionPreventionRule. Can be set to enabled or ignored. Custom rules cannot be recommended. Searchable as Choice.  # noqa: E501

        :param recommendations_mode: The recommendations_mode of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "ignored", "unknown", "disabled"]  # noqa: E501
        if recommendations_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `recommendations_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(recommendations_mode, allowed_values)
            )

        self._recommendations_mode = recommendations_mode

    @property
    def can_be_assigned_alone(self):
        """Gets the can_be_assigned_alone of this IntrusionPreventionRule.  # noqa: E501

        True when the rule has no dependencies.  # noqa: E501

        :return: The can_be_assigned_alone of this IntrusionPreventionRule.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_assigned_alone

    @can_be_assigned_alone.setter
    def can_be_assigned_alone(self, can_be_assigned_alone):
        """Sets the can_be_assigned_alone of this IntrusionPreventionRule.

        True when the rule has no dependencies.  # noqa: E501

        :param can_be_assigned_alone: The can_be_assigned_alone of this IntrusionPreventionRule.  # noqa: E501
        :type: bool
        """

        self._can_be_assigned_alone = can_be_assigned_alone

    @property
    def depends_on_rule_ids(self):
        """Gets the depends_on_rule_ids of this IntrusionPreventionRule.  # noqa: E501

        IDs of intrusion prevention rules the rule depends on, which will be automatically assigned if this rule is assigned.  # noqa: E501

        :return: The depends_on_rule_ids of this IntrusionPreventionRule.  # noqa: E501
        :rtype: list[int]
        """
        return self._depends_on_rule_ids

    @depends_on_rule_ids.setter
    def depends_on_rule_ids(self, depends_on_rule_ids):
        """Sets the depends_on_rule_ids of this IntrusionPreventionRule.

        IDs of intrusion prevention rules the rule depends on, which will be automatically assigned if this rule is assigned.  # noqa: E501

        :param depends_on_rule_ids: The depends_on_rule_ids of this IntrusionPreventionRule.  # noqa: E501
        :type: list[int]
        """

        self._depends_on_rule_ids = depends_on_rule_ids

    @property
    def id(self):
        """Gets the id of this IntrusionPreventionRule.  # noqa: E501

        ID of the IntrusionPreventionRule. Searchable as ID.  # noqa: E501

        :return: The id of this IntrusionPreventionRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntrusionPreventionRule.

        ID of the IntrusionPreventionRule. Searchable as ID.  # noqa: E501

        :param id: The id of this IntrusionPreventionRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cvss_score(self):
        """Gets the cvss_score of this IntrusionPreventionRule.  # noqa: E501

        A measure of the severity of the vulnerability according the National Vulnerability Database. Searchable as String or as Numeric.  # noqa: E501

        :return: The cvss_score of this IntrusionPreventionRule.  # noqa: E501
        :rtype: str
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """Sets the cvss_score of this IntrusionPreventionRule.

        A measure of the severity of the vulnerability according the National Vulnerability Database. Searchable as String or as Numeric.  # noqa: E501

        :param cvss_score: The cvss_score of this IntrusionPreventionRule.  # noqa: E501
        :type: str
        """

        self._cvss_score = cvss_score

    @property
    def cve(self):
        """Gets the cve of this IntrusionPreventionRule.  # noqa: E501

        List of CVEs associated with the IntrusionPreventionRule. Searchable as String.  # noqa: E501

        :return: The cve of this IntrusionPreventionRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this IntrusionPreventionRule.

        List of CVEs associated with the IntrusionPreventionRule. Searchable as String.  # noqa: E501

        :param cve: The cve of this IntrusionPreventionRule.  # noqa: E501
        :type: list[str]
        """

        self._cve = cve

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
        if issubclass(IntrusionPreventionRule, dict):
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
        if not isinstance(other, IntrusionPreventionRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

