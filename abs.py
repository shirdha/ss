a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a[0]*60+a[1]
d=b[0]*60+b[1]
e=abs(c-d)
print(str(e//60)+" "+str(e%60))
