#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:21:15 2017

@author: evanbaker
"""
import sys
import requests
import warnings

import matplotlib.pyplot as plt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
               
square = Rectangle.new_square(5)
print(square.calculate_area())

rec1 = Rectangle(5,4)
print(rec1.calculate_area())


# Make a new class for something interesting.  Add a method. 
# This doesn't fucking work - I don't understand. 
class Volume:
    def _init__(self, dates, volumes):
        self.dates = dates
        self.volumes = volumes
    
    def plot_volumes(self):
        plt.plot(self.volumes)
        
initialDates = [0,1,2,3,4,5]
initialVolumes = [0,1,3,4,3,2]        
BTC = Volume(initialDates,initialVolumes)
BTC.plot_volume


#==============================================================================
# Command+4 comments out a block of code.
# Command+5 uncomments out a block of code.
# test
# test
# test
# test
#==============================================================================

