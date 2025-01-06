import cv2

class Detector:
    def __init__(self, cascade_path: str):
        self.cascade = cv2.CascadeClassifier(cascade_path)

    def detect(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objects = self.cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return len(objects) > 0, objects
