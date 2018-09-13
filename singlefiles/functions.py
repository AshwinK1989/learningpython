#function to print the name

def print_name(name):
	print('My name is '+name)

print_name('Ashwin')

#function to perform addition

def add_two_numbers(num1,num2):
	return num1+num2

print ('The sum of two numbers ',add_two_numbers(30,30))

#function to check whether a particular word is present in string

def check_String_Present(stringValue,word):
	return word in stringValue.lower()


print(check_String_Present('My name is Ashwin','ashwin'))