print("Reading the file myfile.txt")

myFile = open('myfile.txt')
print(myFile.read())

print("Moving the cursor to start")
myFile.seek(0)

print("Reading the file line wise")
print(myFile.readlines())
myFile.seek(0)

myFile.close()

print('By using folllowing way of opening file, we dont have to close it')
with open('myfile.txt') as MyFiles:
 print(MyFiles.read())


print('Write to a file')

with open('my_newFile.txt',mode='w') as f:
	f.write('This is first line')

print('Append to new file')
with open('my_newFile.txt',mode='a') as f:
    f.write('\nThis is second line')


print('Reading the new file')
with open('my_newFile.txt',mode='r') as f:
	print(f.read())
