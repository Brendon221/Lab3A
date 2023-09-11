# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:39:17 2023

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

Magnitude1= float(input("Enter First Richter Scale Value:"))
Magnitude2 = float(input("Enter Second Richter Scale Value:"))
EL1 = 10**(1.5*Magnitude1+4.4)
EL2 = 10**(1.5*Magnitude2+4.4)
Magnitude_diff = abs(Magnitude2-Magnitude1)
Ratio = 10**(1.5*Magnitude_diff)
print(f'The difference in two Richter Scale Values to the ratio of the energy released in two earthquakes is {Ratio}')
