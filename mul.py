n=int(input(""))
a=0
c=0
for i in range(1,6):
    a=n*i
    if(c==0):
            print(a,end="")
            c=c+1
    else:
            print("",a,end="")
