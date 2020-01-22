from decimal import Decimal
#Compute how much money would be refunded if user was to recycle

#User enters number of containers
smallc=float(input("Enter number of small drink containers (1.0L or less): "))
bigc=float(input("Enter number of big drink containers (more than 1.0L): "))

#Compute amount of money refunded
refund=(smallc*0.10)+(bigc*0.25)

#Round to 2 decimal places
rrefund=round(refund,2)

#Display the results
print("From recycling, you would be able to get $",rrefund)

#Blank input to keep code open
input()