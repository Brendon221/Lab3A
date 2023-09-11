# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:06:40 2023

@author: bgodf
"""
# Name: JASON LAU
#       ERIC LIU
#       BRENDON GODFREY
#       ZANDER STRICKLER
#
# Section: 549
# Assignment: Lab 3A
# Date: 14 September 2023
import pandas as pd

#Names of the Group Members
Name1 = input("Type the first name\n")

Name2 = input("Type the second name\n")

Name3 = input("Type the third name\n")

Name4 = input("Type the fourth name\n")


#Birthdays using words only
print("When typing the birthday, type month then day then year")
print("")
Birthday1 = input("Type the first birthday\n")

Birthday2 = input("Type the second birthday\n")

Birthday3 = input("Type the third birthday\n")

Birthday4 = input("Type the fourth birthday\n")

    # Creating the DataFrame
df = pd.DataFrame({'Name':[Name1, Name2, Name3, Name4],
                   'Birthday':[Birthday1, Birthday2, Birthday3, Birthday4]})
  
# Create the index
index_ = ['Person 1', 'Person 2', 'Person 3', 'Person 4', ]
  
# Set the index
df.index = index_
  
# Print the DataFrame
print(df)