s=input()
d={}
l=[]
for i in s:
    a=s.count(i)
    d.update({i:a})
    l.append(a)

m=min(l)    #minimum
n=[]
for x,y in d.items():
    if y==m:
        n.append(x)
for i in range(0,len(n)):
	if i==0:
		print(n[i],end="")
	else:
		print("",n[i],end="")
