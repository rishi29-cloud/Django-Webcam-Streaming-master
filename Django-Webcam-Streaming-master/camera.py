import cv2
from PIL import Image
import io
import time
from pytesseract import pytesseract

path_to_tesseract = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
from app.models import *
import base64


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        image = Image.open(io.BytesIO(frame))
        pytesseract.tesseract_cmd = path_to_tesseract
        time.sleep(0.5)
        text = pytesseract.image_to_string(image, lang='eng')
        cv2.waitKey(0)
        # print("input:5")
        if text:
            text = text.replace(" ", "")
            text_list = text.split("\n")
            for i in text_list:
                print("input:", i)
                if vehicle.objects.filter(vehicle_no__icontains=i) and len(i) > 2:
                    data = vehicle.objects.filter(vehicle_no__icontains=i)
                    for j in data:
                        print("Vehicle no:", j.vehicle_no)
                        print("owner:", j.owner)
                        print("model:", j.model)
                        print("year:", j.year)
                        print("Approved")
                        time.sleep(5)

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
