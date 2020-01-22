# Sahil Brar (30021440)
# Convert dog years to human years (1-2 Human years= 10.5, after that add 4 per human years)

# User input
print("Human years to dog years converter")
Hyears=float(input("Enter an age in Human years (Negative number to exit): "))

# Calculations
while Hyears>=0 and Hyears<=2:
    Dyears=Hyears*10.5
    print(Hyears, "is equivalent to", Dyears, "dog years.")
    Hyears=float(input("Enter an age in Human years (Negative number to exit): "))
    
    while Hyears>2:
        num=Hyears-2
        Dyears=(num*4)+21.0
        print(Hyears, "is equivalent to", Dyears, "dog years.")
        Hyears=float(input("Enter an age in Human years (Negative number to exit): "))

if Hyears<0:
    exit()