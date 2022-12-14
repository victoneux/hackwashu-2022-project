# coding: utf-8

"""
    Priceless Planet Data Services API

    A platform to calculate user's sustainability metrics  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: apisupport@mastercard.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.image import Image  # noqa: E501
from openapi_client.rest import ApiException

class TestImage(unittest.TestCase):
    """Image unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Image
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.image.Image()  # noqa: E501
        if include_optional :
            return Image(
                url = 'https:image'
            )
        else :
            return Image(
        )

    def testImage(self):
        """Test Image"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
