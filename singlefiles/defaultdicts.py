
from collections import defaultdict

d={'k1':1}

print(d['k1'])

list1=[1,2,3,4,5]
d=defaultdict(lambda:list1)

print(d['k2'])

print(d)
