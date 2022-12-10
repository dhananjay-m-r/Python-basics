# -*- coding: utf-8 -*-
"""ln 8 Intext Examples_Strings.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QzrZOe5o5_MxnOIHKkR1tOUgOVW0HdM_

#About this notebook

Notebook made by: Dhananjay M.R

Subject: Computer Science - Grade 11 CBSE

Language: - Python

Topic: Intext Examples with Explanation - Strings

Execution mode: Script Mode

#Strings
String is a sequence which is made up of one or more UNICODE characters. Here the character can be a letter, digit, whitespace or any other symbol. A string can be created by enclosing one or more characters in single, double or triple quote.

#Example 8.1
"""

str1 = 'Hello World!'
str2 = "Hello World!"
str3 = """Hello World!"""
str4 = '''Hello World!'''

"""`str1, str2, str3, str4` are all string variables having the same value `'Hello World!'`. Values stored in `str3` and `str4` can be extended to multiple lines using triple codes as can be seen in the following example:"""

str3 = """Hello World!
welcome to the world of Python"""

str4 = '''Hello World!
welcome to the world of Python'''

"""#Accessing Characters in a String 
Each individual character in a string can be accessed using a technique called indexing. The index specifies the character to be accessed in the string and is written in square brackets (`[ ]`). The index of the first character (from left) in the string is 0 and the last character is n-1 where n is the length of the string. If we give index value out of this range then we get an IndexError. The index must be an integer (positive, zero or negative).
"""

#initializes a string str1
str1 = 'Hello World!'

#gives the first character of str1
print('first character of str1:')   #Optional Statement
print(str1[0])
print('')   #Optional statement, to leave a line gap

#gives seventh character of str1
print('seventh character of str1:')  #Optional Statement
print(str1[6])
print('')   #Optional statement, to leave a line gap

#gives last character of str1
print('last character of str1:')    #Optional Statement
print(str1[11])

#gives error as index is out of range
#str1[15]

"""The index can also be an expression including variables and operators but the expression must evaluate to an integer."""

str1 = 'Hello World!'
str1[2+4]

"""Python allows an index value to be negative also. Negative indices are used when we want to access the characters of the string from right to left. Starting from right hand side, the first character has the index as -1 and the last character has the index –n where n is the length of the string."""

#initializes a string str1
str1 = 'Hello World!'

print(str1[-1])   #gives first character from right
print(str1[-12])  #gives last character from right

"""An inbuilt function `len()` in Python returns the length of the string that is passed as parameter."""

#initializes a string str1
str1 = 'Hello World!'

#gives the length of the string str1
print('length of the string str1:')  #Optional Statement
print(len(str1))
print('')   #Optional statement, to leave a line gap

#length of the string is assigned to n
print('length of the string is assigned to n:')    #Optional Statement
n = len(str1)
print(n)
print('')   #Optional statement, to leave a line gap

#gives the last character of the string
print('last character of the string:')    #Optional Statement
print(str1[n-1])
print('')   #Optional statement, to leave a line gap

#gives the first character of the string
print('first character of the string:')   #Optional Statement
print(str1[-n])

"""# String is Immutable
A string is an immutable data type. It means that the contents of the string cannot be changed after it has been created. An attempt to do this would lead to an error.
```
>>> str1 = "Hello World!"
#if we try to replace character 'e' with 'a'
>>> str1[1] = 'a'
TypeError: 'str' object does not support item assignment
```

# String Operations

As we know that string is a sequence of characters. Python allows certain operations on string data type, such as:
*   Concatenation
*   Repetition
*   Membership
*   Slicing

# Concatenation
To concatenate means to join. Python allows us to join two strings using concatenation operator plus which is denoted by symbol +
"""

str1 = 'Hello '   #First String
str2 = 'World'    #Second String

print('The concated string is:')    #Optional statement
print(str1 + str2)   #Concated strings
print('')   #Optional statement, to leave a line gap

#After the operation str1 and str2 remain the same
print('After the operation str1 and str2 remains the same')
print('')   #Optional statement, to leave a line gap

print('str1 is:')   #Optional statement
print(str1)

print('')   #Optional statement, to leave a line gap

print('str2 is:')   #Optional statement
print(str2)

"""# Repetition
Python allows us to repeat the given string using repetition operator which is denoted by symbol *
"""

#assign string 'Hello' to str1
str1 = 'Hello ' 

#repeat the value of str1 2 times 
str1 * 2

#assign string 'Hello' to str1
str1 = 'Hello ' 

#repeat the value of str1 5 times 
str1 * 5

"""# Membership
Python has two membership operators `in` and `not in`. The `in` operator takes two strings and returns `True` if the first string appears as a substring in the second string, otherwise it returns `False`.
"""

str1 = 'Hello World!'
'W' in str1

str1 = 'Hello World!'
'Wor' in str1

