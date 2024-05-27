#Docstrings in Python
#fun.__doc__ : return features of function.

#you can write features of your function as follow

def square(n):
    '''Take a number n and return its square'''     
    return n**2

print(square(5))
print(square.__doc__)

#note: docstring should be the first line of function else its not a docstring

def square(n):
    a=5
    '''Take a number n and return its square'''     
    return n**2

print(square(5))
print(square.__doc__)

#PEP8 : Python Enhancement Proposal
#It provides guidlines and best practices on how to write Python code.


#The Zen of Python : use (import this) in terminal and it will show you the following poem
"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

print(dir(__builtins__)) #return names of all of Python’s built-in objects
