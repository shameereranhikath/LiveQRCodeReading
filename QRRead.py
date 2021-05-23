# Library for Realtime Computer vision
import cv2
# Library for Mathematical Functions
import numpy
# Library for decoding the barcode and Qrcode from the image
from pyzbar.pyzbar import decode

# capturing the Videos or Frames from the Default WebCam
cap = cv2.VideoCapture(0)
# width of the windows set it for 640
cap.set(3, 640)
# height of the windows set it for 480
cap.set(4, 480)
# Reading the video continuously from the WebCam
while True:
    # getting the Image frame form the Webcam
    success, img = cap.read()
    code = decode(img)
    for qrCode in code:
        # converting the data into utf-8 encoding
        myData = qrCode.data.decode('utf-8')
        # to get the co-ordinates for the Qrcode of the image
        pts = numpy.array([qrCode.polygon], numpy.int32)
        # to get the Rectangular points for fixing the text on the image
        rectanglePoints = qrCode.rect
        # green lines are drawn on the area of the QR code in the image
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        # putting the text on the image
        cv2.putText(img, myData, (rectanglePoints[0], rectanglePoints[1]), cv2.FONT_ITALIC, 0.9, (0, 0, 255), 1)
        print(myData)
        # cv2.pol
# Result is showing
    cv2.imshow("Result Image", img)
    cv2.waitKey(2)
