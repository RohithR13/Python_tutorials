# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:46:27 2020

@author: Rohith R
"""
import csv
import json 
csv_column =["emp_id","name","dob","manager_id","dept"]
dict_data =[
    {"emp_id":1,"name":"arun","dob":"1/2/2000","manager_id":4,"dept":"operation"},
    {"emp_id":2,"name":"bala","dob":"1/2/2000","manager_id":4,"dept":"operation"},
    {"emp_id":3,"name":"chandran","dob":"1/3/2000","manager_id":5,"dept":"hr"},
    {"emp_id":4,"name":"delma","dob":"1/4/2000","manager_id":6,"dept":"operation"},
    {"emp_id":5,"name":"eva","dob":"1/5/2000","manager_id":6,"dept":"hr"},
    {"emp_id":6,"name":"fatima","dob":"1/6/2000","manager_id":None,"dept":"ceo"}
    ]
def search_id(manager_id):
    for keyval in items:
        if manager_id == keyval["manager_id"]:
            return keyval["emp_id"],keyval["name"]
csv_file ="emp.csv"
try:
    with open(csv_file,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=csv_column)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print ("I/o error")
f = open('emp.csv','r')
arr =[]
headers =[]
for header in f.readline().split(','):
    headers.append(header)
for line in f.readlines():
        lineItems = {}
        for i,item in enumerate(line.split(',')):
            lineItems[headers[i]] = item
        arr.append(lineItems)
f.close()
jsonText=json.dumps(arr)
json.dump(arr,open('empj.json','w'),indent=4,sort_keys=False)
print( jsonText)

with open('empj.json')as json_data:
    items= json.load(json_data)
    item =input("enter the id :")

    if(search_id(item) != None):
        print("the employee id is:",search_id(item))
    else:
        print("employe not found is ")




    

    