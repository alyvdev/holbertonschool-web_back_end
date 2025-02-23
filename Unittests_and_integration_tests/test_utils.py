#!/usr/bin/env python3
"""Tests for the utils module."""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """Test access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path_map), result_expec)

    @parameterized.expand([
        ({}, ("a",), "KeyError('a')"),
        ({"a": 1}, ("a", "b"), "KeyError('b')")
    ])
    def test_access_nested_map_exception(self, nested_map, path, error_message):
        """Test that KeyError is raised properly"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), error_message.split('(')[1][:-1])
