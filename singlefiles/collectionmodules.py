from collections import Counter

#Print the count of elements present in the list
l=[1,1,2,2,2,4,4,4,4,5,5,5,5,7,7,7,]
print(Counter(l))


#Print the count of chars in the string
s='kkkkklllllaaaaalllddddlkkk'
print(Counter(s))


#Print the count of each word in the string
k='Mumbai is Great Mumbai Great is Mumbai'
word=k.split()
c=Counter(word)
print(c)

#Example of using most_common
print(c.most_common(2))

#Other common patterns using the count object:->
#sum
print(sum(Counter(c.values())))

#convert it to list:
print(list(c))

#convert it to dict:
print(dict(c))

#convert it to set:
print(set(c))

#convert to list of count
print(list(c.values()))

#to get the least common element:
print(c.most_common()[:-2-1:-1])