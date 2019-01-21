n=int(input())
sq=0
while n!=0:
    r=n%10
    sq=sq+r*r
    n=n//10
print(sq)
