import os
import cv2
import numpy as np
import pytesseract
from Levenshtein import distance



# tesseract ocr configuration
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # this path may be different for you. Check where the Tesseract library is
config = ('-l eng --oem 1 --psm 3')


image_dir = r"the path to the folder containing the images you want to scann"
classified_dir = r"path to folder to save results"

# scan images
for filename in os.listdir(image_dir):
   
    image = cv2.imread(os.path.join(image_dir, filename))  # read images

    
    text = pytesseract.image_to_string(image, config=config) # Read the text in the iamge

    # calculate the similarity ratio
    similarity = 0
    for text2 in texts:
        similarity = max(similarity, distance(text, text2))

    # classify the image. create and save "similar" and "different" folders
    if similarity > 70:
        cv2.imwrite(os.path.join(classified_dir, "similar", filename), image) #you can enter the folder name you want it to create here
    else:
        cv2.imwrite(os.path.join(classified_dir, "different", filename), image) #and here


