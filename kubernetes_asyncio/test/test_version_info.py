# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.models.version_info import VersionInfo  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestVersionInfo(unittest.TestCase):
    """VersionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVersionInfo(self):
        """Test VersionInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = kubernetes_asyncio.client.models.version_info.VersionInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()