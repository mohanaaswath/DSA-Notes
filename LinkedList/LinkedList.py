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
# class Node:
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize next as null
        

#Think of it like a chain: [10 | next] → [20 | next] → [30 | next] → None 

#Creating One Node :
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# node1 = Node(10)
# print(node1.data)
# print(node1.next)
# ┌──────┬──────┐
# │  10  │ None │
# └──────┴──────┘      

#Creating Two Nodes : 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# node1 = Node(10)
# node2 = Node(20)

# node1.next = node2

# print(node1.data)   #Gives 10
# print(node1.next.data)   #Gives 20
# 10 20 
# node1                 node2
# ┌────┬──────┐         ┌────┬──────┐
# │ 10 │ None │         │ 20 │ None │
# └────┴──────┘         └────┴──────┘

#node1.next = node2 
# node1
#   ↓
# ┌────┬──────┐
# │ 10 │  ──────────┐
# └────┴──────┘     │
#                    ↓
#                 ┌────┬──────┐
#                 │ 20 │ None │
#                 └────┴──────┘

# node1
#  ↓
# data = 10
# next → node2
#           ↓
#         data = 20 

#Creating a 3-Node Linked List : 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3

# print(node1.data)
# print(node1.next.data)
# print(node1.next.next.data)
# 10 20 30

# Step 1 — Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# We now have:
# node1        node2        node3
# [10 | None]  [20 | None]  [30 | None]


# Step 2 — Connect node1 to node2
# node1.next = node2
# Now:
# [10 |  ●] → [20 | None]

# Step 3 — Connect node2 to node3
# node2.next = node3
# Now:
# [10 | ●] → [20 | ●] → [30 | None]

# That's our linked list:  10 → 20 → 30 → None

# Accessing the values
# First node: node1.data → 10
# Second node: node1.next.data → 20
# Third node: node1.next.next.data → 30

# Why?
# node1
#  ↓
# 10
#  ↓ next
# 20
#  ↓ next
# 30
#  ↓
# None

#Traversing the Linked List : 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

current = node1

while current is not None:
    print(current.data)    #10 20 30
    current = current.next   
    
# Let's understand the loop

# Initially:
# current = node1
# So:
# current
#    ↓
# [10] → [20] → [30] → None

# First iteration
# print(current.data)
# prints:
# 10
# Then:
# current = current.next
# Now current moves to node 2:
#        current
#           ↓
# [10] → [20] → [30] → None

# Second iteration
# Print:
# 20
# Then:
# current = current.next
# Now:
#                current
#                   ↓
# [10] → [20] → [30] → None

# Third iteration
# Print:
# 30
# Then:
# current = current.next
# Now:
# [10] → [20] → [30] → None
#                          ↑
#                        current

# Actually current is now None.
# Therefore:while current is not None => becomes false and the loop stops.   

#tomorrow see