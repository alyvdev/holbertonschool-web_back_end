#!/usr/bin/env python3
"""Tests for the utils module."""
import unittest
from unittest.mock import patch
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """Test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path_map),
                         result_expec)

    @parameterized.expand([
        ({}, ("a",), "KeyError('a')"),
        ({"a": 1}, ("a", "b"), "KeyError('b')")
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, error_message):
        """Test that KeyError is raised properly"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception),
                         error_message.split('(')[1][:-1])


class TestGetJson(unittest.TestCase):
    """Tests for the get_json method."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, result_expec):
        """Test get_json method"""

        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = result_expec
            self.assertEqual(get_json(test_url), result_expec)
            mock_request.assert_called_once()
