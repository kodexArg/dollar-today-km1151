from PIL import Image, ImageDraw, ImageFont

# Ask for numeric value
price_usd = input("Enter a numeric value: ")

# Open background image and get its dimensions
background = Image.open("background/background.jpg")
width, height = background.size

# Create a new image with the same dimensions and mode as the background image
image = Image.new(background.mode, (width, height))

# Paste the background image onto the new image
image.paste(background, (0, 0))

# Load the Arial font with size 48
font = ImageFont.truetype("arial.ttf", 512)

# Create a new ImageDraw object
draw = ImageDraw.Draw(image)

# Get the dimensions of the text
text_width, text_height = draw.textsize(price_usd, font=font)

# Calculate the position to draw the text
x = (width - text_width) / 2
y = (height - text_height) / 2

# Draw the text onto the image
draw.text((x, y), price_usd, font=font, fill=(255, 255, 255))

# Save the image
image.save("output.png")
