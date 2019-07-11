#f=open("input.txt","r")
#b=f.read()
b=input()
a=""
keyword=['int','float']
#for i in range(0,500):
#	b+='0'
for i in range(len(b)):
	if b[i]=='+' or b[i]=='-' or b[i]=='*' or b[i]=='/' or b[i]=='=' or b[i]==',' or b[i]==';' or b[i]=='}' or b[i]=='{' or b[i]==')' or b[i]=='(':
		a+=' '
		a+=b[i]
		a+=' '
	else:
		a+=b[i]
print(a)
a=a.split()
token=[]
for i in range(0,100):
    token.append(-1) 
for i in range(0,len(a)):
    if a[i] in keyword:
        if a[i]=='int':
            token[i]=0
        else:
            token[i]=20
    elif (a[i].isalpha() and token[0]==0) or '_' in a[i] or (a[i][0].isalpha() and a[i].isnumeric):
        token[i]=1
    elif (a[i].isalpha() and token[0]==20) or '_' in a[i] or (a[i][0].isalpha() and a[i].isnumeric) :
        token[i]=21;
    elif a[i].isnumeric():
        token[i]=2
    elif '.' in a[i]:
        token[i]=3
    elif a[i]=='=':
        token[i]=189
    elif a[i]=='+' or a[i]=='-' or a[i]=='*' or a[i]=='/'  :
    	token[i]=190
    elif a[i]==',':
        token[i]=191
    elif a[i]==';':
        token[i]=192
    elif a[i]=='}' or a[i]=='{' or a[i]=='(' or a[i]==')':
        token[i]==193
for i in range(0,len(a)):
    if token[i]==0:
        print(a[i],"integer keyword")
    elif token[i]==20:
        print(a[i],"float keyword")
    elif token[i]==1:
        print(a[i],"integer identifier")
    elif token[i]==21:
        print(a[i],"float identifier")
    elif token[i]==2:
        print(a[i],"integer constant")
    elif token[i]==3:
        print(a[i],"float constant")
    elif token[i]==189:
    	print(a[i],"assignment operator")
    elif token[i]==190:
    	print(a[i],"operator")
    elif token[i]==191:
    	print(a[i],"seperator")
    elif token[i]==192:
    	print(a[i],"EOL")
    elif token[i]==193:
        print(a[i],"bracket")
    else:
        print("wrong format")




