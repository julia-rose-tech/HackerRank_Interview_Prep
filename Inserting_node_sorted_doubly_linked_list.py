#!/bin/python3

import math
import os
import random
import re
import sys

# Sample Input:
# 1
# 4
# 1
# 3
# 4
# 10
# 5
# Sample Output:
# 1 3 4 5 10

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
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    node = DoublyLinkedListNode(data)
    current_node = llist

    if llist.data > data:
        node.next = llist
        llist.prev = node
        return node

    while current_node.next is not None:
        if current_node.next.data > data:
            node.next = current_node.next
            node.prev = current_node
            current_node.next.prev = node
            current_node.next = node
            return llist
        else:
            current_node = current_node.next
            
    current_node.next = node
    node.prev = current_node
      
    return llist

if __name__ == '__main__':
 
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ')
        print('\n')

