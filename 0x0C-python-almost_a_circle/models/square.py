#!/usr/bin/python3
"""Class Square inherits from Rectangle"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle.
     Attributes:
        size: width and height of square.
        x: x value.
        y: y value.
        id: identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square

        Args:
            size: width and height of square.
            x: x value.
            y: y value.
            id: identity of square.
        """
        if type(size) != int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints square
        Return:
            [Square] (<id>) <x>/<y> - <size>.
        """
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        Public instance method  returns the current square size.
        Returns: The current square size.
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Public instance method  sets the square width.
        Paramerters:
            value: new width to set width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each class
        attributes.
        Args:
            *args:  the list of arguments.
            **kwargs: A double pointer to a
            dictionary: key/value
        """
        if args is not None and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a square.
        Return: square dictionary.
        """
        dict_squ = {}
        dict_squ["id"] = self.id
        dict_squ["size"] = self.__size
        dict_squ["x"] = self.x
        dict_squ["y"] = self.y
        return dict_squ
