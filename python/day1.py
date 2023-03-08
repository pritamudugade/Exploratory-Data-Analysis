a = "pritam udugade"
b = ""
for i in a:
    b = b + i
print("name is:",b)

a = [10,20,30,40,50,11,22,33,44,55]
b = []
c = []
for i in a:
    if i%10 == 0:
        b.append(i)
    elif i%11 == 0:
        c.append(i)
    else:
        print("not divisble by 10 nor by 11:")
print("divisible by 10:", b)
print("divisible by 11:", c)


a = ((12,22),(35,53),(84,91))
d = dict((y,x) for x, y in a)
print(d)
print(type(d))


# convert two list into dict

a = ["A","B","C"]
b = [11,22,33]
d = dict(zip(a,b))
print(d)


#by using for loop
c = {}
for i in range(len(a)):
    c.update({a[i]:b[i]})
print(c)


# merge two dictionaries

a = {'Ten': 10, 'Twenty': 20}
b = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

c = {**a, **b}
print(c)

d = a.copy()
d.update(b)
print(d)


# print history marks
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

# initialise with default

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)
