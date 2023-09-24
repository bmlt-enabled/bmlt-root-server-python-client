# coding: utf-8

"""
    BMLT

    BMLT Admin API Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from bmlt_client.models.format_translation import FormatTranslation  # noqa: E501

class TestFormatTranslation(unittest.TestCase):
    """FormatTranslation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormatTranslation:
        """Test FormatTranslation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormatTranslation`
        """
        model = FormatTranslation()  # noqa: E501
        if include_optional:
            return FormatTranslation(
                key = '',
                name = '',
                description = '',
                language = ''
            )
        else:
            return FormatTranslation(
                key = '',
                name = '',
                description = '',
                language = '',
        )
        """

    def testFormatTranslation(self):
        """Test FormatTranslation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
