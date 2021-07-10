# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 18:39:11 2021

@author: Aman Singhal
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('E:/Aman Skilledge/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('E:/Aman Skilledge/Aman.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('E:/Aman Skilledge/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('Aman.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)

