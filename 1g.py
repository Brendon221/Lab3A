# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:29:04 2023

@author: jason
"""

# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: JASON LAU
#       ERIC LIU
#       BRENDON GODFREY
#       ZANDER STRICKLER
# Section: 549
# Assignment: Lab 3A
# Date: 10 September 2023

import math
voltage = float(input("Enter Voltage:"))
refV = 1
print(20*math.log(voltage/refV,10), "Decibel volts")
