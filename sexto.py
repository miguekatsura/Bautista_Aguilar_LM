n1=0
n2=1
sig=0
print 1,":",n1
print 2,":",n2
for i in range(0,100):
	sig=n1+n2
	print i+1,":",sig
	n1=n2
	n2=sig
