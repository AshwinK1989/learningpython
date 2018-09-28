s='Hello World'
#Capitalize: It will capitalize the firsr character in the string
print(s.capitalize())

#lower: It will lower case the entire string
print(s.lower())

#upper: It will uppercase the string
print(s.upper())

#count: It will provide the count of particular character in the string
print(s.count('o'))

#center: It will surround the entire string with the characters we provide as we can also make a string of certain length
print(s.center(20,'o'))

#isalnum: Check whether the string is alphanumeric
print(s.isalnum())

#isalpha: Check whether the string is alphabetic
print(s.isalpha())

#isupper: Check whether the string is uppercase
print(s.isupper())

#islower: Check whether the string is lowercase
print(s.islower())

'Hello\tworld'.expandtabs()


#Check whether the string ends with a particular character
print(s.endswith('d'))



#Partition, It is similar to split. However it splits the string based on first match and it splits the string in two parts
print(s.partition(' '))