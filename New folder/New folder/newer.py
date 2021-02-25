import json
from typing import Dict


def search_id(item):
    for keyval in items:
        if (item == keyval["manager_id"]):
            print( keyval["emp_id"]," "+keyval["name"])
        
    return True
    
       
    
with open('empj.json')as json_data:
    items= json.load(json_data)
    item =input("enter the id :")

    if(search_id(item) != None):
        print("the employee id is:",search_id(item))
        print(b)
    else:
         print("No other employe not found is  ")
    
   
    