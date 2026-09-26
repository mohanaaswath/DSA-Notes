#Stack is a linear data structure that follows the Last In First Out (LIFO) principle.
#It means that the last element added to the stack will be the first one to be removed.
#The basic operations of a stack are push (to add an element), pop (to remove the top element), and peek (to view the top element without removing it). 
#Stacks can be implemented using arrays or linked lists.

st = []
st.append("a")
st.append("b")
st.append("c")

print(st)
print(st.pop())
print(st.pop())
print(st)

#deque is a linear data structure that follows the first in first out (FIFO) principle.
#It means that the first element added to the deque will be the first one to be removed.
from collections import deque 
stack = deque()
stack.append("a")
stack.append("AI Powered Full Stack Developer")
print(stack)          


#Stack Problems:

A = [1,2,3,4,5]
A.append(6)
print(A) # [1, 2, 3, 4, 5, 6]

def reverse_string(s):
    stack = []
    for char in s: #s means parameter of function reverse_string
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

result = reverse_string("Enterpenure World!")
print(result)  # Output: !dlroW eruneptnE


