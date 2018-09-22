def reverse_string(str):
	length=len(str)

	for i in range(length-1,-1,-1):
		yield str[i]


for letter in reverse_string('Ashwin'):
	print(letter)