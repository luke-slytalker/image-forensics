import sys
from PIL import Image, ImageChops
import argparse

# setup the ol' argParser so the user can supply input
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Imput image to run ELA on")

args = vars(ap.parse_args())

# load the image path into a variable
inp = args["image"]


TEMP = 'temp.jpg'       # temporary image name to save the ELA to
SCALE = 88              # Error Level scale.  Change this (along with the alpha value) to better check for manipulation
ALPHA = .40             # transparency level to blend the ELA with the original

def ELA():
    # Error Level Analysis for basic image forensics
    original = Image.open(inp)          # open up the input image
    original.save(TEMP, quality=95)     # re-save the image with a quality of 95%
    temporary = Image.open(TEMP)        # open up the re-saved image

    diff = ImageChops.difference(original, temporary)   # load in the images to look at pixel by pixel differences
    d = diff.load()                     # load the image into a variable
    WIDTH, HEIGHT = diff.size           # set the size into a tuple
    for x in range(WIDTH):                                  # row by row
        for y in range(HEIGHT):                             # column by column
            d[x, y] = tuple(k * SCALE for k in d[x, y])     # set the pixels to their x,y & color based on error


    diff.save('ela-saved.jpg')          # save the ELA version of the image
    #diff.show()                        # show the ELA version

    new_img = ImageChops.blend(temporary, diff, ALPHA)      # blend the original w/ the ELA @ a set alpha/transparency
    new_img.save('comp-saved.jpg', quality=95)              # save the image @ 95% quality

    new_img.show()          # display the blended image -- original + ELA

if __name__ == '__main__':
    ELA()