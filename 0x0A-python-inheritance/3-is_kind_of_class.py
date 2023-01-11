#!/usr/bin/python3
"""checks if object is an instance of a class
or an inherited class
"""

def is_kind_of_class(obj, a_class):
    """ Function that returns True/False if obj is an
    instance of a_class
        True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
