# AI Image Editing Application

## Overview

The **AI Image Editing Application** is a powerful tool that enables users to edit images using natural language prompts. Built with Python and the Gradio library, this application allows users to adjust various aspects of images such as brightness, contrast, color, sharpness, blur, crop, and resize seamlessly.

## Features

- **Image Upload**: Users can upload images for editing.
- **Natural Language Processing**: Enter prompts to specify the desired adjustments.
- **Multiple Edits**: Adjust brightness, contrast, color, sharpness, blur, crop, and resize images.
- **Real-time Results**: View edited images instantly.

## Installation

To run this application, you need to have Python 3.7 or higher installed. You can install the required libraries using the following command:

```bash
pip install gradio pillow numpy opencv-python-headless



# Usage
Upload an Image: Click on the upload button to select an image from your device.
Enter Editing Prompt: Use the textbox to enter your editing command, such as:
brighten by 1.5
contrast by 1.2
crop to 50, 50, 200, 200
resize to 300, 300
View the Edited Image: The application will process your request and display the edited image.
Code Structure
The application consists of the following core functions:

interpret_prompt(prompt): Parses user prompts and determines the necessary adjustments.
adjust_brightness_contrast_color(image, brightness, contrast, color): Adjusts the brightness, contrast, and color intensity of the image.
sharpen_image(image, sharpness): Sharpens the image based on the specified sharpness level.
blur_image(image, blur_intensity): Applies a Gaussian blur to the image.
crop_image(image, top, left, height, width): Crops the image to a specified region.
resize_image(image, new_width, new_height): Resizes the image to the specified dimensions.
process_image(image, prompt): Main function that applies all edits based on the user's prompt.
Gradio Interface
The Gradio interface consists of:

An image upload component for selecting the image.
A textbox for entering editing prompts.
A display area for showing the edited image.
Conclusion
This AI Image Editing Application simplifies the image editing process through intuitive natural language commands, making it accessible for all users.
