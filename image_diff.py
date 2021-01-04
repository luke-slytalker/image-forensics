from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2

# setup the ol' argParser so the user can supply input
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="base input image that is assumed to be the 'original'.")
ap.add_argument("-s", "--second", required=True,
	help="second image to compare against the base image to look for differences")
args = vars(ap.parse_args())

# load the two images so we can start testing them
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
# convert the images to grayscale so we can compare them as a more "apples to apples"
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)


# compute the Structural Similarity Index (SSIM) between the two images
(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))


# Threshold the difference image
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# Find contours to obtain the regions of the two input images where they differ
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


# loop over the contours
for c in cnts:
	# compute the bounding box of the contour
	(x, y, w, h) = cv2.boundingRect(c)
	# Draw bounding boxes on the first image where differences exist
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (55, 0, 255), 2)
	# Draw bounding boxes on the 2nd image where differences exist
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (55, 0, 255), 2)

# show the output images
cv2.imshow("ORIGINAL IMAGE", imageA)
cv2.imshow("SUSPECTED MODIFIED IMAGE", imageB)
cv2.imshow("DIFFERENCES", diff)
cv2.imshow("THRESHOLD", thresh)
cv2.waitKey(0)



