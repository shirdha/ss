#shirdha
n,m=map(int,input().split())
c=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(0,len(b)):
    a.append(b[i])
    if c==0:
        print(max(a),end="")
        c=c+1
    else:
        print("",max(a),end="")
