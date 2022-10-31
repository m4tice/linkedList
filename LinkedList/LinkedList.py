from platform import node
"""MyLinkedList module."""

from Node import Node

class MyLinkedList:
    def __init__(self):
        self.node = Node()
        self.head = self.node
        self.tail = self.node
        self.length = 1
