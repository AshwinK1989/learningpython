#Creating a list from the Hello
list1 = [x for x in 'Hello']
print(list1)

#Creating a list of only even numbers
list2 =[x for x in range(0,100) if x%2==0]
print(list2)

#Creating a list of only even numbers multiplied by 2
list3 =[x*2 for x in range(0,100) if x%2==0]
print(list3)


#Example of nested for loop:
list6=[]

for x in [1,2,3]:
	for y in [100,200,300]:
		list6.append(x*y)
print(list6)