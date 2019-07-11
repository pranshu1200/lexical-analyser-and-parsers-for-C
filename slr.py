d={}
operator=['+','-','*','/','%','^']
d['E+T']='E'
d['E-T']='E'
d['T']='E'
d['T*F']='T'
d['T/F']='T'
d['T%F']='T'
d['F']='T'
d['id^P']='F'
d['P^F']='F'
d['id']='P'
d['P']='F'
x=input()
y=''
for i in range(0,len(x)):
    if x[i] in operator:
        y=y+' '
        y=y+x[i]
        y=y+' '
    else:
        y=y+x[i]
l=[]
l=y.split(' ')
print(l)
run=1
for i in l:
    if i not in operator:
        if i.isnumeric():
            l[l.index(i)]='id'
        else:
            print('invalid')
            run=0
print(l)
b=['E+','E-','T*','T/','T%','P^']
c=['E+T','E-T','T*F','T/F','T%F','P^F']
if run==1:
    stack=[]
    j=0
    while j<len(l):
        if l[j]=='id':
            stack.append(l[j])
            j=j+1
            print(stack)
        elif l[j] in operator:
            if stack[-1]+l[j] in b:
                stack.append(l[j])
                j=j+1
                print(stack)
            else:
                if len(stack)>=3:
                    str=''
                    str=str+stack[len(stack)-3]
                    str=str+stack[len(stack)-2]
                    str=str+stack[len(stack)-1]
                    if str in c:
                        del stack[len(stack)-1]
                        del stack[len(stack)-1]
                        del stack[len(stack)-1]
                        stack.append(d[str])
                        print(stack)
                    else:
                        str1=''
                        str1=stack[-1]
                        stack[-1]=d[str1]
                        print(stack)
                else:
                    str1=''
                    str1=stack[-1]
                    stack[-1]=d[str1]
                    print(stack)
    k=0
    #while stack[-1]!='E':
     #   if stack[-1]=='id' or stack[-1]=='F':
      #      stack[-1]=d[stack[-1]]
       #     print(stack)
        #else:
         #   z=''
          #  z=z.join(l[-3:-1])
           # stack=stack[:-3]+d[z]
            #print(stack)
    while len(stack)>1 or stack[0]!='E':
        if len(stack)>=3:
                str=''
                str=str+stack[len(stack)-3]
                str=str+stack[len(stack)-2]
                str=str+stack[len(stack)-1]
                if str in c:
                    del stack[len(stack)-1]
                    del stack[len(stack)-1]
                    del stack[len(stack)-1]
                    stack.append(d[str])
                    print(stack)
                else:
                    str1=''
                    str1=stack[-1]
                    stack[-1]=d[str1]
                    print(stack)
        else:
            str1=''
            str1=stack[-1]
            stack[-1]=d[str1]
            print(stack)
        
                        
