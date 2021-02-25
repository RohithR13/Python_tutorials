# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:14:06 2020

@author: Rohith R
"""

import csv
csv_column =["emp_id","name","dob","manager_id","dept"]
dict_data =[
    {"emp_id":1,"name":"arun","dob":"1/2/2000","manager_id":4,"dept":"operation"},
    {"emp_id":2,"name":"bala","dob":"1/2/2000","manager_id":4,"dept":"operation"},
    {"emp_id":3,"name":"chandran","dob":"1/3/2000","manager_id":5,"dept":"hr"},
    {"emp_id":4,"name":"delma","dob":"1/4/2000","manager_id":6,"dept":"operation"},
    {"emp_id":5,"name":"eva","dob":"1/5/2000","manager_id":6,"dept":"hr"},
    {"emp_id":6,"name":"fatima","dob":"1/6/2000","manager_id":None,"dept":"ceo"}
    ]
csv_file ="emp.csv"
try:
    with open(csv_file,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=csv_column)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print ("I/o error")