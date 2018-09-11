my_List = [1,2,3,4,5]

#len function to get the length of the list
print("The length of my_List is : ") 
print(len(my_List))

#Get particular element fro list using len
print("Second element in list is :") 
print(my_List[1])


#Get elements from position 0 to 3
print("Elements from position 0 to 2 are : ")
print(my_List[0:3])


my_otherList = [6,7,8,9,10]

print("Concating two different lists :") 
print(my_List+my_otherList)


#Changing last element from my_otherList
my_otherList[4]=11
print("Changing last element from my_otherList :") 
print(my_otherList)


my_unsorted_list = ['b','c','a','d','e','f']

#Sorting the list
print("The sorted list is ")
my_unsorted_list.sort()
print(my_unsorted_list)

#Reversing the the list

print("Reversing the list")
my_unsorted_list.reverse()
print(my_unsorted_list)

print("Adding an element at the end of the list")
my_unsorted_list.append('Last Element')
print(my_unsorted_list)

print("Removing last element from the list")
my_unsorted_list.pop()
print(my_unsorted_list)

print("Removing  element from the particular index")
my_unsorted_list.pop(0)
print(my_unsorted_list)



