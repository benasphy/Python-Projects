# filepath: /Users/teru/Python Projects/Text to handwriting/text_to_handwriting.py
from PIL import Image, ImageDraw, ImageFont

txt = "Hello, this is a test message. You are not gonna tortured anymore by Assignments."

# Create an image with white background
img = Image.new('RGB', (800, 400), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Load a handwriting-like font
font = ImageFont.truetype("/Users/teru/Python Projects/Text to handwriting/JustAnotherHand-Regular.ttf", size=30)  # Replace with the path to a handwriting font

# Write text on the image
draw.text((50, 50), txt, fill=(0, 0, 255), font=font)

# Save the image
img.save("output.png")
print("END")