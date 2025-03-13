#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
# Fix the import to explicitly import the fixtures
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
            f"https://api.github.com/orgs/{org_name}"
        )

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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Unit test for GithubOrgClient.public_repos method
        """
        # Define mock return values
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        expected_repos = ["repo1", "repo2", "repo3"]
        test_url = "https://api.github.com/orgs/test-org/repos"

        # Mock the _public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            # Set the return value for the property
            mock_public_repos_url.return_value = test_url

            # Create an instance and call the method
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            # Assert the result matches expected repos
            self.assertEqual(result, expected_repos)

            # Assert that get_json was called once with the right URL
            mock_get_json.assert_called_once_with(test_url)

            # Assert that _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test that GithubOrgClient.has_license returns correct boolean
        based on repo license and given license key
        """
        client = GithubOrgClient("test-org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test cases for GithubOrgClient class"""
    @classmethod
    def setUpClass(cls):
        """Set up class method to mock external requests"""
        # Start patcher for requests.get
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect function to return appropriate responses
        def get_side_effect(url):
            # Mock response object with json() method
            class MockResponse:
                """Mock response class with json method"""

                def __init__(self, json_data):
                    self._json_data = json_data

                def json(self):
                    """Return the json data"""
                    return self._json_data

            # Return appropriate fixture based on URL
            if url.endswith('/orgs/testorg'):
                return MockResponse(cls.org_payload)
            elif url.endswith('/orgs/testorg/repos'):
                return MockResponse(cls.repos_payload)
            return MockResponse({})  # Default empty response

        # Configure mock with side_effect
        cls.mock_get.side_effect = get_side_effect

        # Initialize the client
        cls.client = GithubOrgClient('testorg')

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
