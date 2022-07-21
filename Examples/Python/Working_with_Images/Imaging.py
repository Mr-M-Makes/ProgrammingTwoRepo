from PIL import Image, ImageEnhance

def main():
    im1 = Image.open("Examples\Python\Working_with_Images\diwali-1179941.jpg")
    color_enhancer = ImageEnhance.Color(im1)
    new_image = color_enhancer.enhance(.5)
    Image._show(new_image)

main()