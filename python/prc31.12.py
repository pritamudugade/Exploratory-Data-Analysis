# LCM
n1 = 3
n2 = 5

f1 = []
# factors of n1
for i in range(1,11):
  f1.append(i*n1)
print(f1)

f2 = []
# factors of n2
for j in range(1, 11):
  f2.append(j*n2)
print(f2)

l = list(set(f1) & set(f2))
print(l)
LCM = min(l)
print("LCM of given num is:", (LCM))


a = 16
b = 12

mi = min(a,b)
print(mi)

while (1):
  if ((mi%a == 0) and (mi% b == 0)):
    print("LCM:", mi)
    break
  mi = mi + 1

# LCM and GCD using math module
a = 18


b = 12
import math


GCD = math.gcd(a,b)
print("GCD is:", GCD)

import numpy as np

a = np.arange(1,100)
print(a)
print(sum(a))

"""
"""  
a = [[14, 16, 18], [12, 15, 17], [16, 16, 13]]
print(sum(a))




