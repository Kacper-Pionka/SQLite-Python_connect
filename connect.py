# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('chinook.sqlite')
print("Opened database successfully");

cursor = conn.execute("SELECT DISTINCT billingcity, billingcountry FROM invoice ORDER BY billingcountry")
for row in cursor:
   print("billingcity = ", row[0])          #Returns non repeating combinations of billingcity
   print("billingcountry = ", row[1], "\n") #and billingcountry in alphabetic order of billingcountry element
print("Operation done successfully")
conn.close()
