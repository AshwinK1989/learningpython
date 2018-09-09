name="Ashwin"

#use of \n to print on next line
print("Hello \nWorld")

#use of \t to mimic tab i.e four spaces between words
print("Hello\tWorld")

#use of len() function to return the length of the string
print(len(name))

#Example of indexing: It should print "A"
print(name[0])

#Example of Reverse Indexing : It should print "i"
print(name[-2])

#Example of Slicing : It should print "Ash"
print(name[0:3])

#Example of Slicing name from "s" to end
print(name[1:])

#Example of Slicing name from "A" to "i"
print(name[:5])

str="abcdefghijk"
print("After Jump "+ str[::2])

#Trick to reverse the string
print("Reversed String "+str[::-1])

sentence = "DaD si DaD"
print("Reversed Sentence "+sentence[::-1])
