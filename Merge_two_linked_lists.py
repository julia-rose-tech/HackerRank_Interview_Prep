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
        print(str(node.data), end=sep)  # Use 'end' to control the separator

        node = node.next

    print() 

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def mergeLists(head1, head2):

    #check is either list is none, then return non-none list
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    #start with the list with the lowest first value
    if head1.data < head2.data:
        current_node = head1
        other_head = head2
        first_node = head1
    else:
        current_node = head2
        other_head = head1
        first_node = head2

    #while next node in list is not none
    while current_node.next is not None:
        #Check if the next node is smaller (or equal) to the other head, if so continue
        if current_node.next.data <= other_head.data:
            current_node = current_node.next
        else:
            #if not, change the pointer so the pointer points to the other head
            dummy_pointer = current_node.next
            current_node.next = other_head
            current_node = other_head
            other_head = dummy_pointer
    #when the next node is none, point to the remainder of the other list
    current_node.next = other_head
    
    #return the first node of the modified list
    return first_node

if __name__ == '__main__':
    tests = int(input().strip())

    for tests_itr in range(tests):
        llist1_count = int(input().strip())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input().strip())
            llist1.insert_node(llist1_item)

        llist2_count = int(input().strip())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input().strip())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        print()