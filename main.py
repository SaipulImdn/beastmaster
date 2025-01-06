import time
from core.detector import Detector
from core.capture import Capture
from core.save_image import ImageSaver
from config.settings import CASCADE_PATH, STORAGE_DIR, CAMERA_INDEX

def main():
    print("Starting live detection...")
    detector = Detector(CASCADE_PATH)
    capture = Capture(CAMERA_INDEX)
    saver = ImageSaver(STORAGE_DIR)

    try:
        while True:
            frame = capture.get_frame()
            detected, objects = detector.detect(frame)

            if detected:
                print("Object detected! Capturing image...")
                file_path = saver.save(frame)
                print(f"Image saved to: {file_path}")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                print("Exiting...")
                break

            time.sleep(1)
    finally:
        capture.release()

if __name__ == "__main__":
    main()
