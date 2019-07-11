def isop(x):
	if x=='+' or x=='-' or x=='/' or x=='*' or x=='%' or x=='^':
		return 1
a=input()
#print(a)
run=1
for i in range(1,len(a)-1):
	if isop(a[i]) and isop(a[i+1]):
		print("invalid")
		run=0
	#if not isnum(a[i]) or not isop(a[i]):
		#print("invalid")
		#run=0
if isop(a[0]):
	print("invalid")
	run=0
if isop(a[len(a)-1]):
	print("invalid")
	run=0
l=''
if run==1:
	#l=a.list()
	#print(l)
	for i in range(len(a)):
		if isop(a[i]):
			l=l+' '
			l=l+a[i]
			l=l+' '
		else:
			l=l+a[i]
	l=l.split()
	#print(l)
	i=len(l)-1
	#while i>-1 :
		#if l[i]=='^':
			#v1=int(l[i-1])
			#v2=int(l[i+1])
			#ans=v1-v2
			#l[i]=ans
			#del l[i-1]
			#del l[i+1]
			#i=i-2
	#print(l)
	plus=0
	minus=0
	mul=0
	div=0
	pow=0
	mod=0
	for i in l:
	    if i=='+':
	        plus=plus+1
	    elif i=='-':
	        minus=minus+1
	    elif i=='*':
	        mul=mul+1
	    elif i=='/':
	        div=div+1
	    elif i=='^':
	        pow=pow+1
	    elif i=='%':
	        mod=mod+1
	x=len(l)-1
	while x>=0:
	    if l[x]=='^':
	        v1=int(l[x-1])
	        v2=int(l[x+1])
	        ans=v1**v2
	        del l[x]
	        del l[x]
	        del l[x-1]
	        l.insert(x-1,ans)
	        print(l)
	        print('f^p')
	    x=x-1
	for k in range(0,mul+div+mod):
	    for i in l:
		    if i=='*':
			    j=l.index(i)
			    v1=int(l[j-1])
			    v2=int(l[j+1])
			    ans=v1*v2
			    del l[j-1]
			    del l[j-1]
			    del l[j-1]
			    l.insert(j-1,ans)
			    print(l)
			    print('f*p')
			    break;
		    elif i=='/':
			    j=l.index(i)
			    v1=int(l[j-1])
			    v2=int(l[j+1])
			    ans=v1/v2
			    del l[j-1]
			    del l[j-1]
			    del l[j-1]
			    l.insert(j-1,ans)
			    print(l)
			    print('f/p')
			    break;
		    elif i=='%':
			    j=l.index(i)
			    v1=int(l[j-1])
			    v2=int(l[j+1])
			    ans=v1%v2
			    del l[j-1]
			    del l[j-1]
			    del l[j-1]
			    l.insert(j-1,ans)
			    print(l)
			    print('f%p')
			    break;
	for k in range(0,minus+plus):
	    for i in l:
		    if i=='-':
			    j=l.index(i)
			    v1=int(l[j-1])
			    v2=int(l[j+1])
			    ans=v1-v2
			    del l[j-1]
			    del l[j-1]
			    del l[j-1]
			    l.insert(j-1,ans)
			    print(l)
			    print('t-e')
			    break;
		    elif i=='+':
			    j=l.index(i)
			    v1=int(l[j-1])
			    v2=int(l[j+1])
			    ans=v1+v2
			    del l[j-1]
			    del l[j-1]
			    del l[j-1]
			    l.insert(j-1,ans)
			    print(l)
			    print('t+e')
			    break;


