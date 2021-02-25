class A:
    def __init__(self) -> None:
        print("in a init")

    def features1(self):
        print("features 1 working")
    def features2(self):
        print("features 2 working")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("in b init")

    def features3(self):
        print("features 3 working")
    def features4(self):
        print("features 4 working")   

# class C(B,A):
#     def features5(self):
#         print("features 5 working")
#     def features5(self):
#         print("features 7 working")
    



a1 =A()
a1.features1()
a1.features2()
b1 = B()