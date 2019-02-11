n=input()
s=''
for i in n:
    if i=='x' or i=='y' or i=='z':
        d=chr(ord(i)-23)
        s=s+d
    else:
        d=chr(ord(i)+3)
        s=s+d
print(s)

        
