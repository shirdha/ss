s=input()
c=0
d=0
for i in range(len(s)):
    if s[i].isdigit():
        c=c+1
    elif s[i].isalpha():
        d=d+1
if c>0 and d>0:
    print("Yes")
else:
    print("No")
