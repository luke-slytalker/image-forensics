import cv2, argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="image to check")

args = vars(ap.parse_args())

path = args["image"]
src = cv2.imread(path)

# conversion codes
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV_FULL)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ycb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
lab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
invrt = cv2.bitwise_not(src)

# Displaying the image
cv2.imshow("HSV", hsv)
cv2.imshow("GRAY", gray)
cv2.imshow("YCB", ycb)
cv2.imshow("LAB", lab)
cv2.imshow("INVERTED", invrt)
cv2.waitKey(0)