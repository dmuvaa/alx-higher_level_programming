#!/user/bin/python3

"""Creates a class."""


class Base:
    """creates a class called Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
