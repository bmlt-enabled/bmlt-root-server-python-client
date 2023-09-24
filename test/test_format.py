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

from bmlt_client.models.format import Format  # noqa: E501

class TestFormat(unittest.TestCase):
    """Format unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Format:
        """Test Format
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Format`
        """
        model = Format()  # noqa: E501
        if include_optional:
            return Format(
                world_id = 'string',
                type = 'string',
                translations = [
                    bmlt_client.models.format_translation.FormatTranslation(
                        key = '', 
                        name = '', 
                        description = '', 
                        language = '', )
                    ],
                id = 0
            )
        else:
            return Format(
                world_id = 'string',
                type = 'string',
                translations = [
                    bmlt_client.models.format_translation.FormatTranslation(
                        key = '', 
                        name = '', 
                        description = '', 
                        language = '', )
                    ],
                id = 0,
        )
        """

    def testFormat(self):
        """Test Format"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()