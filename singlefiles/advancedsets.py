s=set()

#Adding value to the set
s.add(1)
s.add(2)

print(s)

#copy the set
sc = s.copy()
print(sc)

#clear the set
s.clear()
print(s)

#Difference: It will return the set by removing the same value present in other set
diff = {1,2,3}
diff1= {1,2,4}

print(diff.difference(diff1))

diff.difference_update(diff1)
print(diff)

#Intersection: It will return the same values present in two sets

inter = {1,2,3}
inter1 = {1,2,4}

print(inter.intersection(inter1))

inter.intersection_update(inter1)

print(inter)


#symmetric_difference: It will return the different values present in two sets
symm = {1,2,4}
symm1 = {1,2,3}

print(symm.symmetric_difference(symm1))

symm.symmetric_difference_update(symm1)

print(symm)

#discard: It will remove specific value from the set

dis = {1,2,3}

dis.discard(2)

print(dis)


#isdisjoint: It will return true if there are no common values in two sets

isdis = {1,2,4}

isdis1 = {3,5,6}

print(isdis.isdisjoint(isdis1))


#issubset: It will check if set1 is subset of set2
sub1 = {1,2,3}
sub2 = {1,2,3,4,5,6}

print(sub1.issubset(sub2))


#issuperset: It will check if set1 is superser of set2

sub1 = {1,2,3,4,5,6}
sub2 = {1,2,3}

print(sub1.issubset(sub2))


#union: it will return the combination of two sets
sub1 = {1,2,3,4,5,6}
sub2 = {1,2,3}

print(sub1.union(sub2))

#update: it will update the set with its own union and other set
upd={1,2,3}
upd1={4}
upd.update(upd1)
print(upd)

