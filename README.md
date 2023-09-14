 ## VAMPT - Dracula Wallpaper Tool

 ![screenshot](https://user-images.githubusercontent.com/134826922/266882902-9bb83ae7-5e41-4c96-b4a8-aac6459d0559.png)

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pillow Version](https://img.shields.io/badge/Pillow-8.3.2-blue)

Vampt is a command-line tool designed to convert images into black and white photos with a Dracula dark theme. It applies a filter using the Dracula background color #282a36 over the grayscale image, resulting in a stylish and aesthetic effect for Dracula themed environments.

## Features

- Converts any image type to black and white.
- Applies a Dracula dark theme color filter.
- Supports a wide range of image formats.

## Installation

Clone this repository to your local machine:

    git clone https://github.com/alexanderpareja/vampt.git

    cd vampt

Ensure you have Python 3.7 or higher installed.

   Install the required dependencies using pip:

    pip install Pillow

## Usage

   To use Vampt, run the following command in your terminal:

    python vampt.py <path-to-image> <path-to-save-location>

   \<path-to-image\>: The path to the input image you want to process.

   \<path-to-save-location\>: The directory where you want to save the processed image.

## Example:

    python3 vampt.py ~/wallpapers/image.jpg ~/wallpapers/vampt_wallpapers/

![screenshot](https://user-images.githubusercontent.com/134826922/266882913-10d57e29-96c3-42a3-bcea-ea346ae99831.png)
![screenshot](https://user-images.githubusercontent.com/134826922/266882919-c02f80b9-ccea-4900-99d2-83c504bfc9f1.png)



