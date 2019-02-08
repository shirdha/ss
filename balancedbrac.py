#shirdha
n=input()
for i in n:
    s=n.count('(')
    t=n.count(')')
if s==t:
    print("yes")
else:
    print("no")
