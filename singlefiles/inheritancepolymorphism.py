#Example of Inheritance
#Lets create a parent class Animal

class Animal():

	def __init__(self,name):
		self.name=name

	def walk(self):
		print("I can walk")

#Lets create a child class
class Dog(Animal):

	def __init__(self,name,breed):
		Animal.__init__(self,name)
		self.breed=breed


	def speak(self):
		print('I Woof and my name is {} '.format(Animal(self.name).name))


my_dog = Dog('Tom','Lab')
my_dog.speak()


#Example of polymorphism

#Lets create an abstract class

class Bird():

	def __init__(self,name):
		self.name=name


	def speak(self):
		raise "Method should be implemented in Base class"


class Eagle(Bird):

	def __init__(self,name):
		Bird.__init__(self,name)


	def speak(self):
		print('I speak in oww language'n)



eagle= Eagle('Nano')

eagle.speak()
