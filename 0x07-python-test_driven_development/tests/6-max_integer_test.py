#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ 
    this is a unittest for max_integer
    """

    def list_is_empty(self):
        """ list is empty """
        my_list = []
        self.assertIsNone(max_integer(my_list))


    def list_has_one_element(self):
        """ list has only 1 element """
        my_list = [5]
        self.assertEqual(max_integer(my_list), 5)


    def first_element_is_largest(self):
        """ test largest as the first element """
        my_list = [99, 0, -2, 98]
        eslf.assertEqual(max_integer(my_list, 99))


    def middle_element_is_largest(self):
        """ move the largest into the middle of the list """
        my_list = [0, 99, -2, 98]
        eslf.assertEqual(max_integer(my_list, 99))


    def last_element_is_largest(self):
        """ move the largest into the middle of the list """
        my_list = [0, 98, -2, 99]
        eslf.assertEqual(max_integer(my_list, 99))


    def largest_is_a_negative_number(self):
        """ move the largest into the middle of the list """
        my_list = [-1, -98, -2, -99]
        eslf.assertEqual(max_integer(my_list, -1))


    def function_doc(self):
        """docstring for function test """
        f = max_integer.__doc__
        self.assertTrue(len(f) > 3)


    def module_doc(self):
        """docstring for module """
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 3)


if __name__ == "__main__":
    unittest.main()
