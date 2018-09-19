#Example where we try to open the file which is not available
def handleerrors():
	try:
		open('Ashwin.txt')
	except:
		print('File is not available')
	finally:
		print('Finally Block executed')


handleerrors()