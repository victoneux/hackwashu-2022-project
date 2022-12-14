# coding: utf-8

"""
    Priceless Planet Data Services API

    A platform to calculate user's sustainability metrics  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class Error(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'source': 'str',
        'reason_code': 'str',
        'description': 'str',
        'recoverable': 'bool',
        'details': 'str'
    }

    attribute_map = {
        'source': 'Source',
        'reason_code': 'ReasonCode',
        'description': 'Description',
        'recoverable': 'Recoverable',
        'details': 'Details'
    }

    def __init__(self, source=None, reason_code=None, description=None, recoverable=None, details=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._reason_code = None
        self._description = None
        self._recoverable = None
        self._details = None
        self.discriminator = None

        self.source = source
        self.reason_code = reason_code
        self.description = description
        self.recoverable = recoverable
        if details is not None:
            self.details = details

    @property
    def source(self):
        """Gets the source of this Error.  # noqa: E501

        The application name that generated this error. Every error message that is generated and returned by the gateway will have this field equal to Gateway.  # noqa: E501

        :return: The source of this Error.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Error.

        The application name that generated this error. Every error message that is generated and returned by the gateway will have this field equal to Gateway.  # noqa: E501

        :param source: The source of this Error.  # noqa: E501
        :type source: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) > 100):
            raise ValueError("Invalid value for `source`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source is not None and len(source) < 1):
            raise ValueError("Invalid value for `source`, length must be greater than or equal to `1`")  # noqa: E501

        self._source = source

    @property
    def reason_code(self):
        """Gets the reason_code of this Error.  # noqa: E501

        A unique constant identifying the error case encountered during request processing.  # noqa: E501

        :return: The reason_code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this Error.

        A unique constant identifying the error case encountered during request processing.  # noqa: E501

        :param reason_code: The reason_code of this Error.  # noqa: E501
        :type reason_code: str
        """
        if self.local_vars_configuration.client_side_validation and reason_code is None:  # noqa: E501
            raise ValueError("Invalid value for `reason_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reason_code is not None and len(reason_code) > 100):
            raise ValueError("Invalid value for `reason_code`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reason_code is not None and len(reason_code) < 1):
            raise ValueError("Invalid value for `reason_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._reason_code = reason_code

    @property
    def description(self):
        """Gets the description of this Error.  # noqa: E501

        Short description of the ReasonCode field.  # noqa: E501

        :return: The description of this Error.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Error.

        Short description of the ReasonCode field.  # noqa: E501

        :param description: The description of this Error.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 10):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `10`")  # noqa: E501

        self._description = description

    @property
    def recoverable(self):
        """Gets the recoverable of this Error.  # noqa: E501

        Indicates whether this error will always be returned for this request, or retrying could change the outcome.  # noqa: E501

        :return: The recoverable of this Error.  # noqa: E501
        :rtype: bool
        """
        return self._recoverable

    @recoverable.setter
    def recoverable(self, recoverable):
        """Sets the recoverable of this Error.

        Indicates whether this error will always be returned for this request, or retrying could change the outcome.  # noqa: E501

        :param recoverable: The recoverable of this Error.  # noqa: E501
        :type recoverable: bool
        """
        if self.local_vars_configuration.client_side_validation and recoverable is None:  # noqa: E501
            raise ValueError("Invalid value for `recoverable`, must not be `None`")  # noqa: E501

        self._recoverable = recoverable

    @property
    def details(self):
        """Gets the details of this Error.  # noqa: E501

        (Optional) Where appropriate, indicates detailed information about data received and calculated during request processing, to help the user with diagnosing errors.  # noqa: E501

        :return: The details of this Error.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Error.

        (Optional) Where appropriate, indicates detailed information about data received and calculated during request processing, to help the user with diagnosing errors.  # noqa: E501

        :param details: The details of this Error.  # noqa: E501
        :type details: str
        """
        if (self.local_vars_configuration.client_side_validation and
                details is not None and len(details) > 5000):
            raise ValueError("Invalid value for `details`, length must be less than or equal to `5000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                details is not None and len(details) < 0):
            raise ValueError("Invalid value for `details`, length must be greater than or equal to `0`")  # noqa: E501

        self._details = details

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
