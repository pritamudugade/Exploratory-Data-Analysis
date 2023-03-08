# Assignment-

# find sum of odd nums of factors
n = 68
f = []              # to store factors

for i in range(2,n+1):
  if n%i == 0:
    f.append(i)
#print(f)

odd = []
even = []
for x in f:        # access nums from list
  if x%2 == 0:
    even.append(x)
  else:
    odd.append(x)

#print(odd)
#print(even)

print("sum of odd nums:", sum(odd))