str1 = 'Hello World!'
'My' in str1

"""The `not in` operator also takes two strings and returns True if the first string does not appear as a substring in the second string, otherwise returns `False`"""

str1 = 'Hello World!'
'My' not in str1

str1 = 'Hello World!'
'Hello' not in str1

"""# Slicing
In Python, to access some part of a string or substring, we use a method called slicing. This can be done by specifying an index range. 

Given a string `str1`, the slice operation `str1[n:m]` returns the part of the string `str1` starting from index n (inclusive) and ending at m (exclusive). 

 In other words, we can say that `str1[n:m]` returns all the characters starting from `str1[n]` till `str1[m-1]`. The numbers of characters in the substring will always be equal to difference of two indices m and n, i.e., (m-n).
"""

str1 = 'Hello World!'

#gives substring starting from index 1 to 4
str1[1:5]

str1 = 'Hello World!'

#gives substring starting from 7 to 9
str1[7:10]

"""If the first index is not mentioned, the slice starts from index. """

str1 = 'Hello World!'

#gives substring from index 0 to 4
str1[:5]

"""If the second index is not mentioned, the slicing is done till the length of the string."""

str1 = 'Hello World!'

#gives substring from index 6 to end
str1[6:]

"""The slice operation can also take a third index that specifies the ‘step size’. For example, `str1[n:m:k]`, means every kth character has to be extracted from the string `str1` starting from n and ending at m-1. By default, the step size is one."""

str1 = 'Hello World!'
str1[0:10:2]

str1 = 'Hello World!'
str1[0:10:3]

"""# Transversing a string
We can access each character of a string or traverse a string using for loop and `while` loop.

# (A) String Traversal Using `for` Loop:
"""

str1 = 'Hello World!'

for ch in str1:
  print(ch,end = '')

"""In the above code, the loop starts from the first character of the string `str1` and automatically ends when the last character is accessed.

# (B) String Traversal Using `while` Loop:
"""

str1 = 'Hello World!'

index = 0
#len(): a function to get length of string
while  index < len(str1):
  print(str1[index],end = '')
  index += 1

"""Here `while` loop runs till the condition `index < len(str)` is `True`, where index varies from 0 to `len(str1)` -1.

# -> Strings methods and built-in functions

# `len()`
Returns the length of the given string
"""

str1 = 'Hello World!'
len(str1)

"""# `title()`
Returns the string with first letter of every word in the string in uppercase and rest in lowercase
"""

str1 = 'hello WORLD!'
str1.title()

"""# `lower()`
Returns the string with all uppercase letters converted to lowercase
"""

str1 = 'hello WORLD!'
str1.lower()

"""# `upper()`
Returns the string with all lowercase letters converted to uppercase
"""

str1 = 'hello WORLD!'
str1.upper()

"""# `count(str, start, end)`
Returns number of times substring `str` occurs in the given string. If we do not give start index and end index  then searching starts from index 0 and ends at length of the string
"""

str1 = 'Hello World! Hello Hello'
print(str1.count('Hello',12,25))
print(str1.count('Hello'))

"""# `find(str,start, end)`
Returns the first occurrence of index of substring `str` occurring in the given string. If we do not give start and end then searching starts from index 0 and ends at length of the string. If the substring is not present in the given string, then the function returns -1
"""

str1  = 'Hello World! Hello Hello'
print(str1.find('Hello',10,20))
print(str1.find('Hello',15,25))
print(str1.find('Hello'))
print(str1.find('Hee'))

"""# `endswith()`
Returns True if the given string ends with the supplied substring otherwise returns False
"""

str1 = 'Hello World!'

print(str1.endswith('World!'))
print(str1.endswith('!'))
print(str1.endswith('lde'))

"""# `startswith()`
Returns True if the given string starts with the supplied substring otherwise returns False
"""

str1 = 'Hello World!'
print(str1.startswith('He'))
print(str1.startswith('Hee'))

"""# `isalnum()`
Returns True if characters of the given string are either alphabets or numeric. If whitespace or special symbols are part of the given string or the string is empty it returns False
"""

str1 = 'HelloWorld'
str1.isalnum()

str1 = 'HelloWorld2'
str1.isalnum()

str1 = 'HelloWorld!!'
str1.isalnum()

"""# `islower()`
Returns True if the string is non-empty and has all lowercase alphabets, or has at least one character as lowercase alphabet and rest are non-alphabet characters
"""

str1 = 'hello world!'
str1.islower()

str1 = 'hello 1234'
str1.islower()

str1 = 'hello ??'
str1.islower()

str1 = '1234'
str1.islower()

str1 = 'Hello World!'
str1.islower()

"""# `isupper()`
Returns True if the string is non-empty and has all uppercase alphabets, or has at least one character as uppercase character and rest are non-alphabet characters
"""

str1 = 'HELLO WORLD!'
str1.isupper()

