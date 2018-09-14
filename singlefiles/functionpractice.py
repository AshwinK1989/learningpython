#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶

def lesser_of_two_evens(a,b):
	if a%2==0 and b%2==0:
		return min(a,b)
	else:
		return max(a,b)


print('The number is ',lesser_of_two_evens(12,13))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶

def animal_crackers(text):
	splitValue= text.lower().split()
	return splitValue[0][0] == splitValue[1][0]

print(animal_crackers('Hello Honey'))


#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶


def makes_twenty(a,b):
	return sum((a,b))==20 or a==20 or b==20

print(makes_twenty(10,10))


#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶

def old_macdonald(name):
	first_half=name[:3]
	second_half=name[3:]

	return first_half.capitalize()+second_half.capitalize()

print(old_macdonald('macdonald'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed¶


def master_yoda(text):
	return " ".join(text.split()[::-1])


print(master_yoda("I am Home"))


#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200


def almost_there(n):
	return n in range(90,111) or n in range(190,211)


print(almost_there(90))
print(almost_there(150))
print(almost_there(210))

#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
	i=0
	while(i<len(nums)-1):
		if nums[i] ==3 and nums[i+1]==3:
			return True
		else:
			i=i+1
		


print(has_33([1,1,1,3,3]))
print(has_33([1,1,3,3,1]))


#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶

def paper_doll(text):
	value=''
	for item in text:
		value=value+item*3
	return value

print(paper_doll('Mississippi'))

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶


def blackjack(a,b,c):
	sumvalue = sum((a,b,c))
	if sumvalue<=21:
		return sumvalue
	elif sumvalue >21 and 11 in range(a,c+1):
		sumvalue= sumvalue-10
		if sumvalue>21:
			return 'BUST'
		else:
			return sumvalue
	else:
		return 'BUST'


print('The returned value is ',blackjack(5,6,7))
print('The returned value is ',blackjack(9,9,9))
print('The returned value is ',blackjack(9,9,11))

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶

def summer_69(arr):
	value=0
	for item in arr:
		if item in range(6,10):
			continue
		else:
			value=value+item
	return value

print('The sum is ',summer_69([2, 1, 6, 9, 11]))


#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
	code=[0,0,7,'x']

	for num in nums:
		if num == code[0]:
			code.pop(0)
	return len(code)==1

print(spy_game([1,2,3,0,0,7]))


#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number¶

def count_primes(num):
	count=0
	i=2
	for item in range(2,num+1):
		for item1 in range(2,int(item/2)):
			if item%item1==0:
				print('Number is not prime ',item)
			else:
				count=count+1
	return count


print('The number of prime nos ',count_primes(100))



