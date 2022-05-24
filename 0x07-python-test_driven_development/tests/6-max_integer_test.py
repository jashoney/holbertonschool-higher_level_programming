#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ 
    this is a class unittest for the max_integer fn
    """
    def test_list_has_one_element(self):
        """ list has only 1 element """
        my_list = [5]
        self.assertEqual(max_integer(my_list), 5)

    def test_first_element_is_largest(self):
        """ test largest as the first element """
        my_list = [99, 0, -2, 98]
        self.assertEqual(max_integer(my_list), 99)

    def test_middle_element_is_largest(self):
        """ move the largest into the middle of the list """
        my_list = [0, 99, -2, 98]
        self.assertEqual(max_integer(my_list), 99)

    def test_last_element_is_largest(self):
        """ move the largest into the end of the list """
        my_list = [0, -2, 99]
        self.assertEqual(max_integer(my_list), 99)

    def test_largest_is_a_negative_number(self):
        """ check for negative numbers """
        my_list = [-1, -98, -2, -99]
        self.assertEqual(max_integer(my_list), -1)

    def test_function_doc(self):
        """docstring for function test """
        doc = max_integer.__doc__
        self.assertTrue(len(doc) > 3)

    def test_module_doc(self):
        """docstring for module test """
        doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(doc) > 3)

    def test_list_is_empty(self):
        """ list is empty """
        my_list = []
        self.assertIsNone(max_integer(my_list))

    def test_list_has_a_non_integer(self):
        """ list has a string """
        my_list = [1, 3, "hello", 5]
        with self.assertRaises(TypeError):
            max_integer(my_list)

    def test_None(self):
        """ use None as input """
        list is None
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
