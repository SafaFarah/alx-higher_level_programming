#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base.
    Attributes:
        width: The width  of a rectangle
        width: The height  of a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The constructor for rectangle  class.

        Parameters:
            width: The width  of a rectangle.
            width: The height  of a rectangle.
            x: X-axis
            y: Y-axis
            id:
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Public instance method  returns the current rectangle width.
        Returns: The current rectangle width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Public instance method  sets the rectangle width..
        Paramerters:
            value: new width to set width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Public instance method  returns the current rectangle height.

        Returns: The current rectangle height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Public instance method  sets the rectangle height.

        Paramerters:
            value: new size to set rectangle height.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Public instance method  returns the current x value.
        Returns: The current x value.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Public instance method  sets the x value.

        Paramerters:
            value: new x-axis.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Public instance method  returns the current y value.
        Returns: The current y value.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Public instance method  sets y value.
        Paramerters:
            value: new y-axis.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public instance method  returns the current rectangle  area.
        Return: the area value of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints the rectangle  with the #
        character.
        """
        rectangle = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for k in range(self.__y):
            rectangle.append("\n")
        for i in range(self.__height):
            for n in range(self.__x):
                rectangle.append(" ")
            for j in range(self.__width):
                rectangle.append('#')
            rectangle.append("\n")
        rectangle.pop()
        print("".join(rectangle))

    def __str__(self):
        """
        method so that it returns [Rectangle]
        (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each class
        attributes.
        Args:
            *args: list of arguments to class
            attributes.
            **kwargs: A double pointer to a
            dictionary: key/value
        """
        if args is not None and len(args) != 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle.
        Return: Rectangle dictionary.
        """
        dict_rect = {}
        dict_rect["id"] = self.id
        dict_rect["width"] = self.__width
        dict_rect["height"] = self.__height
        dict_rect["x"] = self.__x
        dict_rect["y"] = self.__y
        return dict_rect
