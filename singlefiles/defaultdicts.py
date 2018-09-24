
from collections import defaultdict

d={'k1':1}

print(d['k1'])

list1=[1,2,3,4,5]
list2=[6,6,8,9]

d=defaultdict(lambda:list1)
d=defaultdict(lambda:list2)

print(d['k3'])

print(d)
