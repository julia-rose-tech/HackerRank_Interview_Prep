#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

def reverse(current_node):
    #llist head has been inserted as current node
    prev = None

    while current_node is not None:
    
        next_node = current_node.next
        #storing next node
        current_node.next = prev
        #chanding next node to previous
        prev = current_node
        #updating previous to current node
        current_node = next_node
        #moving current node to the next node in the list
    
    return prev



if __name__ == '__main__':

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist = reverse(llist.head)

        print_singly_linked_list(llist, ' ')
        print('\n')



