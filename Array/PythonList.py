Basic_List = [10,3.14,"Python",True,None,2+3j,[1,2,3],(4,5,6),{"name":"John","age":30}]
print(Basic_List)

    #Python List
        #A List is a collection that allows you to store multiple values in a single variable.
        

fruits = ["Apple", "Banana", "Orange"]

print(fruits) # ["Apple" ,"Banana" ,"Orange"]
       #Here, fruits contains three items.

       #Lists are :✅ Ordered , ✅ Mutable (you can change them), ✅ Allow duplicate values

    #Accessing Elements :
        #Lists use indexing, starting from 0.

print(fruits[0]) # Apple

    #To get the last item:

print(fruits[-1]) #Orange

    #Adding Elements : Use the append() method.

fruits.append("Mango")

print(fruits) # ["Apple", "Banana", "Orange", "Mango"]

    #Removing Elements : Use remove().

fruits.remove("Banana")

print(fruits) #["Apple", "Orange", "Mango"]

     #Updating Elements : Lists are mutable, so you can modify values.

fruits[1] = "Grapes"
print(fruits) #["Apple", "Grapes" ,"Mango"]

      #List Length :To find the number of items:

print(len(fruits)) #3

      #Where Are Lists Used?

        #Lists are used everywhere in real-world applications:

               #Shopping carts in e-commerce
               #Student records
               #Employee data
               #Product catalogs
               #To-do lists
               #AI and Data Science datasets    

#what is index : index is a position of a each value in a list. 

#positive index start from 0 
#negative index start from -1 (last value) 



#Range of Index : You can access a range of values in a list using slicing. 
#range() have start , end and step values. 


list = [456 , "python", "java" , 3.45 , "javascript" , True]
list1 = list[1:4] # it will print from index 1 to index 3 (4-1)
print(list1) # ['python', 'java', 3.45]

#print(list[2:5]) # it will print from index 2 to index 4 (5-1) #['java', 3.45, 'javascript']

print(list[2:]) # it will print from index 2 to last index #['java', 3.45, 'javascript', True]
print(list[:4]) # it will print from index 0 to index 3 (4-1) # [456, 'python', 'java', 3.45]
print(list[1:4:2]) # it will print from index 1 to index 3 (4-1) with step 2 #['python', 3.45]
print(list[::2]) # it will print all values with step 2 # [456, 'java', 'javascript']
print(list[::-1]) # it will print all values in reverse order # [True, 'javascript', 3.45, 'java', 'python', 456]
print(list[1:5:-1]) # it will print empty list because step is negative and start index is less than end index # []

print(list[6:1])# it will print empty list because start index is greater than end index # []
print(list[-6:-1]) # it will print from index -6 to index -2 (-1 is not included) # [456, 'python', 'java', 3.45, 'javascript']

print(list[-1:-6]) # it will print empty list because start index is greater than end index # []

# insert = > in list we can insert a value at any index using insert() method. It takes two arguments, index and value.
a = ["python" , "java" , "javascript" ,"c++"]
a.insert(1,'ml')
print(a) #['python', 'ml', 'java', 'javascript', 'c++']
print(len(a)) # it will print length of list # 5
a.insert(2 ,["DataScience","AI" ,"UniqStackAI"]) #['python', 'ml', ['DataScience', 'AI', 'UniqStackAI'], 'java', 'javascript', 'c++']
print(a)

# #append => in list we can add element in the end of the list using append() method. It takes one argument, value.
# #extend => in list we can add multiple elements in the end of the list using extend() method. It takes one argument, iterable (list, tuple, set, string).
b = ["AI" , "google" ,"chatgpt","gemini"]
print(b)
b.append(a)
print(b) #['AI', 'google', 'chatgpt', 'gemini', 'Claude']
b.extend("a") # ['AI', 'google', 'chatgpt', 'gemini', ['python', 'ml', ['DataScience', 'AI', 'UniqStackAI'], 'java', 'javascript', 'c++']]

