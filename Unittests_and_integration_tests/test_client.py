#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        and that get_json is called once with the expected argument
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        expected_url = "https://api.github.com/orgs/test-org/repos"
        mock_payload = {"repos_url": expected_url}

        # Use patch as a context manager to mock GithubOrgClient.org property
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            # Configure the mock to return the mock_payload
            mock_org.return_value = mock_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test-org")

            # Get the public repos URL
            result = client._public_repos_url

            # Verify the URL is correct
            self.assertEqual(result, expected_url)


if __name__ == '__main__':
    unittest.main()
