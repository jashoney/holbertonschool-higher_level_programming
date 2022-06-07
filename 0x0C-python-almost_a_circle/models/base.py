#!/usr/bin/python3
""" base class definition """


import json
import csv


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
        if list_dictionaries is None:
            list_dictionaries = []
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
        mylist = []
        if list_objs is not None:
            for i in list_objs:
                if issubclass(type(i), Base):
                    mylist.append(cls.to_dictionary(i))
        with open(myfile, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(mylist))

    @classmethod
    def create(cls, **dictionary):
        """ returns a class instance with attrs set """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads from a json file """
        filename = cls.__name__ + ".json"
        mylist = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                if f:
                    mylist = [cls.create(**obj) for obj in
                              cls.from_json_string(f.read())]
        except Exception:
            pass
        return mylist

@classmethod
    def load_from_file_csv(cls):
        """ loads a list of object from csv file """
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    attributename = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    attributename = ["id", "size", "x", "y"]
                dictreader = csv.DictReader(csvfile, fieldnames=attributename)
                for item in dictreader:
                    item = {k: int(v) for k, v in item.items()}
                    list_objs.append(cls.create(**item))
                return list_objs
        except Exception:
            return list_objs
