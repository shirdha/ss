n=input()
a=[]
for i in n:
    if i.isdigit():
        a.append(i)
print(*a)
