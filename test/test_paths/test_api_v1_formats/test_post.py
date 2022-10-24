# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import bmlt_client
from bmlt_client.paths.api_v1_formats import post  # noqa: E501
from bmlt_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1Formats(ApiTestMixin, unittest.TestCase):
    """
    ApiV1Formats unit test stubs
        Creates a format  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
