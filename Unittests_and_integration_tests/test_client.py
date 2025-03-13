#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up class method that starts the patcher for requests.get"""
        def get_json_side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            if url == cls.org_payload.get("repos_url"):
                return cls.repos_payload
            return None

        # Start patcher for requests.get
        cls.get_patcher = patch('client.requests.get')
        mock_get = cls.get_patcher.start()

        # Configure the mock to return an object with a json() method
        mock_response = mock_get.return_value
        mock_response.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method that stops the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for public_repos method"""
        # Create client instance
        client = GithubOrgClient("google")

        # Test public_repos without license filter
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for public_repos method with license filter"""
        # Create client instance
        client = GithubOrgClient("google")

        # Test public_repos with apache2 license filter
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
