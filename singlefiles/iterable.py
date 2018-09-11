my_list =[1,2,3,4,5,6]

#For iterating through the list
for num in my_list:
	print(num)

#Priniting some value for number of items present in the list
for _ in my_list:
    print("Hello world")	

#Iterating through the string:
my_string='ashwin'

for chars in my_string:
	print(chars)

d = (1,2,3,4)

for num in d:
	print(num)

#There is also something as tuple unpacking, it will be used when we have tuples in the list:
tup_list = [(1,2),(3,4),(5,6)]

for a,b in tup_list:
    print(a)
    print(b)	

#Iterating through the keys present in dictionary
dicts = {"k1":"Ashwin","K2":"karangutkar"}

for key in dicts.keys():
	print('The key is '+key)

#Iterating through the values present in dictionary
for value in dicts.values():
	print('The value is '+ value)

#Iterating through the key and values present in dictionary:

for key,value in dicts.items():
	print('The key is '+ key)
	print('The value is '+ value)





