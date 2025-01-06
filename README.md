# Live Detection with Camera

This project implements a system for detecting living beings using a camera. When a living being is detected, the system captures a photo and saves it to a designated storage folder. The code follows clean architecture principles and clean coding practices for modularity and maintainability.

---

## Features

- Detects living beings in real-time using OpenCV.
- Automatically captures an image upon detection.
- Saves images in the `storage` folder with timestamps.
- Modular design following clean architecture principles.

---

## Project Structure

```
project/
│
├── core/
│   ├── detector.py       # Logic for detection
│   ├── capture.py        # Logic for capturing frmes
│   └── save_image.py     # Logic for saving images
│
├── config/
│   └── settings.py       # Application configuration
│
├── main.py               # Entry point of the application
└── storage/              # Folder for storing captured images
```

---

## Prerequisites

1. Python 3.x installed on your system.
2. OpenCV library for Python.
3. A functional camera connected to your device.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/beastmaster
   cd project
   ```

2. Install dependencies:

   ```bash
   pip install opencv-python
   ```

3. Download the Haar Cascade XML file for detection:

   - Download `haarcascade_frontalface_default.xml` from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades).
   - Place it in the project directory or specify its path in `config/settings.py`.

---

## Configuration

Edit the `config/settings.py` file to configure paths and parameters:

```python
CASCADE_PATH = "haarcascade_frontalface_default.xml"  # Path to Haar Cascade file
STORAGE_DIR = "storage"                              # Directory to save images
CAMERA_INDEX = 0                                      # Index of the camera
```

---

## Running the Application

1. Start the application:

   ```bash
   python main.py
   ```

2. Use the live detection system:

   - When a living being is detected, a photo will be taken and saved in the `storage` folder.
   - To exit the application, press `q`.

---

## Clean Architecture Explanation

### Core Components

- **Detection:**

  - The `Detector` class in `core/detector.py` handles the detection logic, using Haar Cascade for identifying objects in frames.

- **Capture:**

  - The `Capture` class in `core/capture.py` manages video feed capture from the camera.

- **Image Saving:**

  - The `ImageSaver` class in `core/save_image.py` manages saving images to the storage directory.

### Configurations

- All configuration parameters (e.g., paths, camera index) are centralized in `config/settings.py` for easy modification.

---

## Output

- Images are saved in the `storage` folder with filenames in the format `capture_YYYYMMDD_HHMMSS.jpg`.

---

## Debugging Tips

If the camera does not work or the program throws an error:

1. Ensure the camera is connected and functional.
2. Check the correct camera index by testing with a small OpenCV script:
   ```python
   import cv2
   cap = cv2.VideoCapture(0)  # Try different indices (e.g., 1, 2) if 0 doesn't work
   if not cap.isOpened():
       print("Failed to open camera.")
   else:
       print("Camera is working.")
   cap.release()
   ```
3. Verify that the Haar Cascade file is available at the specified path.

---

## Future Improvements

- Add support for multiple detection algorithms (e.g., deep learning models).
- Enable remote storage options (e.g., AWS S3, Google Drive).
- Add a GUI for displaying the live feed.

---

## License

This project is licensed under the MIT License.
