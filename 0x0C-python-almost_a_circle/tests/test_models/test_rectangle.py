#!/usr/bin/python3
"""A test module for the base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

import sys
import io


class Testbase(unittest.TestCase):
    """A test case class for the Rectangle class
    """

    def test_id(self):
        """
        test for id
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(3, 4)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)

    def test_width_height(self):
        """
        test for width and height value
        """
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 5)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 5)

        with self.assertRaises(TypeError):
            r = Rectangle(2, '6')
        with self.assertRaises(ValueError):
            r = Rectangle(1, -3)

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(3, 4)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)

        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 4)

    def test_x_y(self):
        """
        test for x and y value
        """
        r = Rectangle(1, 1, 2, 3)

        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.y = -5

        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.x = -5

    def test_area_with_valid_dimensions(self):
        """Test for area valid values
        """
        r1 = Rectangle(3, 2)
        result = r1.area()
        self.assertEqual(result, 6)

    def test_area_with_invalid_dimensions(self):
        """Test for area invalid values
        """
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(None)
        self.assertIn(
            "missing 1 required positional argument: 'height'", str(context.exception))

    def test_area_with_invalid_dimensions2(self):
        """Test for area invalid values
        """
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle("")
        self.assertIn(
            "missing 1 required positional argument: 'height'", str(context.exception))

    def test_display_with_valid_dimensions(self):
        """
        In summary, this test is checking whether the display method of the Rectangle
        class correctly prints a rectangle with a width of 3 and a height of 2. It does
        so by redirecting the standard output, calling the method, capturing the output, and then comparing it to the expected
        output. If the actual and expected outputs match, the test passes; otherwise, it fails.
        """
        saved_output = sys.stdout
        sys.stdout = io.StringIO()

        r = Rectangle(3, 2)
        r.display()
        expected_output = "###\n###\n"
        actual_output = sys.stdout.getvalue()
        self.assertEqual(actual_output, expected_output)
        sys.stdout = saved_output

    def test_display_with_invalid_dimensions(self):
        """Test for display invalid values
        """
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle("")
        self.assertIn(
            "missing 1 required positional argument: 'height'", str(context.exception))

    def test_display_with_invalid_dimensions2(self):
        """Test for display invalid values
        """
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(None)
        self.assertIn(
            "missing 1 required positional argument: 'height'", str(context.exception))

    def test___str___with_valid_dimensions(self):
        """Test for str print
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        actual_string = str(r1)
        expected_output = str('[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(actual_string, expected_output)

    def test___str___with_invalid_dimensions(self):
        """Test for str print invalid values
        """
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(None)
            self.assertIn(
                "missing 1 required positional argument: 'height'", str(context.exception))

    def test_update_with_valid_dimensions(self):
        """check for update
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        actual_string = str(r1)
        expected_output = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(actual_string, expected_output)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary_with_valid_dimensions(self):
        """Test for to_dictionary
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        actual_output = str(s1_dictionary)
        expected_output = "{'id': 4, 'x': 2, 'size': 10, 'y': 1}"
        self.assertEqual(actual_output, expected_output)
