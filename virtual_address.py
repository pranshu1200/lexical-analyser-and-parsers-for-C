x=input()
y=''
l=[]
for i in x:
	if i==']' or i=='[' or i==';':
		y=y+' '
		y=y+i
		y=y+' '
	else:
		y=y+i
l=y.split()
#print(l)
error=0
if l[0]!='int' and l[0]!='float' and l[0]!='char':
	error=1
for i in range(len(l)):
	if l[i]=='[' and l[i+2]!=']':
		error=1
	if l[i]==']' and l[i-2]!='[':
		error=1
	if l[len(l)-1]!=';':
		error=1
	if l[i]=='[' and l[i+1].isnumeric()==0:
		error=1
	if l[len(l)-2]==';':
		error=1
#print(error)
if error==0:
	print("valid input")
	if l[0]=='int':
		print("type is int")
		e=4
	elif l[0]=='float':
		print("type is float")
		e=4
	else:
		print("type is char")
		e=1
	counta=0
	#countb=0
	for i in l:
		if i==']':
			counta+=1
	if counta==1:
		type=1
		print("1-D array")
	elif counta==2:
		type=2
		print("2-D array")
	if type==1:
		for i in range(len(l)):
			if l[i]=='[':
				row=(int)(l[i+1])
				#print(row)
	elif type==2:
		m=0
		for i in range(len(l)):
			if l[i]=='[' and m==0:
				row=(int)(l[i+1])
				#print(row)
				m=1
			if l[i]=='[' and m==1:
				col=(int)(l[i+1])
				#print(col)
if type==1 and error==0:
	print("enter source address")
	source=(int)(input())
	print("enter lower bound")
	lb=(int)(input())
	print("enter upper bound")
	ub=(int)(input())
	vo=source-lb*e
	print("virtual origin is at ",vo)
	print("enter array index I to be measured")
	I=(int)(input())
	if I<0 or I>=row:
		print("index out of bounds")
	else:
		print("address is at ",vo+I*e)
elif type==2 and error==0:
	print("enter source address")
	source=(int)(input())
	print("enter lower bound 1")
	lb1=(int)(input())
	print("enter upper bound1")
	ub1=(int)(input())
	print("enter lower bound2")
	lb2=(int)(input())
	print("enter upper bound2")
	ub2=(int)(input())
	s=(ub2-lb2+1)*e
	vo=source-(lb1*s)-(lb2*e)
	print("virtual origin is at ",vo)
	print("enter array index Ito be measured")
	I=(int)(input())
	print("enter array index J to be measured")
	J=(int)(input())
	if (I<0 or I>=row) or(J<0 and J>=col):
		print("index out of bounds")
	else:
		print("address is at ",I*s+e*J)
if error==1:
	print("invalid input")
		
	
		



