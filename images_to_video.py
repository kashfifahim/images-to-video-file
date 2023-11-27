import cv2
import os

def resize_image(image, target_width, target_height):
    """
    Resize an image to fit within the specified dimensions while maintaining the original aspect ratio.
    """
    original_height, original_width = image.shape[:2]
    aspect_ratio = original_width / original_height
    
    if original_width > original_height:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    resized_image = cv2.resize(image, (new_width, new_height))
    
    # If the new dimensions are smaller in any direction, pad the resized image with black color
    top_padding = (target_height - new_height) // 2
    bottom_padding = target_height - new_height - top_padding
    left_padding = (target_width - new_width) // 2
    right_padding = target_width - new_width - left_padding

    return cv2.copyMakeBorder(resized_image, top_padding, bottom_padding, left_padding, right_padding, cv2.BORDER_CONSTANT, value=[0, 0, 0])

def images_to_video(image_folder, output_video_file, fps=30, duration=5, target_width=1920, target_height=1080):
    """
    Convert a set of images in a folder to a video.
    
    Parameters:
    - image_folder: path to the folder containing the images
    - output_video_file: path to the output video file (e.g., 'output.mp4')
    - fps: frames per second for the output video
    - duration: duration in seconds for each image to be displayed
    - target_width: width to resize images to
    - target_height: height to resize images to
    """
    
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()

    out = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, (target_width, target_height))
    
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        
        resized_img = resize_image(img, target_width, target_height)
        
        for _ in range(fps * duration):  # This will make each image last for 'duration' seconds
            out.write(resized_img)
    
    out.release()

# Example usage:
# images_to_video('path_to_image_folder', 'output_video.mp4', fps=30, duration=5)
images_to_video('images', 'hi_friend.mp4', fps=30, duration=20)