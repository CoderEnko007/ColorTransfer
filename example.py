from transfer import color_transfer
import numpy as np
import cv2
import argparse

def show_image(title, image, width = 300):
	print(image.shape)#image.shape[0]为高，image.shape[1]为宽
	r = width / float(image.shape[1])
	dim = (width, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

	cv2.imshow(title, resized)

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True)
ap.add_argument("-t", "--target", required = True)
args = vars(ap.parse_args())

source = cv2.imread(args["source"])
target = cv2.imread(args["target"])

transfer = color_transfer(source, target)

show_image("source", source)
show_image("target", target)
show_image("transfer", transfer)

cv2.waitKey(0)