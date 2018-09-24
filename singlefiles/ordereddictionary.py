#Lets create a normal dict to demonstrate it does not save values in order
d={}

d['b']=2
d['a']=1
d['c']=3
d['d']=4
d['e']=5
d['f']=6
d['g']=7
d['h']=8
d['i']=9
d['j']=10
d['k']=11
d['l']=12
d['m']=13
d['n']=14
d['o']=15
d['p']=16
d['q']=17
d['r']=18
d['s']=19
d['t']=20
d['u']=21
d['v']=22
d['w']=23
d['x']=24
d['y']=25
d['z']=26

for k,v in d.items():
	print (k,v)
from collections import OrderedDict

d1=OrderedDict()

d1['a']=1
d1['b']=2
d1['c']=3
d1['d']=4
d1['e']=5
d1['f']=6
d1['g']=7
d1['h']=8
d1['i']=9
d1['j']=10
d1['k']=11
d1['l']=12
d1['m']=13
d1['n']=14
d1['o']=15
d1['p']=16
d1['q']=17
d1['r']=18
d1['s']=19
d1['t']=20
d1['u']=21
d1['v']=22
d1['w']=23
d1['x']=24
d1['y']=25
d1['z']=26

for k,v in d1.items():
	print (k,v)


d2 = OrderedDict()
d2['a']=2
d2['b']=1


d3=OrderedDict()
d3['b']=1
d3['a']=2

#Check two dicts are same
print(d2==d3)