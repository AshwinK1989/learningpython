#Usage of while and else
num=0
while num<5:
	print "The num is", num
	num=num+1
else:
	 print('Loop ended')    

#Usage of break statement

num=0
while num<5:
	if num==3:
		break
	print "The num is ",num
	num+=1

#Usage of Continue Statement
num=0
while num<5:
	num+=1
	if num == 2:
		continue
	
	print "The num is ",num

#Usage of pass, it is used when we want to implement something which is not ready and to avoid errors
num=0
while num==1:
	#comment
	pass


	
	

