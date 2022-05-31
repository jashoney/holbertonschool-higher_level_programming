#!/usr/bin/python3
""" Studect class defn, to_json fn """


class Student:
    """ setup of class Student """

    def __init__(self, first_name, last_name, age):
        """ instantiation of Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dict representation of a Student instance """
        return self.__dict__
