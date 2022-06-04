#!/usr/bin/python3
""" setting a class Square which inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle which inherits from Base """

    def __init__(self, size, x=0, y=0, id=None):
        """ instance constructor for a Square instance """
        super().__init__(size, size, x, y, id=None)
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, val):
        """ size setter """
        self.width = val
        self.height = val

    def __str__(self):
        """ overriding the str dunder method """
        mystring = f"[Square] ({self.id}) "
        mystring += f"{self.x}/{self.y} - {self.width}"
        return mystring

    def update(self, *args, **kwargs):
        """ assigns new values to the attributes using *args
            if *args is NULL or empty uses **kwargs dict
        """
        if args is not None and len(args) > 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns a dict repr of the square instance """
        newdict = {'id': self.id,
                   'size': self.width,
                   'x': self.x,
                   'y': self.y}
        return newdict
