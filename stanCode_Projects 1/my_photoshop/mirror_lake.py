"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: Str, the original path of image file.
    :return: The reflected image.
    """
    # Giving blank img with double size of the height
    blank_img = SimpleImage.blank(filename.width, filename.height * 2)
    for x in range(filename.width):
        for y in range(filename.height):
            # colored pixel
            original_mt_pixel = filename.get_pixel(x, y)
            # reflected
            blank_part1 = blank_img.get_pixel(x, y)
            blank_part2 = blank_img.get_pixel(x, blank_img.height-1-y)

            blank_part1.red = original_mt_pixel.red
            blank_part1.blue = original_mt_pixel.blue
            blank_part1.green = original_mt_pixel.green

            blank_part2.red = original_mt_pixel.red
            blank_part2.blue = original_mt_pixel.blue
            blank_part2.green = original_mt_pixel.green
    return blank_img


def main():
    """
    This program will reflect the mt-rainier
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    blank_img = reflect(original_mt)
    blank_img.show()


if __name__ == '__main__':
    main()
