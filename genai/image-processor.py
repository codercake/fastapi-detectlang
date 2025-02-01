import cv2
import numpy as np

def preprocess_image(image):

    #convert to grayscalw
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   #apply adaptive thresholding
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    #noise reduction
    denoised = cv2.fastNlMeansDenoising(binary)

    #deskewing
    coords = np.column_stack(np.where(denoised > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = 90 + angle
    return deskew_image(denoised, angle)


    