#Example of creating class and attributes
class Dog():

	def __init__(self,breed,name,spots):
		self.breed=breed
		self.name=name
		self.spots=spots

my_dog = Dog('Lab','Tom',False)

print('The breed is '+my_dog.breed)
print('The name is '+my_dog.name)
print('Does the dog has spots? ',my_dog.spots)