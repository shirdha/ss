n=int(input())
a=input()
c=""
d=["a","e","i","o","u"] #list contains vowels
for i in a:
    if i not in d:
        c=c+i
print(c[::-1])
