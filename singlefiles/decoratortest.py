def decorator_test(func_passed):
	
	def greet():
		return 'This is a greet function'

	def welcome():
		return 'This is a welcome function'

	func_passed()
	print(greet())
	print(welcome())


@decorator_test
def check_Decorator():
	print('Function needs to be decorated')
