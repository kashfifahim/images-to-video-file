# Image to Video Converter
Convert a sequence of images to a video usiing Python and OpenCV

## Requirements
- Python: Version 3.x or above.
- OpenCV-Python library: This library will provide the tools needed to read images and generate video.

## Setup & Installation:
1. Make sure you have Python 3 installed.
2. Install the `opencv-python` library using pip

## How to Use
1. Prepare Your Images: Place all your images in a single folder. The script assumes that the images are named sequentially (e.g., frame001.png, frame002.png, ...). Ensure they are in the order you want them to appear in the video.
2. Run the script. Navigate to the directory containing the script and run:
```python images_to_video.py```
By default, this will generate a video named output_video.avi with a frame rate of 30 FPS. If you want to customize the input folder, output video name, or frame rate, modify the parameters in the images_to_video function call within the script.

## Contributing
Feel free to fork this project and make your own changes. Pull requests are welcome!