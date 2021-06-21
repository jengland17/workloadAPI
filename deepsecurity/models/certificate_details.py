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


class CertificateDetails(object):
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
        'issuer_dn': 'str',
        'subject_dn': 'str',
        'not_before': 'int',
        'not_after': 'int',
        'serial_number': 'str',
        'sha1_fingerprint': 'str',
        'sha256_fingerprint': 'str'
    }

    attribute_map = {
        'issuer_dn': 'issuerDN',
        'subject_dn': 'subjectDN',
        'not_before': 'notBefore',
        'not_after': 'notAfter',
        'serial_number': 'serialNumber',
        'sha1_fingerprint': 'sha1Fingerprint',
        'sha256_fingerprint': 'sha256Fingerprint'
    }

    def __init__(self, issuer_dn=None, subject_dn=None, not_before=None, not_after=None, serial_number=None, sha1_fingerprint=None, sha256_fingerprint=None):  # noqa: E501
        """CertificateDetails - a model defined in Swagger"""  # noqa: E501

        self._issuer_dn = None
        self._subject_dn = None
        self._not_before = None
        self._not_after = None
        self._serial_number = None
        self._sha1_fingerprint = None
        self._sha256_fingerprint = None
        self.discriminator = None

        if issuer_dn is not None:
            self.issuer_dn = issuer_dn
        if subject_dn is not None:
            self.subject_dn = subject_dn
        if not_before is not None:
            self.not_before = not_before
        if not_after is not None:
            self.not_after = not_after
        if serial_number is not None:
            self.serial_number = serial_number
        if sha1_fingerprint is not None:
            self.sha1_fingerprint = sha1_fingerprint
        if sha256_fingerprint is not None:
            self.sha256_fingerprint = sha256_fingerprint

    @property
    def issuer_dn(self):
        """Gets the issuer_dn of this CertificateDetails.  # noqa: E501

        The certificate issuer.  # noqa: E501

        :return: The issuer_dn of this CertificateDetails.  # noqa: E501
        :rtype: str
        """
        return self._issuer_dn

    @issuer_dn.setter
    def issuer_dn(self, issuer_dn):
        """Sets the issuer_dn of this CertificateDetails.

        The certificate issuer.  # noqa: E501

        :param issuer_dn: The issuer_dn of this CertificateDetails.  # noqa: E501
        :type: str
        """

        self._issuer_dn = issuer_dn

    @property
    def subject_dn(self):
        """Gets the subject_dn of this CertificateDetails.  # noqa: E501

        The certificate subject (owner).  # noqa: E501

        :return: The subject_dn of this CertificateDetails.  # noqa: E501
        :rtype: str
        """
        return self._subject_dn

    @subject_dn.setter
    def subject_dn(self, subject_dn):
        """Sets the subject_dn of this CertificateDetails.

        The certificate subject (owner).  # noqa: E501

        :param subject_dn: The subject_dn of this CertificateDetails.  # noqa: E501
        :type: str
        """

        self._subject_dn = subject_dn

    @property
    def not_before(self):
        """Gets the not_before of this CertificateDetails.  # noqa: E501

        The date on which the certificate validity period begins.  # noqa: E501

        :return: The not_before of this CertificateDetails.  # noqa: E501
        :rtype: int
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this CertificateDetails.

        The date on which the certificate validity period begins.  # noqa: E501

        :param not_before: The not_before of this CertificateDetails.  # noqa: E501
        :type: int
        """

        self._not_before = not_before

    @property
    def not_after(self):
        """Gets the not_after of this CertificateDetails.  # noqa: E501

        The date on which the certificate validity period ends.  # noqa: E501

        :return: The not_after of this CertificateDetails.  # noqa: E501
        :rtype: int
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this CertificateDetails.

        The date on which the certificate validity period ends.  # noqa: E501

        :param not_after: The not_after of this CertificateDetails.  # noqa: E501
        :type: int
        """

        self._not_after = not_after

    @property
    def serial_number(self):
        """Gets the serial_number of this CertificateDetails.  # noqa: E501

        A number that uniquely identifies the certificate and is issued by the certification authority.  # noqa: E501

        :return: The serial_number of this CertificateDetails.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CertificateDetails.

        A number that uniquely identifies the certificate and is issued by the certification authority.  # noqa: E501

        :param serial_number: The serial_number of this CertificateDetails.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def sha1_fingerprint(self):
        """Gets the sha1_fingerprint of this CertificateDetails.  # noqa: E501

        The sha1 fingerprint of the certificate.  # noqa: E501

        :return: The sha1_fingerprint of this CertificateDetails.  # noqa: E501
        :rtype: str
        """
        return self._sha1_fingerprint

    @sha1_fingerprint.setter
    def sha1_fingerprint(self, sha1_fingerprint):
        """Sets the sha1_fingerprint of this CertificateDetails.

        The sha1 fingerprint of the certificate.  # noqa: E501

        :param sha1_fingerprint: The sha1_fingerprint of this CertificateDetails.  # noqa: E501
        :type: str
        """

        self._sha1_fingerprint = sha1_fingerprint

    @property
    def sha256_fingerprint(self):
        """Gets the sha256_fingerprint of this CertificateDetails.  # noqa: E501

        The sha256 fingerprint of the certificate.  # noqa: E501

        :return: The sha256_fingerprint of this CertificateDetails.  # noqa: E501
        :rtype: str
        """
        return self._sha256_fingerprint

    @sha256_fingerprint.setter
    def sha256_fingerprint(self, sha256_fingerprint):
        """Sets the sha256_fingerprint of this CertificateDetails.

        The sha256 fingerprint of the certificate.  # noqa: E501

        :param sha256_fingerprint: The sha256_fingerprint of this CertificateDetails.  # noqa: E501
        :type: str
        """

        self._sha256_fingerprint = sha256_fingerprint

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
        if issubclass(CertificateDetails, dict):
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
        if not isinstance(other, CertificateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

