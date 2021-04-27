"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage

THRESHOLD = 1.3


def combine(background_img, figure_img):
    """
    :param background_img: str, the file path of background.
    :param figure_img: str, the file path of figure.
    :return: figure_img
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            # Find the pixel.
            pixel_figure = figure_img.get_pixel(x, y)
            avg = (pixel_figure.red + pixel_figure.green + pixel_figure.blue) // 3
            if pixel_figure.green > avg * THRESHOLD:
                pixel_background_img = background_img.get_pixel(x, y)
                pixel_figure.red = pixel_background_img.red
                pixel_figure.blue = pixel_background_img.blue
                pixel_figure.green = pixel_background_img.green
    return figure_img


def main():
    """
    This algorithm helps us combine two image (figure + background)
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.make_as_big_as(figure)
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
