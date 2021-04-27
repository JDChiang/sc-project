"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage, the shrunk image
    """
    new_image = SimpleImage.blank(filename.width // 2, filename.height // 2)
    for x in range(new_image.width):
        for y in range(new_image.height):
            old_pixel = filename.get_pixel(2 * x, 2 * y)
            new_pixel = new_image.get_pixel(x, y)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
    return new_image


def main():
    """
    This program will shrink the size of the image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink(original)
    after_shrink.show()


if __name__ == '__main__':
    main()
