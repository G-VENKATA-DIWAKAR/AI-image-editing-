
import gradio as gr
from PIL import Image, ImageEnhance
import numpy as np
import cv2
import re

def interpret_prompt(prompt):
    """Interpret user prompt and return corresponding adjustments."""
    adjustments = {
        "brightness": 1.0,
        "contrast": 1.0,
        "color": 1.0,
        "sharpness": 1.0,
        "blur": 0,
        "crop": None,
        "resize": None
    }

    
    if "brighten" in prompt:
        match = re.search(r'brighten by (\d+(\.\d+)?)', prompt)
        if match:
            adjustments["brightness"] = float(match.group(1))
    
   
    if "contrast" in prompt:
        match = re.search(r'contrast by (\d+(\.\d+)?)', prompt)
        if match:
            adjustments["contrast"] = float(match.group(1))

   
    if "color" in prompt:
        match = re.search(r'color by (\d+(\.\d+)?)', prompt)
        if match:
            adjustments["color"] = float(match.group(1))

    
    if "sharpen" in prompt:
        match = re.search(r'sharpen by (\d+(\.\d+)?)', prompt)
        if match:
            adjustments["sharpness"] = float(match.group(1))

    
    if "blur" in prompt:
        match = re.search(r'blur by (\d+)', prompt)
        if match:
            adjustments["blur"] = int(match.group(1))

    
    if "crop" in prompt:
        match = re.search(r'crop to (\d+), (\d+), (\d+), (\d+)', prompt)
        if match:
            adjustments["crop"] = (
                int(match.group(1)),  
                int(match.group(2)),  
                int(match.group(3)),  
                int(match.group(4))   
            )

    
    if "resize" in prompt:
        match = re.search(r'resize to (\d+), (\d+)', prompt)
        if match:
            adjustments["resize"] = (
                int(match.group(1)),  
                int(match.group(2))   
            )

    return adjustments

def adjust_brightness_contrast_color(image, brightness=1.0, contrast=1.0, color=1.0):
    """Adjust brightness, contrast, and color intensity of the image."""
    img = Image.fromarray(image)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(color)
    return np.array(img)

def sharpen_image(image, sharpness=1.0):
    """Adjust sharpness of the image."""
    img = Image.fromarray(image)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)
    return np.array(img)

def blur_image(image, blur_intensity=0):
    """Apply blur to the image."""
    img = np.array(image)
    if blur_intensity > 0:
        img = cv2.GaussianBlur(img, (2 * blur_intensity + 1, 2 * blur_intensity + 1), 0)
    return img

def crop_image(image, top=0, left=0, height=100, width=100):
    """Crop the image to a specified region."""
    img = Image.fromarray(image)
    cropped_img = img.crop((left, top, left + width, top + height))
    return np.array(cropped_img)

def resize_image(image, new_width=100, new_height=100):
    """Resize the image to the specified width and height."""
    img = Image.fromarray(image)
    resized_img = img.resize((new_width, new_height))
    return np.array(resized_img)

def process_image(image, prompt):
    """Main function to apply edits based on prompt and return the result."""
    adjustments = interpret_prompt(prompt)

    
    edited_image = adjust_brightness_contrast_color(image, 
                                                     adjustments["brightness"], 
                                                     adjustments["contrast"], 
                                                     adjustments["color"])

   
    edited_image = sharpen_image(edited_image, adjustments["sharpness"])

   
    edited_image = blur_image(edited_image, adjustments["blur"])

    
    if adjustments["crop"]:
        edited_image = crop_image(edited_image, *adjustments["crop"])

    
    if adjustments["resize"]:
        edited_image = resize_image(edited_image, *adjustments["resize"])

    return edited_image


image_input = gr.Image(type="numpy", label="Upload Image")
prompt_input = gr.Textbox(label="Enter your editing prompt", placeholder="e.g., 'brighten by 1.5'")

image_output = gr.Image(type="numpy", label="Edited Image")

iface = gr.Interface(
    fn=process_image,
    inputs=[image_input, prompt_input],
    outputs=image_output,
    title="AI Image Editing Application",
    description="Edit images using natural language prompts."
)

iface.launch(share=True)
