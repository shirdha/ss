s=input("")
a=[]
for i in s:
    a.append(i)
print(a)
b=''
for j in range(0,len(a),2):
    a[j],a[j+1]=a[j+1],a[j]
    b=b+a[j]+a[j+1]
    print(b)
