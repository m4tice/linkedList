"""MyLinkedList module."""

from platform import node
from Node import Node

class MyLinkedList:
    def __init__(self):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            node : Node
                first node of linkeList
            head : Node
                first node in linkedList
            tail : Node
                last node in linkedList
            tail : int
                length of linkedList
        """
        self.node = Node()
        self.head = self.node
        self.tail = self.node
        self.length = 1
