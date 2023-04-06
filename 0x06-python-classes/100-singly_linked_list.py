#!/usr/bin/python3
class Node:

    def __init__(self, data):
        self.data = data


    @property
    def data(self):

        return self.__data

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        return self.data

    @data.setter
    def next_node(self, value):

        if not None(self, Node):
            raise TypeError("next_node must be a Node object")
        self.__node = value

    def __init__(self, data, next_node=None):
        self.__data = data
        self.next_node = None

class SinglyLinkedList:
    head = 0

    def __init__(self):
        print()

    def sorted_insert(self, value):

