#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:52:08 2018

@author: evanbaker
"""

input = 3

if input%2 == 1:  #This means the answer is odd
    print('Weird')

if input%2 == 0 and 2<= input <= 5:
    print('Not Weird')
    
if input%2 ==0 and 6<= input <= 20:
    print('Weird')

if input%2 == 0 and input > 20:
    print('Not Weird')
    
    
import numpy as np

raw_input = 5
if __name__ == '__main__':
    n = int(raw_input())
    n = 5
    index = 0
    while index <= np.sqrt(n)//1:
        print(index*index)
        index = index+1
        

year = 2100
leap = False
if year%100 ==0 and year%400 ==0:
    leap = True
    
leap

year = 2404
leap = False
if year%4 ==0:
    leap = True
if year%100 ==0:
    leap = False
if year%400 == 0:
    leap = True
leap


# Next Tutorial:

n = 5
valuesToPrint = list(range(1,n))
    
print(*valuesToPrint, sep=' ', end='\n', file=sys.stdout)


#Completed Challenge!:
    from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    
    valuesToPrint = list(range(1,n+1))
        
    print(*valuesToPrint, sep='', end='\n')
    
    
#Completing the next challenge:
    
    import numpy

if __name__ == '__main__':
    A = raw_input() #numpy.array((raw_input())
    example_string = A;
    Data = map(float, example_string.split(' '))
    A_Array = numpy.array(Data)
    #print(A_Array)
    print(numpy.floor(A_Array))
    print(numpy.ceil(A_Array))
    print(numpy.rint(A_Array))

#my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    