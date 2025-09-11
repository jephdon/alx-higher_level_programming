#!/usr/bin/python3
"""A module containing the Base class for managing IDs in the
Almost a Circle project.

This module provides the Base class, which serves as the
foundation for other classes, handling the id attribute to
avoid duplication.
"""


class Base:
    """The base class for managing id attributes in all classes
    of the project.

    Attributes:
        __nb_objects (int): A private class attribute to track the
        number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): The ID to assign to the instance.
            Defaults to None.

        Attributes:
            id (int): A public instance attribute set to id if
            provided, else incremented from __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
