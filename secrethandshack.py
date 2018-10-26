alist={"1":"wink","10":"double blink","100":"close eyes","1000":"jump"}
print (alist)
n=int(input("Enter the decimal number: "))
a=bin(n)
b=a[2:]
print ("The binary number is: ",b)
blist=[]
alist1=list(str(b))
print ("The binary number in as spilt manner: ",alist1)
n=len(alist1)
flag=0
for i in reversed(range(n)):
   if(alist1[flag]!=0):
       e=str(alist1[flag])+str('0'*i)
       blist.append(e)
   flag+=1
print (blist)
clist=[]
for k,v in alist.items():
    for i in reversed(blist):
        if i==k:
            clist.append(v)
print(clist)





