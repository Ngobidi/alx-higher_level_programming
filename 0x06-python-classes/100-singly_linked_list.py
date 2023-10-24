#!/usr/bin/python3

"""Define classes for a singly-linked list.
    data must be an integer.
    next_node must be a Node object.
    else TypeError
"""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new_Node.

        Args:
            data (int): The data of the new_Node.
            next_node (Node): The next node of the new_Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new Singly_Linked_List."""
        self.__head = None

    def sorted_insert(self, value):
        """Input a new_Node to the Singly_Linked_List.

        The node is inputed into the list at the correct
        numericals position.

        Args:
            value (Node): The new_Node to input.
        """
        result = Node(value)
        if self.__head is None:
            result.next_node = None
            self.__head = result
        elif self.__head.data > value:
            result.next_node = self.__head
            self.__head = result
        else:
            p = self.__head
            while (p.next_node is not None and
                    p.next_node.data < value):
                p = p.next_node
            result.next_node = p.next_node
            p.next_node = result

    def __str__(self):
        """Define the print() representations of a Singly_Linked_List."""
        values = []
        p = self.__head
        while p is not None:
            values.append(str(p.data))
            p = p.next_node
        return ('\n'.join(values))
