from treelib import Node,Tree

class Department(object):
    def __init__(self,dept):
        self.dept=dept
# class Manager_id(object):
#     def __init__(self,manage_id):
#         self.manage_id =manage_id
# class DOB(object):
#     def __init__(self,dob):
#         self.dob =dob

     
     


tree =Tree()
tree.create_node("fatima","fatima",data=Department("CEO"))
tree.create_node("Eva","eva",parent="fatima",data=Department("HR"))
tree.create_node("Delima","delima",parent="fatima",data=Department("OP"))
tree.create_node("Chandran","chandran",parent ="eva",data=Department("HR"))
tree.create_node("Arun","arun",parent="delima",data=Department("OP"))
tree.create_node("Bala","bala",parent="delima",data=Department("OP"))
tree.show()
#tree.show(data_property="dept")
a=str(input("enter the name of employee:"))
sub_t= tree.subtree(str(a),)
sub_t.show(data_property="dept")

