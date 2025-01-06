import cv2

class Capture:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.camera = cv2.VideoCapture(camera_index)

    def get_frame(self):
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture frame from camera.")
        return frame

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()
