#!/usr/bin/python3

class Node:
    """
    This class defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance with data and an optional next_node.

        Args:
            data (int): The data for the node.
            next_node (Node,optional): Next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node of the current node.

        Args:
            value (Node): The next node, which should be a Node object.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList with a head node.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts new Node into the list in correct sorted posi(increasing order)

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur.next_node is not None and cur.next_node.data < value:
                cur = cur.next_node
            new_node.next_node = cur.next_node
            cur.next_node = new_node

    def __str__(self):
        """
        Provides a string representation of the linked list.
        """
        result = []
        cur = self.head
        while cur is not None:
            result.append(str(cur.data))
            cur = cur.next_node
        return ('\n'.join(result))
