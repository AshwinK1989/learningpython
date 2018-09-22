def return_cubes(n):
	for x in range(n):
		yield x**3


print(list(return_cubes(10)))