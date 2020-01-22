#Compute minimum amount of coins needed to give change
print("Change machine")

#Assign variables
c_T=200
c_L=100
c_Q=25
c_D=10
c_N=5
c_P=1

#Input cents from user as integer
cents=int(input("Enter number of cents: "))

#Compute change from biggest coin to smallest by doing integer division then using remainder to compute next coin
print(cents//c_T, "Toonies")
cents=cents%c_T

print(cents//c_L, "Loonies")
cents=cents%c_L

print(cents//c_Q, "Quarters")
cents=cents%c_Q

print(cents//c_D, "Dimes")
cents=cents%c_D

print(cents//c_N, "Nickles")
cents=cents%c_N

print(cents, "Pennies")

#Blank input to keep code open
input()