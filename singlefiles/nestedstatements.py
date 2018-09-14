# Example of nested methods in python

x =50

def func(x):
	
	print('The value of x',x)

	def func1():
		x=10
		print('The value of x ',x)
	func1()


func(20)


# Example of using Global Keyword

x1 =50

def func():
	global x1
	x1=15

	print('The value of x',x1)

	def func1():
		x1=10
		print('The value of x ',x1)
	func1()


func()