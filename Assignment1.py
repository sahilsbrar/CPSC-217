#     Sahil Brar (30021440)
# Draw a "happy face" that translates according to a users x and y input

# User input for translation (Original vales is x=450, y=20)
print("Pickle Rick Simulation! (x=400, y=300 for centered image")

x=float(input("Enter a x value: "))+50             # x+50 so it is centered when user inputs 400
y=float(input("Enter a y value: "))-280            # y-280 so image is centered when user inputs 300
# Image now shifts properly according to user input (Weird shaped image)

from SimpleGraphics import *   #Import function is after x and y input so image window opens after user enters input

background("dark sea green")

# Draw Pickle Ricks Body
setOutline("black")
setFill(53, 122, 7)
blob(x, y, x+180, y+100, x-150, y+519, x-348, y+418, x-139, y+235)

setOutline("forestgreen")
setFill("forestgreen")
blob(x-250, y+438, x-168, y+323, x-80, y+243, x-60, y+220, x-40, y+106, 
x+50, y+54, x+60, y+144, x-10, y+249, x-67, y+277, x-104, y+357, x-166, y+382)

# Spots on body
setOutline("darkgreen")
setFill("darkgreen")
blob(x+30, y+234, x+45, y+231, x+33, y+246)
blob(x-156, y+418, x-136, y+429, x-155, y+434)
blob(x-265, y+364, x-254, y+352, x-249, y+370)
blob(x-203, y+333, x-184, y+341, x-199, y+346)
blob(x-159, y+263, x-145, y+240, x-141, y+263)
blob(x-73, y+144, x-54, y+120, x-63, y+147)

setOutline("chartreuse3")
setFill("chartreuse3")
blob(x, y+60, x+12, y+65, x+37, y+55, x+30, y+50, x+25, y+50, x+10, y+48, x+5, y+55, x+8, y+55)

# Draw Eyebrow
setOutline("black")
setFill("lightsteelblue")
blob(x-10, y+88, x-6, y+70, x+45, y+70, x+70, y+105, x+59, y+118, x+35, y+75)

# Draw Eyes
setOutline("black")
setFill(209, 237, 201)
ellipse(x-36, y+100, 50, 50)   # Left eye
ellipse(x+7, y+120, 50, 50)    # Right eye

# Pupils
setFill("black")
ellipse(x-17, y+116, 5, 5)
ellipse(x+32, y+140, 5, 5)

# Draw Eye Bags
curve(x-40, y+137, x-37, y+157, x-20, y+155)  #Left
curve(x+15, y+172, x+33, y+184, x+45, y+173)  #Right

# Draw Nose
setOutline("black")
curve(x-9, y+149, x-22, y+161, x-20, y+180, x+3, y+160)

# Draw Mouth
setOutline("black")
setFill(2, 38, 0)
blob(x-41, y+163, x-23, y+184, x+5, y+184, x+32, y+192, x+34, y+220, \
x+1, y+234, x-47, y+216, x-69, y+200, x-75, y+170, x-59, y+155)

# Teeth (Top left to right)
setFill("seashell1")
blob(x-45, y+162, x-43, y+173, x-40, y+172, x-37, y+168)
blob(x-40, y+165, x-38, y+180, x-33, y+178, x-25, y+180)
blob(x-31, y+174, x-32, y+188, x-24, y+188, x-17, y+183, x-24, y+180)
blob(x-21, y+183, x-19, y+190, x-14, y+192, x-8, y+185, x-13, y+183)
blob(x-11, y+184, x-9, y+193, x-4, y+193, x+1, y+184, x-4, y+184)
blob(x-1, y+184, x+1, y+192, x+5, y+192, x+10, y+187, x+11, y+185, x+5, y+185)
blob(x+9, y+185, x+12, y+192, x+16, y+192, x+19, y+188)

# Teeth (Bottom left to right)
blob(x-68, y+199, x-62, y+199, x-56, y+201, x-60, y+207, x-63, y+203)
blob(x-61, y+207, x-54, y+201, x-50, y+202, x-50, y+214, x-55, y+210)
blob(x-51, y+213, x-48, y+204, x-41, y+204, x-40, y+218, x-44, y+216)
blob(x-43, y+217, x-38, y+209, x-33, y+209, x-31, y+224, x-34, y+221)
blob(x-35, y+223, x-28, y+213, x-24, y+215, x-21, y+225, x-20, y+225)
blob(x-22, y+226, x-20, y+219, x-14, y+219, x-11, y+229, x-14, y+228)
blob(x-13, y+228, x-10, y+222, x-3, y+222, x-2, y+230, x-5, y+230)

# Tongue
setOutline("black")
setFill("red2")
blob(x-4, y+231, x-2, y+214, x-24, y+203, x+6, y+203, x+8, y+217, x+8, y+228, x+8, y+230)

# Mouth Wrinkles
setOutline("black")
curve(x+26, y+186, x+35, y+194, x+40, y+211, x+30, y+229, x+13, y+235, x, y+235)                  #Right Wrinkle
curve(x-35, y+163, x-37, y+159, x-55, y+148, x-78, y+162, x-80, y+184, x-75, y+200, x-55, y+215)  #Left Wrinkle

# Text: I'm Pickle Rick!!
setOutline("steel blue")
setFont("Arial", "70", "bold")
text(x-230, y+180, "I'm")
text(x+157, y+350, "Pickle")
text(x+157, y+445, "Rick!!")