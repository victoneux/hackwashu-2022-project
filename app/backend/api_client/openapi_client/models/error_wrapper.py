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


class ErrorWrapper(object):
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
        'errors': 'Errors'
    }

    attribute_map = {
        'errors': 'Errors'
    }

    def __init__(self, errors=None, local_vars_configuration=None):  # noqa: E501
        """ErrorWrapper - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self.discriminator = None

        self.errors = errors

    @property
    def errors(self):
        """Gets the errors of this ErrorWrapper.  # noqa: E501


        :return: The errors of this ErrorWrapper.  # noqa: E501
        :rtype: Errors
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ErrorWrapper.


        :param errors: The errors of this ErrorWrapper.  # noqa: E501
        :type errors: Errors
        """
        if self.local_vars_configuration.client_side_validation and errors is None:  # noqa: E501
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

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
        if not isinstance(other, ErrorWrapper):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorWrapper):
            return True

        return self.to_dict() != other.to_dict()
