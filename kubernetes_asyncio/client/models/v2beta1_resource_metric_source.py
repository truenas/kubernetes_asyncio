# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V2beta1ResourceMetricSource(object):
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
        'name': 'str',
        'target_average_utilization': 'int',
        'target_average_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'target_average_utilization': 'targetAverageUtilization',
        'target_average_value': 'targetAverageValue'
    }

    def __init__(self, name=None, target_average_utilization=None, target_average_value=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1ResourceMetricSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._target_average_utilization = None
        self._target_average_value = None
        self.discriminator = None

        self.name = name
        if target_average_utilization is not None:
            self.target_average_utilization = target_average_utilization
        if target_average_value is not None:
            self.target_average_value = target_average_value

    @property
    def name(self):
        """Gets the name of this V2beta1ResourceMetricSource.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this V2beta1ResourceMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2beta1ResourceMetricSource.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this V2beta1ResourceMetricSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def target_average_utilization(self):
        """Gets the target_average_utilization of this V2beta1ResourceMetricSource.  # noqa: E501

        targetAverageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :return: The target_average_utilization of this V2beta1ResourceMetricSource.  # noqa: E501
        :rtype: int
        """
        return self._target_average_utilization

    @target_average_utilization.setter
    def target_average_utilization(self, target_average_utilization):
        """Sets the target_average_utilization of this V2beta1ResourceMetricSource.

        targetAverageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :param target_average_utilization: The target_average_utilization of this V2beta1ResourceMetricSource.  # noqa: E501
        :type: int
        """

        self._target_average_utilization = target_average_utilization

    @property
    def target_average_value(self):
        """Gets the target_average_value of this V2beta1ResourceMetricSource.  # noqa: E501

        targetAverageValue is the target value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the \"pods\" metric source type.  # noqa: E501

        :return: The target_average_value of this V2beta1ResourceMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._target_average_value

    @target_average_value.setter
    def target_average_value(self, target_average_value):
        """Sets the target_average_value of this V2beta1ResourceMetricSource.

        targetAverageValue is the target value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the \"pods\" metric source type.  # noqa: E501

        :param target_average_value: The target_average_value of this V2beta1ResourceMetricSource.  # noqa: E501
        :type: str
        """

        self._target_average_value = target_average_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2beta1ResourceMetricSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1ResourceMetricSource):
            return True

        return self.to_dict() != other.to_dict()
