"""
File: stanCodoshop.py
Name: Jo-Di(Frank), Chiang
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------

TODO:

"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values
    """
    dist = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]
    """
    rgb = []
    # Count the total of RGB in pixels
    total_red = []
    total_green = []
    total_blue = []
    for pixel in pixels:
        total_red.append(pixel.red)
        total_blue.append(pixel.blue)
        total_green.append(pixel.green)
    # Make sure the avg will be int, using //.
    avg_red = sum(total_red) // len(total_red)
    avg_green = sum(total_green) // len(total_red)
    ave_blue = sum(total_blue) // len(total_red)
    #   Adding avg of RGB in rgb list
    rgb.append(avg_red)
    rgb.append(avg_green)
    rgb.append(ave_blue)
    return rgb  # The average rgb value will be store as [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    rgb_average = get_average(pixels)
    best_pixel = pixels[0]
    minimum_dist = float('inf')
    for pixel in pixels:
        color_dist = get_pixel_dist(pixel, rgb_average[0], rgb_average[1], rgb_average[2])
        if color_dist < minimum_dist:
            minimum_dist = color_dist
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            total_rgb = []
            for image in images:
                pixel_rgb = image.get_pixel(x, y)
                total_rgb.append(pixel_rgb)
            image_best_pixel = get_best_pixel(total_rgb)
            # Choose the best pixel in all image
            final_result = result.get_pixel(x, y)
            final_result.red = image_best_pixel.red
            final_result.green = image_best_pixel.green
            final_result.blue = image_best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
