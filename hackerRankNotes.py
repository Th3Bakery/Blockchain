#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 17:18:08 2018

@author: evanbaker
"""

raw_input= '5/n 2 3 6 6 5'

raw_input = """5
            2 3 6 6 5"""

            
n = int(raw_input())
arr = map(int, raw_input().split())
               

s = """ very long string
        test test test """
        
raw_input().split()


# I need some sample code that this actually works on. 

if __name__ == '__main__':
    inputIntegers = int(input())
    listOfInputIntegers = list(map(int,raw_input().strip().split()))[:inputIntegers]
    originalMax = max(listOfInputIntegers)
    # find the original maximum value & then remove it. 
    while max(listOfInputIntegers) == originalMax:
        listOfInputIntegers.remove(max(listOfInputIntegers))
    # after removing the maximum value - print the new max. 
    print max(listOfInputIntegers)


file = open('input.txt', 'r') 
txtInputString = file.read()

print file.read() 

file = open('input.txt','r')
file = open('input.txt','r')

txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()

file = open('input.txt,'r')
txtInputString = file.read()
file = open('input.txt','r')
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()
txtInputString = file.read()

file = open('input.txt','r')
file = open('input.txt','r')


#
#They pretty much gave me the answer here:
    
    if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    print [ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range ( z + 1) if ( ( i + j +k ) != n ) ]


#This is a really cool way to grow a list to a very large size

a = 5
b = 5
c = 5
#print [ [d,e,f] for d in range(a+1) for e in range(b+1) for f in range(c+1)]

# my Spyder version of python doesn't like starting the command with print. 
[ [d,e,f] for d in range(a+1) for e in range(b+1) for f in range(c+1)]

# The command above is super powerful and enables the quick creation of enormous lists.
# let's say I wanted a variable to go from 1:1000

a = 1000
listTo1000 = [ [d] for d in range(a+1)]

listTo1000


# Super powerful way to create a new list of any length and of any size in python

a = 1000
listTo1000 = [ [d] for d in range(a+1)]

listTo100 = [ [i] for i in range(a+1)]

listTo100 = [ [i] for i in range(101)]

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split()[:n])
    
    t = tuple(integer_list)
    print hash(t)


#using tuples>
# to convert a list to a tuple, simply use tuple(list_name)
tuple(list_name)
tuple(list_name)
tuple(list_name)

#to extract a variable from a list separated by spaces

integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])
integer_list = map(int, raw_input().split()[:n])

l = list()
l.insert(0 5)

#


# Mastering lists in Python.

if __name__ == '__main__':
    N = int(raw_input())
    i=1
    l = list()
    
    # There is probably a much more efficient way to write this code. 
    
    while i<=N:
        command_list = map(str, raw_input().split()[:N])
        
        if command_list[0] == 'insert':
            l.insert(int(command_list[1]),int(command_list[2]))
        if command_list[0] == 'remove':
            l.remove(int(command_list[1]))
        if command_list[0] == 'append':
            l.append(int(command_list[1]))
        if command_list[0] == 'sort':
            l.sort()
        if command_list[0] == 'pop':
            l.pop()
        if command_list[0] == 'reverse':
            l.reverse()
        if command_list[0] == 'print':
            print l
        #print command_list   #Was used for debugging
        i=i+1


# it is super important to understand how to manipulate lists.
# once you create something as a list - it has a bunch of properties
# that you can easily manipulate.  one of the quick key things to 
# try after creating a general list - is to try the . to see if any
# common commands are useful for solving whatever specific problem
# that you are currently trying to solve.  That will enable you to 
# solve the problem you are trying to solve much quicker.
#
# Understanding python to the best of my ability - and enabling myself
# to contribute to python code for new blockchain interfaces - or enabling
# myself to quickly edit other blockchains will enable me to be much
# more powerful and efficient at solving very complex problems.
# still taking baby steps today though.  Just learning the basics
# and getting comfortable using python on a daily basis.
# once I am comfortable coding in a variety of ways, I will be able
# to create more complex structures, functions and creations.
#
# It is interesting how easy it was to pass the original python tests
# in my 'learn pyhton' app and how much more challenging it is on this
# hacker rank webpage. 



#Manipulating strings in python.  In this test, i switched capitalization
# of strings in such a way that every lower case letter became capitalized
# and every capital letter became lower case.  I also carried through
# all letters that were neither capitalized nor lower case.

def swap_case(s):
    
    stringLength = len(s)
    #print stringLength  checking the string length output. 
    
    newString = ''
    lowerString = ''
    
    for index in range(0,len(s)):
            if s[index].isupper():
                #print s[index].isupper()
                lowerString = s[index].lower()
                newString += lowerString
                #print newString
            elif s[index].islower():
                upperString = s[index].upper()
                newString += upperString
                #newString.append(s[index].upper)
                #print newString
            else:
                newString += s[index]
                #print newString
    return newString


# Splitting and joining strings.

def split_and_join(line):
    # write your code here
    newOutput = line.split(' ')
    #print newOutput
    joinedString = '-'.join(newOutput)
    #print joinedString
    #a = "-".join(a)
    return joinedString

# this describes how to split and join strings in python.

SentenceString = 'hi my name is evan'
splitString = SentenceString.split(' ')
splitString
joinedString = ','.join(splitString)
joinedString


# printing a screen display output. The purpose was to just display someones
# name to the screen.  Not too terribly challenging.  This would have been 
# a single line of code in matlab.  Kind of strange that I had to split it 
# up so much here in python.  Working on developing cleaner code would be 
# an important start.

def print_full_name(a, b):
    newString = 'Hello '
    newString += a
    newString += ' '
    newString += b
    newString += '! You just delved into python.'
    print newString
    return newString

#

# building a python function that can replace a single variable in a string
# with another variable in that same string.

def mutate_string(string, position, character):
    
    string = string[:position] + character + string[position+1:]
    #print string
    
    return string

# practicing

string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]
string = string[:position] + character + string[position+1:]

# passing another algorithm
# quickly being able to count things. 

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)+1-len(sub_string)):
        if (string[i:i+len(sub_string)]) == sub_string:
            #print (string[i:i+len(sub_string)])
            count = count+1
            #print count
    return count



# Quickly checking the code if it contains various types of letter types.
# this type of analysis could be helpful to quickly search different types of scripts
# this sounds especially helpful for checking if the password of a given 
# system meets requirements.
# It looks like this password would require alphanumeric, alphabetical, digits lower and upper case letters



if __name__ == '__main__':
    s = raw_input()
    
    # Initialize all variables to be false
    containsAlphaNumericChar = False
    containsAlphabeticalChar = False
    containsDigits = False
    containsLower = False
    containsUpper = False
    
    for index in range(0,len(s)):
    
        if s[index].isalnum():
            containsAlphaNumericChar = True
    
        if s[index].isalpha():
            containsAlphabeticalChar = True
 
        if s[index].isdigit():
            containsDigits = True
        
        if s[index].islower():
            containsLower = True
        
        if s[index].isupper():
            containsUpper = True
        
    print containsAlphaNumericChar
    print containsAlphabeticalChar
    print containsDigits
    print containsLower
    print containsUpper


# Creating the Hacker Rank Logo. Kind of a fund random task. 

#Replace all ______ with rjust, ljust or center. 

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone    This is done and correct
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars    This is done and correct
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt    This is done and correct
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)    

#Bottom Pillars     likely done and correct
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)    

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)    



# Killing another string manipulation script.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


def wrap(string, max_width):
    newString = ''
    index = 0
    while index < len(string):
        newString += string[index:index+max_width]
        index = index+max_width
        newString += '\n'
    return newString


numpy arrays.

def arrays(arr):
    import numpy as np
    #print arr
    arr = map(float,arr)
    newArray = np.array(arr)
    #print arr
    #newArray = np.array(arr,float)
    #newArray = arr.strip().split(' ')
    #print newArray
    newArray = newArray[::-1]
    #print newArray
    
    #reversed_arr.rstrip('0')
    #print reversed_arr
    
    return newArray

manipulating array code.  you use np.array(yourList)
np.array(yourList)
np.array(yourList)
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
import numpy as np
