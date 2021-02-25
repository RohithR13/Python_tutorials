a=5
b=0
try:
    print(a/b)
except Exception as e:
    print("you cannot divide  anumber by zero", e)
finally:
    print("division is done")