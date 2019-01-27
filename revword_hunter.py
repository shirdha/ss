def revword(s): 
   
   w = s.split(" ")
   nw = [i[::-1] for i in w]
   ns = " ".join(nw)
   return ns

s = input("")
print(revword(s))
