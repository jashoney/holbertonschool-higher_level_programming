#!/usr/bin/python3
""" Studect class defn, to_json fn """


class Student:
    """ setup of class Student """

    def __init__(self, first_name, last_name, age):
        """ instantiation of Student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dict representation of a Student instance
            filters with the attrs list if it is a list of dict keys
        """
        if attrs is None:
            return self.__dict__

        newlist = []
        if type(attrs) is list:
            for i in range(len(attrs)):
                if type(attrs[i]) != str:
                    return self.__dict__

        for attr_key in attrs:
            for key, value in self.__dict__.items():
                if key == attr_key:
                    newlist.append(value)

        return newlist
