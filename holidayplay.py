s=input("")
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday"]
for i in range(0,len(weekdays)):
    if(s==weekdays[i]):
        print("no")
        break
else:
    print("yes")
