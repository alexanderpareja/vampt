#!/usr/bin/env python

from PIL import Image, ImageOps
import os
import sys

# This function establishes dracula colors to colorize a grayscale image.
def apply_dracula(image):
    dracula_dark = (40, 42, 54)
    dracula_mid = (68, 71, 90)
    dracula_white = (248, 248, 242)
    return ImageOps.colorize(image.convert("L"), black=dracula_dark, white=dracula_white, mid=dracula_mid)

# This function applies the above colorization function to the image.
def image_proc(image_path, destination_path):
    try:
        img = Image.open(image_path)
        # Apply Dracula
        vampt_image = apply_dracula(img)
        # Save image.
        vampt_image.save(destination_path, "PNG")
        print(f"Image saved to {destination_path} successfully.")
    except Exception as error:
        print(f"Encountered an error during image processing.")
        print(f"Error message: {error}")
        import traceback
        traceback.print_exc()

# Main module.
if __name__ == "__main__":
    # Assure correct usage by checking arguments.
    if len(sys.argv) != 3:
        print("Usage: vampt.py <path-to-image> <path-to-save-location>")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    # Check if file exists.
    if not os.path.exists(input_path):
        print(f"Error: File not found. {input_path}")
        sys.exit(1)
    # Check if directory exists, if not, create one.
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Set up image output.
    base_name = os.path.basename(input_path)
    image_output = os.path.join(output_path, f"vampt_{base_name}")
    # Process image.
    image_proc(input_path, image_output)