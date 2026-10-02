# Linked List:

# Data Structure: Non-contiguous
# Memory Allocation: Typically allocated one by one to individual elements
# Insertion/Deletion: Efficient
# Access: Sequential 
        

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

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3

# current = node1

# while current is not None:
#     print(current.data)    #10 20 30
#     current = current.next   
    
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

#=>> #Singly_Linked_List : singly linked list is a linear data structure where each element is a separate object. 
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

# class Node : 
#     def __init__(self , new_data):
#         self.data = new_data
#         self.next = None
        
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)

# Temp = head

# while Temp is not None:
#     print(Temp.data , end =" ") 
#     Temp = Temp.next       
#output = 10 20 30 40

#Doubly Linked List → can move forward and backward . 
#=>A doubly linked list node has three parts: [ previous | data | next ] => example : None ← [10] ⇄ [20] ⇄ [30] → None     
#=> Real-time example: Browser history  : Google → YouTube → GitHub → ChatGPT 
# None
#   ↓
# [Google] ⇄ [YouTube] ⇄ [GitHub] ⇄ [ChatGPT]
#                                       ↓
#                                     None  
# If you're currently on ChatGPT and press Back: ChatGPT -> GitHub
#If you press Forward, it moves: GitHub → ChatGPT
##That's exactly the advantage of a doubly linked structure: two-way navigation.


# class Node :
#     def __init__(self , data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node_1 = Node(100)
# node_2 = Node(200)
# node_3 = Node(300)
# node_4 = Node(400)
# node_5 = Node(500)

# node_1.next = node_2
# node_2.prev = node_1   

# node_2.next = node_3
# node_3.prev = node_2

# node_3.next = node_4
# node_4.prev = node_3

# node_4.next = node_5
# node_5.prev = node_4
# #Structure : None ← 100 ⇄ 200 ⇄ 300 ⇄ 400 ⇄ 500 → None
# Current = node_1   
# while Current :
#     print(Current.data , end=" ")   #100 200 300 400 500 
#     Current = Current.next 
    
#Moving backward :
# Current = node_5   
# while Current :
#     print(Current.data , end=" ")   #500 400 300 200 100
#     Current = Current.prev

##Circular Linked List : 
# In a normal singly linked list: 10 → 20 → 30 → None , The last node points to None.

# In a circular linked list, the last node points back to the first node:
# 10 → 20 → 30
# ↑         ↓
# └─────────┘
# So there is no None at the end.   

# Real-time example: Multiplayer game turns 
# Imagine four players:
# Player 1 → Player 2 → Player 3 → Player 4
#     ↑                              ↓
#     └──────────────────────────────┘

# Turns happen:
# Player 1
#    ↓
# Player 2
#    ↓
# Player 3
#    ↓
# Player 4
#    ↓
# Player 1
#    ↓
# Player 2
#    ↓
# ...

# After Player 4, you don't stop.
# You go back to Player 1.
# That's a perfect example of a circular linked list. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node("Player 1")
node2 = Node("Player 2")
node3 = Node("Player 3")
node4 = Node("Player 4")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1 #it circular 

current = node1
while True:
    print(current.data)
    current = current.next
    # if current == node1:
    #     break
# Player 1
# Player 2
# Player 3
# Player 4   
    