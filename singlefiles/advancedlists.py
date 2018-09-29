#extend: It is used to combine two lists.
l1 = [1,2,3]
l2=[4,5,6]

l1.extend(l2)
print(l1)

##index(): It is used to add an element at a particular index
print(l1.index(2))

#insert(): It is used to insert the value at a particular index
l1.insert(6,7)
print(l1)

#remove:It is used to remove an element from a list.
l1.remove(7)
print(l1)