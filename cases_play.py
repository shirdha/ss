string=input("")
s=""
for i in string:
    if i.isupper():
        s=s+i.lower()
    else:
        s=s+i.upper()
    
print(s)       
