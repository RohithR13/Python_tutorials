import numpy as np
n =int( input(""))

for x in range(n):
     a =np.array([(input().split())],float)
np.set_printoptions(legacy='1.13')
print(round(np.linalg.det(a),2))


