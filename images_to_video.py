import cv2
import os

def images_to_video(image_folder, output_video_file, fps=30):
    """
    Convert a set of images in a folder to a video.
    
    Parameters:
    - image_folder: path to the folder containing the images
    - output_video_file: path to the output video file (e.g., 'output.avi')
    - fps: frames per second for the output video
    """
    
    # Get all files from the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    
    # Sort the images by name
    images.sort()
    
    # Determine the width and height from the first image
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    h, w, layers = frame.shape
    size = (w,h)
    
    # Create a video writer object
    out = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    
    # Write each image to the video writer
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        out.write(img)
    
    # Release the video writer object
    out.release()

# Example usage:
# images_to_video('path_to_image_folder', 'output_video.avi', fps=30)

images_to_video('images', 'outout_video.avi', fps=30)