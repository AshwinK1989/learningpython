#Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
	for item in range(N):
		yield item**2


for x in gensquares(10):
    print(x)

#Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
#Note: Use the random library. For example:

import random

def rand_num(low,high,n):

	 for _ in range(n):
	 	yield random.randint(low,high)


for num in rand_num(1,10,20):
	print('The random number is ',num)


s =iter('Hello')

for item in s:
	print(item)



  
