#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""
Install Python:

Before you start coding, 
you need to have Python installed on your computer. 
You can download it from the official website python.org.
Run Python:

After installation, open a terminal or command prompt 
and type python. This opens the Python interactive shell, 
where you can run Python code line by line. 
To exit the Python shell, type exit() 
or press Ctrl+Z on Windows 
or Ctrl+D on macOS and Linux.
Write Your First Python Program:

You can use a text editor or 
integrated development environment (IDE) to write Python code. 
Create a new file with a .py extension (e.g., hello.py).

"""
# hello.py

print("Hello, World!")


# In[6]:


#Variables and Data Types:
"""
Python supports various data types like integers, 
floats, strings, and more. 
You can declare variables like this:
"""
name = "Bilal" # This is string value
age = 24       # This is integer value
height = 5.8   # This is float value

# Print Output:
"""
You've already seen the print() function. 
It's used to display the value of variables and text.
"""
print("My name is", name)
print("I am", age, "years old")



# In[7]:


# User Input:
"""
   You can get input from the user 
using the input() function:
"""
user_input = input("Enter your name: ") 
print("My Name is:", user_input)


# In[8]:


# Conditional Statements:
"""
 Use if, elif, and else 
to create conditional logic
"""
age = int(input("Enter your age"))   # I used typecast here.
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")


# In[9]:


"""
    In Python, the range() function is used 
 to generate a sequence of numbers within a specified range. 
 It is often used in for loops to iterate over a sequence of numbers. 
 The range() function is a built-in function, and it has a few different forms:
"""
# range(stop): Generates a sequence of numbers from 0 to stop - 1.
# range(start, stop): Generates a sequence of numbers from start to stop - 1.
# range(start, stop, step): Generates a sequence of numbers from start to stop - 1 with a step size of step.


# In[10]:


# Loops:

"""
You can use 'for' and 'while loops' to repeat code
"""
for i in range(5):
    print(" for loop Iteration", i)

counter = 0
while counter < 3:
    print("While loop iteration", counter)
    counter += 1


# In[11]:


# Functions:
"""
Functions are reusable blocks of code. 
You can define your own functions
"""
def greet():
    print("Hello,")

greet()


# In[ ]:




