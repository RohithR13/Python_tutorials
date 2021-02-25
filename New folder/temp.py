# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import pandas as pd
import json
from pprint import pprint
dict1 ={"emp_id":1,"name":"arun","dob":"1/2/2000","manager_id":4,"dept":"operation"}

with open("emp.json","w+") as fp:
    json.dump(dict1,fp)

dict2 ={"emp_id":2,"name":"bala","dob":"1/2/2000","manager_id":4,"dept":"operation"}

with open("emp.json","a") as fp:
    json.dump(dict2,fp)

dict3 ={"emp_id":3,"name":"chandran","dob":"1/3/2000","manager_id":5,"dept":"hr"}

with open("emp.json","a") as fp:
    json.dump(dict3,fp)


dict4 ={"emp_id":4,"name":"delma","dob":"1/4/2000","manager_id":6,"dept":"operation"}

with open("emp.json","a") as fp:
    json.dump(dict4,fp)

dict5 ={"emp_id":5,"name":"eva","dob":"1/5/2000","manager_id":6,"dept":"hr"}

with open("emp.json","a") as fp:
    json.dump(dict5,fp)


dict6 ={"emp_id":6,"name":"fatima","dob":"1/6/2000","manager_id":1,"dept":"ceo"}

with open("emp.json","a") as fp:
    json.dump(dict6,fp)

# f =input("Enter the file name:")

# f=open("emp.json","r")
# contents=f.readlines()
# print(contents)

# d ={}
# with open("emp.json") as f:
#     for line in f:
#         (key,val) =line.split()
#         d[int(key)] = val
        

# df =pd.DataFrame(list(d.items()),columns =["emp_id","name","dob","manager_id","dept"])
# print(df)
# print(type(df))
with open("emp.json") as f:
    data =json.load("["+ f.read().replace("}\n{","}\n{")+"]")
    print(data)
with open("empj.json",encoding="utf-8-sig") as f:
    json_data =json.load(f)
    print(json_data)

    
    