import os
from PIL import Image, ImageFilter

# Specify the input and output directories
input_folder = '/home/ian_ng/Downloads/gs-data/example_locomotive/input'  # Change this to your input folder path
output_folder = '/home/ian_ng/Downloads/gs-data/example_locomotive_downsampled/input'   # Change this to your output folder path

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Extract the numeric part of the filename
        base_name = filename.split('.')[0]  # Get the part before the extension
        number = int(base_name)  # Convert to integer

        # Process only if the number is divisible by 3
        # Open the image
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Apply Gaussian blur
        worsened_img = img.filter(ImageFilter.GaussianBlur(radius=1))

        # Save the worsened image
        worsened_img_path = os.path.join(output_folder, filename)
        worsened_img.save(worsened_img_path)

        print(f'Processed: {filename}')

print('All applicable images processed.')