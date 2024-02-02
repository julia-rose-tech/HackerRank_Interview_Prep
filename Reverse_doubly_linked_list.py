#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            # if self.head is None: ** same idea
            # checks whether the 'head' attribute is 'None' or no. None = false, so if not/false...
            # the list is empty so the head & tail become the node
            self.head = node
        else:
            #list is not empty, so the pointer to the next becomes the node and the 
            self.tail.next = node
            # the tail now points to the current node, effectivly adding the new node to the end of the list
            # the current node is initalised with the next being None, this remains as it is at the end of the list
            node.prev = self.tail
            # sets this node's previous to be the tail, which is currently the previous node


        self.tail = node
        # updates the tail to now be the new node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)



def reverse(current_node):
    prev = None

    while current_node is not None:
        next_node = current_node.next
        # storing next node
        current_node.next = prev
        # changing the next point to point at previous
        current_node.prev = next_node
        # changing the previous pointer to point at next 
        prev = current_node
        # updating the prev to be the current node
        # intially prev is zero, but that changes after the first node
        # this stores te previous node
        current_node = next_node
        # moving onto the next node in list
    return prev

    

if __name__ == '__main__':
   
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_doubly_linked_list(llist1, ' ')
        print('\n')

