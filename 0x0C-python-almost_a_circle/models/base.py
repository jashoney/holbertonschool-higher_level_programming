#!/usr/bin/python3
""" base class definition """


import json


class Base:
    """
        defines the Base class
        private class attribute nb_objects counts instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instance constructor the the class Base
            assigns an id to the insatnce if not given
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string repr of the dict """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes a JSON string repr to a file """
        myfile = cls.__name__ + ".json"
        if list_objs is None:
            mylist = []
        else:
            mylist = [obj.to_dictionary() for obj in list_objs]
        with open(myfile, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(mylist))

    @classmethod
    def create(cls, **dictionary):
        """ returns a class instance with attrs set """
        dummy = cls(1, 1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads from a json file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "r", encoding="utf-8") as f:
            if f:
                rfile = f.read()
            else:
                return []
        mylist = []
        file_read_list = cls.from_json_string(rfile)
        for i in file_read_list:
            mylist.append(cls.create(**i))
        return mylist
