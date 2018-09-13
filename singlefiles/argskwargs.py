#Example of using *args

def return_sum_of_numbers(*args):
	return sum(args)

print('The sum of numbers is ',return_sum_of_numbers(10,20,30))

#Example of using **kwargs, the key should not be quoted while passing
def return_favorite_food(**kwargs):
	return kwargs['nonveg']

print('My favorite food is '+return_favorite_food(veg='palak',nonveg='chicken'))

#Example of using args and kwargs

def myfunc(*args,**kwargs):
	print('I have {} {}'.format(args[0], kwargs['food']))


myfunc(10,20,30,food='eggs',perfumes='many')