str1 = 'HELLO 1234'
str1.isupper()

str1 = 'HELLO ??'
str1.isupper()

str1 = '1234'
str1.isupper()

str1 = 'Hello World!'
str1.isupper()

"""# `isspace()`
Returns True if the string is non-empty and all characters are white spaces (blank, tab, newline, carriage return)
"""

str1 = '     \n   \t \r'
str1.isspace()

str1 = 'Hello        \n'
str1.isspace()

"""# `istitle()`
Returns True if the string is non-empty and title case, i.e., the first letter of every word in the string in uppercase and rest in lowercase
"""

str1 = 'Hello World!'
str1.istitle()

str1 = 'hello World!'
str1.istitle()

"""# `lstrip()`
Returns the string after removing the spaces only on the left of the string
"""

str1 = '        Hello World!    '
str1.lstrip()

"""# `rstrip()`
Returns the string after removing the spaces only on the right of the string
"""

str1 = '       Hello World!'
str1.rstrip()

"""# `strip()`
Returns the string after removing the spaces both on the left and the right of the string
"""

str1 = '        Hello World!    '
str1.strip()

"""# `replace(oldstr, newstr)`
Replaces all occurrences of old string with the new string
"""

str1 = 'Hello World!'
str1.replace('o','*')

str1 = 'Hello World!'
str1.replace('World','Country')

str1 = 'Hello World! Hello'
str1.replace('Hello','Bye')

"""# `partition()`
Partitions the given string at the first occurrence of the substring (separator) and returns the string partitioned into three parts. 
1. Substring before the separator 
2. Separator 
3. Substring after the separator If the separator is not found in the string, it returns the whole string itself and two empty strings
"""

str1 = 'India is a Great Country'
str1.partition('is')

str1 = 'India is a Great Country'
str1.partition('are')

"""# `split()`
Returns a list of words delimited by the specified substring. If no delimiter is given then words are separated by space.
"""

str1 = 'India is a Great Country'
str1.split()

str1 = 'India is a Great Country'
str1.split('a')

"""# Handling Strings

# Program 8-1: Write a program with a user defined function to count the number of times a character (passed as argument) occurs in the given string.
"""

#Function to count the number of times a character occurs in a

#string
def charCount(ch,st):
  count = 0
  for character in st:
    if character == ch:
      count += 1
  return count 
#end of function

st = input("Enter a string: ")
ch = input("Enter the character to be searched: ")
count = charCount(ch,st)
print("Number of times character",ch,"occurs in the string is:",count)

"""# Program 8-2 Write a program with a user defined function with string as a parameter which replaces all vowels in the string with '*'."""

#Program 8-2 
#Function to replace all vowels in the string with  '*' 

def replaceVowel(st):    

#create an empty string

  newstr = ''
  for character in st:     
    #check if next character is a vowel
    if character in 'aeiouAEIOU':     
      #Replace vowel with *
      newstr += '*'
    else:
      newstr += character     
  return newstr 
#end of function 

st = input("Enter a String: ") 
st1 = replaceVowel(st)
print("The original String is:",st)
print("The modified String is:",st1)

"""# Program 8-3 Write a program to input a string from the user and print it in the reverse order without creating a new string."""

#Program 8-3 
#Program to display string in reverse order

st = input("Enter a string: ")
for i in range(-1,-len(st)-1,-1):
  print(st[i],end='')

"""# Program 8-4 Write a program which reverses a string passed as parameter and stores the reversed string in a new string. Use a user defined function for reversing the string."""

#Program 8-4
#Function to reverse a string

def reverseString(st):
  newstr = ''        #create a new string
  length = len(st)
  for i in range(-1,-length-1,-1):
    newstr += st[i]
  return newstr
#end of function

st = input("Enter a String: ")
st1 = reverseString(st)
print("The original String is:",st)
print("The reversed String is:",st1)

"""# Summary
1. A string is a sequence of characters enclosed in single, double or triple quotes. 
2. Indexing is used for accessing individual characters within a string. 
3. The first character has the index 0 and the last character has the index n-1 where n is the length of the string. The negative indexing ranges from -n to -1. 
4. Strings in Python are immutable, i.e., a string cannot be changed after it is created. 
5. Membership operator in takes two strings and returns True if the first string appears as a substring in the second else returns False. Membership operator ‘not in’ does the reverse. 
6. Retrieving a portion of a string is called slicing. This can be done by specifying an index range. The slice operation str1[n:m] returns the part of the string str1 starting from index n (inclusive) and ending at m (exclusive). 
7. Each character of a string can be accessed either using a for loop or while loop. 
8. There are many built-in functions for working with strings in Python.

For further more programs on strings, kindly refer the file whose link is shared below: 

https://colab.research.google.com/drive/1irVdWdq_3ZA8bMlRS4IYTPZSpOxre9G4?usp=sharing
"""