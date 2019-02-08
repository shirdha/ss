n,k=map(int,input().split())
N=list(map(int,input().split()))
for i in N:
    if i==k:
        print("Yes")
        break
else:
    print("No")
