"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: str, the file path of the original image
    :return new_img: The image with blurred processed.
    """
    blurred = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            r_total = 0
            g_total = 0
            b_total = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r_total += pixel.red
                            g_total += pixel.green
                            b_total += pixel.blue
                            count += 1
            # To get new blurred pixel
            new_pixel = blurred.get_pixel(x, y)
            # Giving the new color
            new_pixel.red = r_total / count
            new_pixel.green = g_total / count
            new_pixel.blue = b_total / count
    return blurred


def main():
    """
    This program will process the image with blurry effect.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()








if __name__ == '__main__':
    main()
