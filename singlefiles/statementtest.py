st = 'Print only the words that start with s in this sentence'

for item in st.split():
	if item[0]=='s':
		print(item)

#Use range() to print all the even numbers from 0 to 10.

list2 = range(0,11,2)
for item in list2:
	if item==0:
		continue
	print(item)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
list3 = [x for x in range(1,51) if x%3==0]
print(list3)

#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for item in st.split():
	if len(item)%2==0:
		print(item)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


for item in range(1,101):
	if item%3==0 and item%5==0:
		print('FizzBuzz')
	elif item%3==0:
		print('Fizz')
	elif item%5==0:
		print('Buzz')
	
	else:
		print(item)

#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
list4=[x[0] for x in st.split()]
print(list4)



