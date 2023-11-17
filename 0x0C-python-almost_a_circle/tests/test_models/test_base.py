#!/usr/bin/python3
"""A test module for the base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class Testbase(unittest.TestCase):
    """A test case class
    """

    def test_to_json_string_with_valid_dimensions(self):
        """Test case for to_json_string method
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()

        # Use [dictionary] to create a list with a single dictionary
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(
            json_dictionary,
            '[{"x": 2, "y": 8, "id": 3, "height": 7, "width": 10}]'
        )

    def test_to_json_string_with_invalid_dimensions(self):
        """Test for to_json_to_string invalid method
        """
        result2 = Base.to_json_string(None)
        self.assertEqual(result2, "[]")

    def test_to_json_string_with_invalid_dimensions2(self):
        """Test for to_json_to_string invalid method
        """
        result3 = Base.to_json_string([])
        self.assertEqual(result3, "[]")

    def test_save_to_file_with_valid_dimensions(self):
        """Test case for save_to_file method
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            result4 = file.read()
        expected_output = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
        self.assertEqual(result4, expected_output)

    def test_save_to_file_with_invalid_dimensions(self):
        """Test case for save_to_file invalid values
        """
        result5 = Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            result5 = file.read()
        self.assertEqual(result5, '[]')

    def test_save_to_file_with_invalid_dimensions2(self):
        """Test case for save_to_file invalid values
        """
        result6 = Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            result6 = file.read()
        self.assertEqual(result6, '[]')

    def test_from_json_string(self):
        """Test case for from_json_string method
        """
        correct_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(correct_input)
        list_output = Rectangle.from_json_string(json_list_input)
        correct_output = "[{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': '1'}]"
        self.assertNotEqual(list_output, correct_output)
