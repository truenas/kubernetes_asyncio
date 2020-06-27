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


class V1alpha1Endpoint(object):
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
        'addresses': 'list[str]',
        'conditions': 'V1alpha1EndpointConditions',
        'hostname': 'str',
        'target_ref': 'V1ObjectReference',
        'topology': 'dict(str, str)'
    }

    attribute_map = {
        'addresses': 'addresses',
        'conditions': 'conditions',
        'hostname': 'hostname',
        'target_ref': 'targetRef',
        'topology': 'topology'
    }

    def __init__(self, addresses=None, conditions=None, hostname=None, target_ref=None, topology=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Endpoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._conditions = None
        self._hostname = None
        self._target_ref = None
        self._topology = None
        self.discriminator = None

        self.addresses = addresses
        if conditions is not None:
            self.conditions = conditions
        if hostname is not None:
            self.hostname = hostname
        if target_ref is not None:
            self.target_ref = target_ref
        if topology is not None:
            self.topology = topology

    @property
    def addresses(self):
        """Gets the addresses of this V1alpha1Endpoint.  # noqa: E501

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. This allows for cases like dual-stack (IPv4 and IPv6) networking. Consumers (e.g. kube-proxy) must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.  # noqa: E501

        :return: The addresses of this V1alpha1Endpoint.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V1alpha1Endpoint.

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. This allows for cases like dual-stack (IPv4 and IPv6) networking. Consumers (e.g. kube-proxy) must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.  # noqa: E501

        :param addresses: The addresses of this V1alpha1Endpoint.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and addresses is None:  # noqa: E501
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1Endpoint.  # noqa: E501


        :return: The conditions of this V1alpha1Endpoint.  # noqa: E501
        :rtype: V1alpha1EndpointConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1Endpoint.


        :param conditions: The conditions of this V1alpha1Endpoint.  # noqa: E501
        :type: V1alpha1EndpointConditions
        """

        self._conditions = conditions

    @property
    def hostname(self):
        """Gets the hostname of this V1alpha1Endpoint.  # noqa: E501

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.  # noqa: E501

        :return: The hostname of this V1alpha1Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1alpha1Endpoint.

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must pass DNS Label (RFC 1123) validation.  # noqa: E501

        :param hostname: The hostname of this V1alpha1Endpoint.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def target_ref(self):
        """Gets the target_ref of this V1alpha1Endpoint.  # noqa: E501


        :return: The target_ref of this V1alpha1Endpoint.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref):
        """Sets the target_ref of this V1alpha1Endpoint.


        :param target_ref: The target_ref of this V1alpha1Endpoint.  # noqa: E501
        :type: V1ObjectReference
        """

        self._target_ref = target_ref

    @property
    def topology(self):
        """Gets the topology of this V1alpha1Endpoint.  # noqa: E501

        topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node   where the endpoint is located. This should match the corresponding   node label. * topology.kubernetes.io/zone: the value indicates the zone where the   endpoint is located. This should match the corresponding node label. * topology.kubernetes.io/region: the value indicates the region where the   endpoint is located. This should match the corresponding node label.  # noqa: E501

        :return: The topology of this V1alpha1Endpoint.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """Sets the topology of this V1alpha1Endpoint.

        topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node   where the endpoint is located. This should match the corresponding   node label. * topology.kubernetes.io/zone: the value indicates the zone where the   endpoint is located. This should match the corresponding node label. * topology.kubernetes.io/region: the value indicates the region where the   endpoint is located. This should match the corresponding node label.  # noqa: E501

        :param topology: The topology of this V1alpha1Endpoint.  # noqa: E501
        :type: dict(str, str)
        """

        self._topology = topology

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
        if not isinstance(other, V1alpha1Endpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Endpoint):
            return True

        return self.to_dict() != other.to_dict()
