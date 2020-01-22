import math 
import numpy
# Setting up entry method for user to enter numbers for Latitude and Longitude
print("Enter latitude and longitude for 2 different points in Degrees")


print("Enter Latitude 1")
t1=float(input())
T1=math.radians(t1)

print("Enter Longitude 1")
g1=float(input())
G1=math.radians(g1)

print("Enter Latitude 2")
t2=float(input())
T2=math.radians(t2)

print("Enter Longitude 2")
g2=float(input())
G2=math.radians(g2)

# Equation for determining distance between the two points
# 6371.01 is the average radius of the Earth in KM
distance = 6371.01 * numpy.arccos(math.sin(T1) * math.sin(T2) + math.cos(T1) * math.cos(T2) * math.cos(G1 -G2))

print("The distance between the two points is", distance, "KM.")

# Blank input to ensure code stays open
input()