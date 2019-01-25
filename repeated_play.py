n=input()
d={}
r=[]
for i in n:
    c=n.count(i)
    d.update({i:c})
    r.append(d[i])

a=max(r)

for x,y in d.items():
    if y==a:
        print(x)
