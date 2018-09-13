#Usage of Range in for loop
for num in range(0,10):
	print(num)

#Creating a list using range
list1 = range(0,10)
for num in list1:
	print(num)

#Using steps in range
list1 = range(0,10,2)
for num in list1:
	print(num)

#Example of enumerate function in python
d=('Ashwin','Karangutkar',29,'Dadar')
for indices,values in enumerate(d):
	print(indices)
	print(values)

#Example of using Zip function. Zip function is used to zip multiple list like it will club the elements index wise and return in a tuple

#Example of using Zip function

list1=[1,2,3]
list2=['Ashwin','Sagar','Aniket']
list3=['Dadar','Wadala','Navi Mumbai']

for item in zip(list1,list2,list3):
	print(item)

#If number of elements in one list is more than other list with which we have clubbed then it will return the shortest list combination

list1=[1,2,3,4,5]
list2=['Ashwin','Sagar','Aniket']
list3=['Dadar','Wadala','Navi Mumbai']

for item in zip(list1,list2,list3):
	print(item)

#in operator is used to check whether a particular value is present in data type. It returns boolean value


print("Hello" in "Hello World") #It will return true

list1= ['Ashwin','Sagar','Aniket']
print("Ashwin" in list1) #It will return true

d = {"Name":"Ashwin","Surname":"Karangutkar"}

print("Name" in d.values()) #It will return false
print("Keys" in d.keys()) #It will return true

#min function will return the minimun value
list4=[1,2,3,4,5,6,7,8,9,]
print(min(list4))

#max function will return the minimun value
list4=[1,2,3,4,5,6,7,8,9,]
print(max(list4))

#shuffle will randomly shuffle the list
from random import shuffle
print(shuffle(list4))

#randint will return random value from the range of numbers we provide
from random import randint
print(randint(0,100))

#To take an input from the user we have to use the input function. Input always returns the value as string
name= input("Enter your name")
print(name)