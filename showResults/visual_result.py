from PIL import Image
from PIL import Image, ImageDraw
# Open the original image
image_path = "./v1_ffn1.5_img15_1.png"  # Replace with the path to your image file
original_image = Image.open(image_path)

# Define the coordinates of the cropped region
left = 316   # Top-left x-coordinate of the cropped region
top = 319     # Top-left y-coordinate of the cropped region
right = 391  # Bottom-right x-coordinate of the cropped region
bottom = 394 # Bottom-right y-coordinate of the cropped region
# Crop the image
cropped_image = original_image.crop((left, top, right, bottom))
cropped_image = cropped_image.resize((300, 300))
# Get the dimensions of the original image
original_width, original_height = original_image.size

# Get the dimensions of the cropped image
cropped_width, cropped_height = cropped_image.size

# Create a new image with the size of the original image
result_image = Image.new('RGB', (original_width, original_height))

# Paste the original image onto the new image
result_image.paste(original_image, (0, 0))

# Paste the cropped image onto the new image at the bottom-right corner
result_image.paste(cropped_image, (original_width - cropped_width, original_height - cropped_height))
# Draw a red frame line around the cropped image
draw = ImageDraw.Draw(result_image)
frame_color = (255, 0, 0)  # Red color
frame_thickness = 3
frame_coordinates = [(original_image.width - 300 - frame_thickness, original_image.height - 300 - frame_thickness),
                     (original_image.width - 300 + 300 + frame_thickness, original_image.height - 300 - frame_thickness),
                     (original_image.width - 300 + 300 + frame_thickness, original_image.height - 300+ 300 + frame_thickness),
                     (original_image.width - 300 - frame_thickness, original_image.height -300 + 300 + frame_thickness)]
draw.polygon(frame_coordinates, outline=frame_color, width=frame_thickness)

# Save and show the result image
result_image.save("v1_ffn1.5_img15_1_crop.jpg")
result_image.show()