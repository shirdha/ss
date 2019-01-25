import math
a,b=map(int,input().split())
c=a*b
d=math.sqrt(c)
e=int(d)
if d==e:
    print("yes")
else:
    print("no")
