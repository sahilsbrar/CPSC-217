# Sahil Brar (30021440)
# Setting up initial input from user to figure out their age in dog years
print("Find out your age in dog years!")
name=input("Enter your name: ")
Age=float(input("Enter your age: "))

# Math to convert age from human years to dog years
dog_years= Age * 7.0

#Final message with Name, Age, and Dog years displayed
print("I can't believe that", name, "is", Age, "years old! That's", dog_years, "in dog years! Wow you're old!")

#Blank input to keep code open
input()