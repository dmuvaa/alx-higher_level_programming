#!/usr/bin/python3
class Node:
    """Node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize data and new node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """node data."""

        return self.__data

    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Set the node."""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance (value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        """Initialize a Singly Linked List."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to this list."""

        new = Node(value)
        if self.__head is None:
            new.next_node = self.__head
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define how the string will print itself."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
