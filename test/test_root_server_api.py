# coding: utf-8

"""
    BMLT

    BMLT Admin API Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bmlt_client.api.root_server_api import RootServerApi  # noqa: E501


class TestRootServerApi(unittest.TestCase):
    """RootServerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RootServerApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_auth_logout(self) -> None:
        """Test case for auth_logout

        Revokes a token  # noqa: E501
        """
        pass

    def test_auth_refresh(self) -> None:
        """Test case for auth_refresh

        Revokes and issues a new token  # noqa: E501
        """
        pass

    def test_auth_token(self) -> None:
        """Test case for auth_token

        Creates a token  # noqa: E501
        """
        pass

    def test_create_error_test(self) -> None:
        """Test case for create_error_test

        Tests some errors  # noqa: E501
        """
        pass

    def test_create_format(self) -> None:
        """Test case for create_format

        Creates a format  # noqa: E501
        """
        pass

    def test_create_meeting(self) -> None:
        """Test case for create_meeting

        Creates a meeting  # noqa: E501
        """
        pass

    def test_create_service_body(self) -> None:
        """Test case for create_service_body

        Creates a service body  # noqa: E501
        """
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Creates a user  # noqa: E501
        """
        pass

    def test_delete_format(self) -> None:
        """Test case for delete_format

        Deletes a format  # noqa: E501
        """
        pass

    def test_delete_meeting(self) -> None:
        """Test case for delete_meeting

        Deletes a meeting  # noqa: E501
        """
        pass

    def test_delete_service_body(self) -> None:
        """Test case for delete_service_body

        Deletes a service body  # noqa: E501
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Deletes a user  # noqa: E501
        """
        pass

    def test_get_format(self) -> None:
        """Test case for get_format

        Retrieves a format  # noqa: E501
        """
        pass

    def test_get_formats(self) -> None:
        """Test case for get_formats

        Retrieves formats  # noqa: E501
        """
        pass

    def test_get_meeting(self) -> None:
        """Test case for get_meeting

        Retrieves a meeting  # noqa: E501
        """
        pass

    def test_get_meetings(self) -> None:
        """Test case for get_meetings

        Retrieves meetings  # noqa: E501
        """
        pass

    def test_get_root_server(self) -> None:
        """Test case for get_root_server

        Retrieves a root server  # noqa: E501
        """
        pass

    def test_get_root_servers(self) -> None:
        """Test case for get_root_servers

        Retrieves root servers  # noqa: E501
        """
        pass

    def test_get_service_bodies(self) -> None:
        """Test case for get_service_bodies

        Retrieves service bodies  # noqa: E501
        """
        pass

    def test_get_service_body(self) -> None:
        """Test case for get_service_body

        Retrieves a service body  # noqa: E501
        """
        pass

    def test_get_user(self) -> None:
        """Test case for get_user

        Retrieves a single user  # noqa: E501
        """
        pass

    def test_get_users(self) -> None:
        """Test case for get_users

        Retrieves users  # noqa: E501
        """
        pass

    def test_partial_update_user(self) -> None:
        """Test case for partial_update_user

        Patches a user  # noqa: E501
        """
        pass

    def test_patch_format(self) -> None:
        """Test case for patch_format

        Patches a format  # noqa: E501
        """
        pass

    def test_patch_meeting(self) -> None:
        """Test case for patch_meeting

        Patches a meeting  # noqa: E501
        """
        pass

    def test_patch_service_body(self) -> None:
        """Test case for patch_service_body

        Patches a service body  # noqa: E501
        """
        pass

    def test_update_format(self) -> None:
        """Test case for update_format

        Updates a format  # noqa: E501
        """
        pass

    def test_update_meeting(self) -> None:
        """Test case for update_meeting

        Updates a meeting  # noqa: E501
        """
        pass

    def test_update_service_body(self) -> None:
        """Test case for update_service_body

        Updates a Service Body  # noqa: E501
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update single user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
