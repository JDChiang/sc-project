"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05

def highlight_fires(filename):
    """
    :param filename: str, the file path of greenland fire.
    :return: the highlighted img
    """
    highlighted = SimpleImage(filename)
    for pixel in highlighted:
        # Calculate the avg
        avg = (pixel.red + pixel.blue + pixel.green)//3
        # determine the on-fire region
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        elif pixel.red < avg * HURDLE_FACTOR:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return highlighted


def main():
    """
    TODO:
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
