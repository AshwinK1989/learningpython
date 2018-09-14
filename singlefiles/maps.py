#Example of Map function where it returns the square of the nos

def square_num(nums):
	return nums**2

item1=[1,2,3,4,5]
print(list(map(square_num,item1)))

#Example of Map function, where if the length of the string that we will provide is even then we will get Even in the list otherwise we will get first letter of the word
def slicer(text):
	if len(text)%2==0:
			return 'Even'
	else:
		return text[0]

names=['Andy','Vaishnavi','Sagar']

print(list(map(slicer,names)))