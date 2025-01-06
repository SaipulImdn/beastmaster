import os
from datetime import datetime

class ImageSaver:
    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def save(self, frame):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(self.storage_dir, f"capture_{timestamp}.jpg")
        cv2.imwrite(file_path, frame)
        return file_path
