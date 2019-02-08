n=input()
a=list(n)
a1=len(n)
if a1%2==1:
    a[a1//2]="*"
else:
    a[a1//2],a[(a1//2)-1]="*","*"
v=''.join(map(str,a))
print(v)
