from collections import namedtuple

Dog = namedtuple('Dog','name age breed')

d = Dog('Tommy',12,'Lab')

print("The dog's name is {} whose age is {} and breed is {}".format(d.name,d.age,d.breed))