# #update => in list we can update a value at any index using index. It takes one argument, index and value.
c = ["love","notlove","hate", "like" ,"Happy"]
c[0] = "loved"
print(c) #['loved', 'notlove', 'hate', 'like', 'Happy'] 

#pop => in list we can remove a value at any index using pop() method. It takes one argument, index. If index is not provided, it removes the last item.
c.pop(-3)
print(c) #['loved', 'notlove', 'like', 'Happy']
print(c.pop()) # it will print the last item and remove it from the list # Happy  

#write a program to generate 1 - 100 

newList = []
for i in range(1,100):
       newList.append(i)
      
       
#write a program to generate 1 - 100 and add even numbers in evenlist and odd numbers in oddlist.   
evenList = []
oddList =[]
for i in range(1,101):
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)
  

#Fibonacci Series :


#write a program to find the largest value in the list without using any inbuilt function.
lst = [5,6,2,2,31,34,53,54,23,350,250,10]
for i in lst :
       if i > lst:
           lst = i
print(lst) # 350


#write a program to find the second largest value in the list without using any inbuilt function.
lst = [5,6,2,2,31,34,53,54,23,350,250,10]
largest = lst[0]
second_largest = lst[0]
for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(second_largest) #250  

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
 
# Example 1:
# Input: nums = [2,7,11,15], target = 9  Output: [0,1]  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
list = [2,7,11,15]
Target = 9
for i in range(len(list)):
    for j in range(1,len(list)):
        if list[i] + list[j] == Target:
            print([i,j]) # [0, 1]

# Example 2:
# Input: nums = [3,2,4], target = 6   Output: [1,2]


        
# Example 3:
# Input: nums = [3,3], target = 6  Output: [0,1]



#list Comprehension : list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes","cherry" ,"kiwi"]
New_list = []
for i in fruits:
    if "a" in i:
        New_list.append(i)
print(New_list) # ['Banana', 'Mango', 'Grapes']  it will print all the values which contains "a" in it.

        #print(OR)

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes","cherry" ,"kiwi"]
New_list = [i for i in fruits if "a" in i]
print(New_list) # ['Banana', 'Mango', 'Grapes']  it will print all the values which contains "a" in it.


#list Shorting : you can sort a list in ascending or descending order using the sort() method. By default, it sorts in ascending order.

list = [5, 2, 8, 1, 9]
list.sort() # it will sort the list in ascending order
print(list) # [1, 2, 5, 8, 9]
list.sort(reverse=True) # it will sort the list in descending order
print(list) # [9, 8, 5, 2, 1] 

CharacterString = ["a", "c", "b", "e", "d"]
CharacterString.sort() # it will sort the list in ascending order
print(CharacterString) # ['a', 'b', 'c', 'd', 'e']

Capital_Small_Letters = ["ACG" , "ath" ,"BDF" ,"XZV","nkr" ,"LMN" ,"zwa" ,"qqw" ,"QER"]
Capital_Small_Letters.sort() # it will sort the list in ascending order
print(Capital_Small_Letters) # ['ACG', 'BDF', 'LMN', 'QER', 'XZV', 'ath', 'nkr', 'qqw', 'zwa']  it will sort the list in ascending order and capital letters will come first then small letters.

# #Reverse your list : you can reverse a list using the reverse() method. It will reverse the order of the list.
# # This reverse is ok => list.reverse() # it will reverse the list 
#print(list) # [1, 2, 5, 8, 9]  it will reverse the list
list.sort(reverse=True)
print(list) # [9, 8, 5, 2, 1]  it will sort the list in descending order
list.sort(reverse=False)
print(list) # [1, 2, 5, 8, 9]  it will sort the list in ascending order

Name = "mom"
Check = Name [ ::-1 ] # it will reverse the string
if Name == Check:
    print("Palindrome") # it will print Palindrome if the string is same when reversed
else:
    print("Not Palindrome") # it will print Not Palindrome if the string is not same when reversed  


     