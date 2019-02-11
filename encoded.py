n=input()
s=''
for i in n:
    if i=='X' or i=='Y' or i=='Z':
        d=chr(ord(i)-23)
        s=s+d
    else:
        d=chr(ord(i)+3)
        s=s+d
print(s)

        
