"""MyLinkedList module."""


from re import S
from linked_list.node import Node

class LinkedList:
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

    def prepend(self):
        """
        Add one node at the front of the list
        @return: nothing
        """

        tempNode= Node()
        self.head.next = tempNode
        self.head = tempNode
        self.length += 1
