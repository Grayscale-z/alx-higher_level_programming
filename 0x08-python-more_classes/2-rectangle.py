#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
[?1049h[22;0;0t[>4;2m[?1h=[?2004h[?1004h[1;75r[?12h[?12l[22;2t[22;1t[27m[23m[29m[m[H[2J[?25l[75;1H"cat" [New][2;1H[1m[34m~                                                                                                                                                                                                                                                                              [3;1H~                                                                                                                                                                                                                                                                              [4;1H~                                                                                                                                                                                                                                                                              [5;1H~                                                                                                                                                                                                                                                                              [6;1H~                                                                                                                                                                                                                                                                              [7;1H~                                                                                                                                                                                                                                                                              [8;1H~                                                                                                                                                                                                                                                                              [9;1H~                                                                                                                                                                                                                                                                              [10;1H~                                                                                                                                                                                                                                                                              [11;1H~                                                                                                                                                                                                                                                                              [12;1H~                                                                                                                                                                                                                                                                              [13;1H~                                                                                                                                                                                                                                                                              [14;1H~                                                                                                                                                                                                                                                                              [15;1H~                                                                                                                                                                                                                                                                              [16;1H~                                                                                                                                                                                                                                                                              [17;1H~                                                                                                                                                                                                                                                                              [18;1H~                                                                                                                                                                                                                                                                              [19;1H~                                                                                                                                                                                                                                                                              [20;1H~                                                                                                                                                                                                                                                                              [21;1H~                                                                                                                                                                                                                                                                              [22;1H~                                                                                                                                                                                                                                                                              [23;1H~                                                                                                                                                                                                                                                                              [24;1H~                                                                                                                                                                                                                                                                              [25;1H~                                                                                                                                                                                                                                                                              [26;1H~                                                                                                                                                                                                                                                                              [27;1H~                                                                                                                                                                                                                                                                              [28;1H~                                                                                                                                                                                                                                                                              [29;1H~                                                                                                                                                                                                                                                                              [30;1H~                                                                                                                                                                                                                                                                              [31;1H~                                                                                                                                                                                                                                                                              [32;1H~                                                                                                                                                                                                                                                                              [33;1H~                                                                                                                                                                                                                                                                              [34;1H~                                                                                                                                                                                                                                                                              [35;1H~                                                                                                                                                                                                                                                                              [36;1H~                                                                                                                                                                                                                                                                              [37;1H~                                                                                                                                                                                                                                                                              [38;1H~                                                                                                                                                                                                                                                                              [39;1H~                                                                                                                                                                                                                                                                              [40;1H~                                                                                                                                                                                                                                                                              [41;1H~                                                                                                                                                                                                                                                                              [42;1H~                                                                                                                                                                                                                                                                              [43;1H~                                                                                                                                                                                                                                                                              [44;1H~                                                                                                                                                                                                                                                                              [45;1H~                                                                                                                                                                                                                                                                              [46;1H~                                                                                                                                                                                                                                                                              [47;1H~                                                                                                                                                                                                                                                                              [48;1H~                                                                                                                                                                                                                                                                              [49;1H~                                                                                                                                                                                                                                                                              [50;1H~                                                                                                                                                                                                                                                                              [51;1H~                                                                                                                                                                                                                                                                              [52;1H~                                                                                                                                                                                                                                                                              [53;1H~                                                                                                                                                                                                                                                                              [54;1H~                                                                                                                                                                                                                                                                              [55;1H~                                                                                                                                                                                                                                                                              [56;1H~                                                                                                                                                                                                                                                                              [57;1H~                                                                                                                                                                                                                                                                              [58;1H~                                                                                                                                                                                                                                                                              [59;1H~                                                                                                                                                                                                                                                                              [60;1H~                                                                                                                                                                                                                                                                              [61;1H~                                                                                                                                                                                                                                                                              [62;1H~                                                                                                                                                                                                                                                                              [63;1H~                                                                                                                                                                                                                                                                              [64;1H~                                                                                                                                                                                                                                                                              [65;1H~                                                                                                                                                                                                                                                                              [66;1H~                                                                                                                                                                                                                                                                              [67;1H~                                                                                                                                                                                                                                                                              [68;1H~                                                                                                                                                                                                                                                                              [69;1H~                                                                                                                                                                                                                                                                              [70;1H~                                                                                                                                                                                                                                                                              [71;1H~                                                                                                                                                                                                                                                                              [72;1H~                                                                                                                                                                                                                                                                              [73;1H~                                                                                                                                                                                                                                                                              [m[74;1H[1m[7mcat [unix] (00:59 01/01/1970)                                                                                                                                                                                                                                         0,0-1 All[1;1H[?25h[?25l[m[75;261Hc[1;1H[?25h[?25l[75;262Ha[1;1H[?25h[?25l[75;263Ht[1;1H[?5h[?25h[?5l[?25l[75;261H   [1;1H[?25h[?25l[75;261H^[[1;1H[75;261H  [1;1H[75;261H^[[1;1H[?5h[?25h[?5l[?25l[75;261H  [1;1H[?25h[?25l[75;261H^[[1;1H[75;261H  [1;1H[75;261H^[[1;1H[?5h[?25h[?5l[?25l[75;261H  [1;1H[?25h[?25l[75;261H^[[1;1H[75;261H  [1;1H[75;261H^[[1;1H[75;261H  [1;1H[?25h[?25l[75;261H^M[1;1H[?5h[?25h[?5l[?25l[75;261H  [1;1H[?25h[?25l[75;261H^M[1;1H[?5h[?25h[?5l[?25l[75;261H  [1;1H[?25h[?25l[75;261H^M[1;1H[75;261H  [1;1H[?25h[?25l[75;261Hc[1;1H[?25h[?25l[75;262Hc[1;1H[75;261H  [1;1H[75;1H[1m-- INSERT --[m[74;263H[1m[7m  0,1[1;1H[?25h[m[75;1H[K[1;1H[?25l[75;261H^[[1;1H[75;261H  [1;1H[74;263H[1m[7m0,0-1[1;1H[?25h[?25l[m[75;261H^[[1;1H[75;261H  [1;1H[?5h[?25h[?5l[?25l[75;261H^[[1;1H[75;261H  [1;1H[75;261H^[[1;1H[75;261H  [1;1H[?25h[?25l[75;261H:[1;1H[75;261H[K[75;1H:[?25hwq[?25l[?2004l[>4;m"cat" [New][unix] 0L, 0B written[23;2t[23;1t
[?1004l[?2004l[?1l>[?25h[>4;m[?1049l[23;0;0t#!/usr/bin/python3
"""2-rectangle, built for Holberton Python project 0x08 task 2.
"""


class Rectangle:
    """Takes in args for width and height of a rectangle, and contains methods
    for calculation of the area or perimeter.

    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (int): horizontal dimension of rectangle
            __height (int): vertical dimension of rectangle

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
