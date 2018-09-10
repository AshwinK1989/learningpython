my_dictionary = {'apples':150,'oranges':100,'bananas':60}

#Get the value from the dictionary
print(my_dictionary['apples'])

my_dictionary_dataTypes = {'Name':'Ashwin','Surname':'Karangutkar','age':29, 'hobbies':['Reading','Photography','Music'],'Residential Address':{'Building':'Mathura Bhuvan','PinCode':'400018'}}

print("Getting the Name ")
print(my_dictionary_dataTypes['Name'])


print("Getting the Age ")
print(my_dictionary_dataTypes['age'])


print("Getting the Hobbies ")
print(my_dictionary_dataTypes['hobbies'])

print("Getting the first Hobby ")
print(my_dictionary_dataTypes['hobbies'][0])


print("Getting the Building Name ")
print(my_dictionary_dataTypes['Residential Address']['Building'])


print("Getting the Keys ")
print(my_dictionary_dataTypes.keys())

print("Getting the Values ")
print(my_dictionary_dataTypes.values())

print("Getting the Pair ")
print(my_dictionary_dataTypes.items())
