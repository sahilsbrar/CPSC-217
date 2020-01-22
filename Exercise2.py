#      Sahil Brar (30021440)
from SimpleGraphics import *
# Draw a house with a door/window/roof as well as the sky with a cloud/sun and the ground with a name in the corner
# Sky background
background("deep sky blue")

# Draw Grass
setOutline("forest green")
setFill("forest green")
rect(0, 350, 800, 300)

# Draw house
setOutline("black")
setFill("burlywood3")
rect(225, 200, 350, 240)

# Draw door
setOutline("black")
setFill("dark slate grey")
rect(280, 260, 100, 180)

setOutline("black")
setFill("goldenrod2")
ellipse(355, 340, 15, 15)

# Draw Roof
setOutline("black")
setFill("brown4")
polygon(175, 220, 625, 220, 400, 100)

# Draw Window
setOutline("black")
setFill("light goldenrod")
rect(420, 280, 125, 75)

setOutline("black")
line(483, 280, 483, 355)
line(420, 318, 545, 318)

# Draw cloud
setOutline("whitesmoke")
setFill("whitesmoke")
blob(40, 58, 100, 30, 150, 60, 200, 30, 250, 60, 280, 100, 250, 150, 200, 180, 150, 150, 75, 180, 30, 180)

# Draw Sun
setOutline("yellow")
setFill("yellow")
pieSlice(625, -100, 300, 300, 95, 270)
rect(750, 0, 55, 100)

# Draw name
setOutline("black")
setFont("comicsans", "20", "bold")
text(725, 550, "Sahil Brar")
setFont("comicsans", "18", "bold")
text(725, 580, "30021440")