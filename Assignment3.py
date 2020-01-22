# Sahil Brar (30021440)
# Create a code that removes tourists from images using median of r, g, b

#----------------------------------------------------#
# ( ͡° ͜ʖ ͡°) COMPLETED A+ PORTION OF THE ASSIGNMENT!!! #
#----------------------------------------------------#

from SimpleGraphics import *
from os import listdir
from os.path import isfile, join
import fnmatch
THUMB_SIZE=4 # size of thumbnails
IMAGES_IN_ROW=4
IMAGE_LOC="./" # Directory/path of image set
IMAGE_EXT=".png" # Filename extenstion

# Part 1: Loading a collection of images
def loadImages():
  list_files=[]
  for entry in listdir(IMAGE_LOC):
    if isfile(join(IMAGE_LOC, entry)) and entry.endswith(IMAGE_EXT):
      list_files.append(entry) # Insert entries into the list of files only .png extension
  
  list_subjects=[]
  for file in list_files:
    rest_str=file.split("_")[0]
    list_subjects.append(rest_str)
  list_subjects=list(set(list_subjects)) # Get unique set and convert into the list
  print(list_subjects)

  # Prompt the user for the abbreviation that describes the subject of the photograph
  subject_photograph= input("Describe the subject of the photograph: ")
  if subject_photograph in list_subjects:
    filepattern=subject_photograph + "_*" + IMAGE_EXT
    n_photos=len(fnmatch.filter(listdir(IMAGE_LOC), filepattern))
    n_photos= n_photos
    print("There are", n_photos, "photos with that subject name.")
    print("Now displaying tourist free image.")
  else:
    # Program displays appropriate error message
    print("Error message: Could not find any photos with that subject name.")
    close()
    quit()
  
  if 3<=n_photos<=16:
    list_img=[] # empty list for images
    for i in range(1, n_photos+1):
      strImgLoc=IMAGE_LOC + subject_photograph + "_" + str(i) + IMAGE_EXT
      img=loadImage(strImgLoc) # Load image for given string image location
      list_img.append(img) # Append loaded image into list
    img_width=getWidth(list_img[0]) # Take first image in the list as a reference
    img_height=getHeight(list_img[0])
    resize(img_width*2, img_height) # window resized to 2*Width of image, height= height of img
    return list_img # Return list of images

  else:
    # Program displays appropriate error message
    print("Error message: Number of photos should be greater than or equal to 3 and less than or equal to 16.")
    close()
    quit()



 #----------------------Without A+ portion of assignment (below)--------------------------------------------------------------
  """
  # Prompt the user for the abbreviation that describes the subject of the photograph
  subject_photograph= input("Describe the subject of the photograph: ")
  
  # Prompt user for number of photos to load
  n_photos=int(input("Enter the number of photos to load: "))

  # Verify that number of photos is >=3 and <=16
  if 3<=n_photos<=16:
    list_img=[] # empty list for images
    for i in range(1, n_photos+1):
      strImgLoc=IMAGE_LOC + subject_photograph + "_" + str(i) + IMAGE_EXT
      img=loadImage(strImgLoc) # Load image for given string image location
      list_img.append(img) # Append loaded image into list
    img_width=getWidth(list_img[0]) # Take first image in the list as a reference
    img_height=getHeight(list_img[0])
    resize(img_width*2, img_height) # window resized to 2*Width of image, height= height of img
    return list_img # Return list of images
  
  else:
    # Program displays appropriate error message
    print("Error message: Number of photos should be greater than or equal to 3 and less than or equal to 16.")
    close()
    quit()
    """
#----------------------Without A+ portion of assignment (above)----------------------------------------------------------------



# Part 2: Create a thumbnail of the given images
# Parameters:
#     img: given img
# Return:
#    a new image which is 1/4 of prev image
def createThumbnail(img):
  #Create new image 1/4 size of prev
  new_img= createImage(getWidth(img)//THUMB_SIZE, getHeight(img)//THUMB_SIZE)

  for y in range(0, getHeight(img), THUMB_SIZE): # Traverse in y direction by jumping steps
    for x in range(0, getWidth(img), THUMB_SIZE): # Traverse in x direction
      r, g, b= getPixel(img, x, y) # Get the r,g,b values for each pixel
      putPixel(new_img, x//THUMB_SIZE, y//THUMB_SIZE, r, g, b) # Put pixel in new image
  return new_img

# Display the thumbnail version of images side by side putting 4 images in a row
# Parameters:
#     images: list of loaded images
# Return:(none)
def drawThumbnails(images):
  # Get height and width of the first image in the list and calculate dimensions of thumbnail
  thumb_width=getWidth(images[0])//THUMB_SIZE
  thumb_height=getHeight(images[0])//THUMB_SIZE

  for n in range(0, len(images)): # Loop through all images in the list
    # Calculate row and column no for given n
    col=n%IMAGES_IN_ROW
    row=n//IMAGES_IN_ROW
    thumb= createThumbnail(images[n]) # Get thumbnail version of image
    drawImage(thumb, thumb_width*col, thumb_height*row) # Draw image in the corresponding location
  


# Part 3:
def median(data):
  data.sort() # sort the data
  if len(data)%2==1:
    # Compute median as the middle value in the list
    median=data[len(data)//2]
  else:
    # Compute the median as the average of the two middle values in the list
    median=(data[len(data)//2] + data[len(data)//2-1])/2
  return median

def removeTourists(images): 
  # Create the tourist free image where size should be size of the loaded images
  new_img=createImage(getWidth(images[0]), getHeight(images[0]))
  
  for y in range(0, getHeight(images[0])): # Traverse in y direction
    for x in range(0, getWidth(images[0])): # Traverse in x direction
      r_list=[]
      g_list=[]
      b_list=[]
      for img in images:
        r, g, b=getPixel(img, x, y) # Get the r,g,b values for each pixel
        r_list.append(r)
        g_list.append(g)
        b_list.append(b)
      r_median=median(r_list)
      g_median=median(g_list)
      b_median=median(b_list)
      putPixel(new_img, x, y, r_median, g_median, b_median) # Put pixels into the new image
    # Draw the new image after processes each row
    drawImage(new_img, getWidth(images[0]), 0)
    update()# update the screen



# The main program loads the images, draws the thumbnails and then generates
# the tourist-free image
def main():
  images = loadImages()
  drawThumbnails(images)
  removeTourists(images)

main()