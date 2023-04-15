import sqlite3
from datetime import datetime




############ Connect ############

cnt = sqlite3.connect('database/Banks.db')


#################################


#### bank ####

sql=''' CREATE TABLE bank
     (id INTEGER PRIMARY KEY,
     bankname CHAR(30) NOT NULL,
     numberOfbranches INT(10) NOT NULL,
     MarketOfvolume INT(20) NOT NULL)'''
     

cnt.execute(sql)
print("Table 1 created succssefully")
#cnt.close()


#### customer ####


sql=''' CREATE TABLE customer
     (id INTEGER PRIMARY KEY,
     name CHAR(30) NOT NULL,
     lastname CHAR(30) NOT NULL,
     number INT(20) NOT NULL,
     birthday CHAR(20) NOT NULL,
     email CHAR(20) NOT NULL,
     city CHAR(20) NOT NULL,
     code CHAR(20) NOT NULL)'''
     

cnt.execute(sql)
print("Table 2 created succssefully")
#cnt.close()


#### order ####


sql=''' CREATE TABLE Orders
     (id INTEGER PRIMARY KEY,
     aid INT(30) NOT NULL,
     bid INT(30) NOT NULL,
     method CHAR(20) NOT NULL,
     fee INT(20) NOT NULL,
     time CHAR(20) NOT NULL,
     balance INT(20) NOT NULL)'''
     

cnt.execute(sql)
print("Table 3 created succssefully")
#cnt.close()


#### account ####

sql=''' CREATE TABLE account
     (id INTEGER PRIMARY KEY,
     bid INT(30) NOT NULL,
     loan INT(20) NOT NULL,
     outstandingloan INT(20) NOT NULL,
     balance INT(20) NOT NULL,
     username CHAR(20) NOT NULL,
     password CHAR(20) NOT NULL)'''
     

cnt.execute(sql)
print("Table 4 created succssefully")
cnt.close()


##############################












