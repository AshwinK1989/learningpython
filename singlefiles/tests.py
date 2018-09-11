#Answer of first expression is 44
print(4 * (6 + 5))

#Answer of second expression is 29
print(4 * 6 + 5 )


#Answer of third expression is 34
print(4 + 6 * 5 )

#Type of below expression is float
print(type(3 + 1.5 + 4))

#What would you use to find a numbers square root, as well as its square?(Dont know)

# Print out 'e' using indexing for hello
s='hello'
print(s[1])

# Reverse the string using slicing
print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.

print(s[4])

print(s[-1])

#Build this list [0,0,0] two separate ways. (Don't know second method)

list1 = list()
list1.insert(0,0)
list1.insert(0,0)
list1.insert(0,0)

print(list1)

list2 =[0]*3
print(list2)

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]

list3[2][2]='goodbye'

print(list3)

#Sort the list below:

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

# Grab 'hello'
d = {'simple_key':'hello'}
print(d['simple_key'])

# Grab 'hello
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

# Getting a little tricker #Grab hello
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying! (Don't Know)
#Can you sort a dictionary? Why or why not?

#Use a set to find the unique values of the list below:

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))

print(4**0.5)
print(4**0.5 != 2)

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

print(l_one[2][0] >= l_two[2]['k1'])

