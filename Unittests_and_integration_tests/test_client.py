#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch
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
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        and that get_json is called once with the expected argument
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
