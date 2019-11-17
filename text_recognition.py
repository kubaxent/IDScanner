# USAGE
# python text_recognition.py --east frozen_east_text_detection.pb --image images/legitka_02.jpg --padding 0.1

# import the necessary packages
from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import cv2
from PIL import Image, ImageEnhance


def processing(img):
    # load the input image and grab the image dimensions
    image = cv2.imread(img)
    image = cv2.resize(image, (3000, 3000))
    image1 = image[1050:1900, 1000:1900]
    image1 = cv2.resize(image1, (3000, 3000))
    image2 = image[1800:2800, 100:1200]
    image2 = cv2.resize(image2, (3000, 3000))
    image = np.concatenate((image1, image2), axis=0)

    # preprocessing
    img = Image.fromarray(image)
    en = ImageEnhance.Color(img)
    image = np.array(en.enhance(1.75))

    image = cv2.medianBlur(image, 3)

    b, g, r = cv2.split(image)
    ret, res = cv2.threshold(g, 95, 255, cv2.THRESH_BINARY)
    image = cv2.merge((res, res, res))

    # showing the preprocessed image
    test = cv2.resize(image,(1920,1080))
    cv2.imshow("Preprocessed:", test)
    cv2.waitKey(0)

    # in order to apply Tesseract v4 to OCR text we must supply
    # (1) a language, (2) an OEM flag of 4, indicating that the we
    # wish to use the LSTM neural net model for OCR, and finally
    # (3) an OEM value, in this case, 7 which implies that we are
    # treating the ROI as a single line of text
    config = "-l pol"
    text = pytesseract.image_to_string(image, config=config)

    return text


def main():
    processedString = processing('images/legita_01.jpg')


if __name__ == '__main__':
    main()