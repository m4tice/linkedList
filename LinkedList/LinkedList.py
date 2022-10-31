from platform import node
"""LinkedList module."""

from Node import Node

class LinkedList:
    def __init__(self):
        self.node = Node()
        self.head = self.node
        self.tail = self.node
        self.length = 1
