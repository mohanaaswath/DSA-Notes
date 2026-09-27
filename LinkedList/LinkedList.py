# Linked List:

# Data Structure: Non-contiguous
# Memory Allocation: Typically allocated one by one to individual elements
# Insertion/Deletion: Efficient
# Access: Sequential 

#Singly_Linked_List : singly linked list is a linear data structure where each element is a separate object. 
# Each element (node) of a list is comprising of two items - the data and a reference to the next node. 
# The last node has a reference to null. The entry point into a linked list is called the head of the list. 
# It should be noted that head is not a separate node, but the reference to the first node.
# If the list is empty then the head is a null reference.

#Sample diagram : Head -> [Data|Next] -> [Data|Next] -> [Data|Next] -> null

#Singly Linked List example implementation in Python:
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        
#Singly Linked List size 4 :
        