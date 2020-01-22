# Sahil Brar (30021440)
# Plot a hurricane's track through the Caribbean and surrounding areas based off user's Latitude, Longitude, and wind speed

from SimpleGraphics import *
import sys
# Resize the window
WIDTH=1022
HEIGHT=620
resize(WIDTH, HEIGHT)
# Load the map from upper left corner of window
MAP=loadImage("map.gif")
drawImage(MAP, 0, 0)

# Add Longitude lines
NUM_LONG=8
NUM_SLOT=NUM_LONG+1
LEFT_EDGE=95
RIGHT_EDGE=50
for longl in range(1, NUM_SLOT):   # run the loop 8 times to draw lines
    setOutline("gray")
    xLong=longl*(WIDTH/NUM_SLOT)
    line(xLong, 0, xLong, HEIGHT)
    # Add number values for Longitude
    longStr=str(LEFT_EDGE-5*longl)+"W"       # Convert number into string
    setFont("14")
    text(xLong, 0, longStr, "nw")

# Add Latitude lines
NUM_LAT=4
num_SLOT=NUM_LAT+1
TOP_EDGE=35
BOTTOM_EDGE=10
for latl in range(1, num_SLOT):             # Run loop 4 times to draw lines
    setOutline("gray")
    yLat=latl*(HEIGHT/num_SLOT)
    line(0, yLat, WIDTH, yLat)
    # Add number values for Latitude
    latStr=str(TOP_EDGE-5*latl)+"N"      # Convert number into string
    setFont("14")
    text(0, yLat, latStr, "nw")

sys.stdin=open("earl.txt")

# User input (Latitude, Longitude, wind speeds) and turn into small grey circles
Lat=float(input("Enter a latitde: "))

#Track prev coords
prevX=0.0
prevY=0.0
maxwindspeed=0.0
maxcategory=0.0
PrevWind=0.0

while Lat != 0.0: #Take lat until it is 0
    # Calculate value of y location
    yLoc= (TOP_EDGE- Lat)*(HEIGHT/(TOP_EDGE-BOTTOM_EDGE))

    # Calculate value of x location
    Long=float(input("Enter a longitude:" )) *(-1.0)
    xLoc= (LEFT_EDGE-Long)*(WIDTH/(LEFT_EDGE-RIGHT_EDGE))
    
    windspeed=float(input("Enter a wind speed: "))
    if windspeed > maxwindspeed:
        maxwindspeed = windspeed

    # In first loop update the values of prev x and y with current x and y
    if prevX == 0.0:
        prevX=xLoc
        prevY=yLoc



    # Change colour and size of circles based off category
    if windspeed >= 157: # Category 5
        setFill("purple")
        setOutline("purple")
        ellipse(xLoc-7.5, yLoc-7.5, 15, 15)
        line(prevX, prevY, xLoc, yLoc)
        category=5
        
    elif windspeed >=130 and windspeed<157: # Category 4
        setFill("red")
        setOutline("red")
        ellipse(xLoc-6.5, yLoc-6.5, 13, 13)
        line(prevX, prevY, xLoc, yLoc)
        category=4
        
    elif windspeed>=111 and windspeed<130: # Category 3
        setFill("orange")
        setOutline("orange")
        ellipse(xLoc-5.5, yLoc-5.5, 11, 11)
        line(prevX, prevY, xLoc, yLoc)
        category=3

    elif windspeed>=96 and windspeed<111: # Category 2
        setFill("yellow")
        setOutline("yellow")
        ellipse(xLoc-4.5, yLoc-4.5, 9, 9)
        line(prevX, prevY, xLoc, yLoc)
        category=2
        
    elif windspeed>=74 and windspeed<96: # Category 1
        setFill("green")
        setOutline("green")
        ellipse(xLoc-3.5, yLoc-3.5, 7, 7)
        line(prevX, prevY, xLoc, yLoc)
        category=1

    else:
        setFill("gray")
        setOutline("gray")
        ellipse(xLoc-2.5, yLoc-2.5, 5, 5)
        line(prevX, prevY, xLoc, yLoc)
        category=0



    # Add lines and change colour according to higher category level
    if category < PrevWind:
        if PrevWind==5: # Category 5
            setOutline("purple")
            line(prevX, prevY, xLoc, yLoc)

        elif PrevWind==4: # Category 4
            setOutline("red")
            line(prevX, prevY, xLoc, yLoc)

        elif PrevWind==3: # Category 3
            setOutline("orange")
            line(prevX, prevY, xLoc, yLoc)

        elif PrevWind==2: # Category 2
            setOutline("yellow")
            line(prevX, prevY, xLoc, yLoc)

        elif PrevWind==1: # Category 1
            setOutline("green")
            line(prevX, prevY, xLoc, yLoc)
        

    if category>maxcategory: # Identify max Category throughout each loop
       maxcategory=category
        

    #Store the prev values just before taking input
    prevX=xLoc
    prevY=yLoc
    PrevWind = category

    #________________________________________________________________prev set of inputs^
    #Take next input
    Lat=float(input("Enter a Latitude: "))


# Report Maximum category and Max wind speed in upper left corner
setOutline("white")
setFont("14")
text(940, 35, "Max Category: "+str(maxcategory))
text(925, 50, "Max Wind Speed (mph): "+str(maxwindspeed))