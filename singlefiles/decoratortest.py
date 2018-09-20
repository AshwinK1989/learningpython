def decorator_test(func_new):

	def greet():
		return 'I am a function to greet'

	func_new()

	def welcome():
		return 'I am a function to welcome'

	print(greet())
	print(func_new())
	print(welcome())



@decorator_test
def decorator_function():
	print('I am the new function')
	return 'I am the function to serve food'