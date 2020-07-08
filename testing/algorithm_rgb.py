"""
Greenness Transformer
"""

import numpy as np


def excess_greenness_index(pxarray: np.ndarray) -> float:
    """
    Minimizes variation between different illuminations and enhances detection
    of plants
    """
    red, green, blue = get_red_green_blue_averages(pxarray)

    return round(2 * green - (red + blue), 2)


def green_leaf_index(pxarray: np.ndarray) -> float:
    """
    Calculates the green leaf index of an image
    """
    red, green, blue = get_red_green_blue_averages(pxarray)

    return round((2 * green - red - blue) / (2 * green + red + blue), 2)


def cive(pxarray: np.ndarray) -> float:
    """
    Can measure crop growth status
    """
    red, green, blue = get_red_green_blue_averages(pxarray)

    return round(0.441 * red - 0.811 * green + 0.385 * blue + 18.78745, 2)


def normalized_difference_index(pxarray: np.ndarray) -> float:
    """
    Calculates the normalized difference index of an image
    """
    red, green, _ = get_red_green_blue_averages(pxarray)

    return round(128 * ((green - red) / (green + red)) + 1, 2)


def excess_red(pxarray: np.ndarray) -> float:
    """
    Finds potential illumination issues that make it difficult to
    tease apart redness from crops/leaves from soil or camera
    artifacts
    """
    red, green, _ = get_red_green_blue_averages(pxarray)

    return round(1.3 * red - green, 2)


def exgr(pxarray: np.ndarray) -> float:
    """
    Minimizes the variation between different illuminations
    """

    return round(excess_greenness_index(pxarray) - excess_red(pxarray), 2)


def combined_indices_1(pxarray: np.ndarray) -> float:
    """
    Combined indices calculation 1
    """

    return round(excess_greenness_index(pxarray) + cive(pxarray), 2)


def combined_indices_2(pxarray: np.ndarray) -> float:
    """
    Combined indices calculation 2
    """

    return round(
        0.36 * excess_greenness_index(pxarray) + 0.47 * cive(pxarray) +
        0.17 * vegetative_index(pxarray), 2)


def vegetative_index(pxarray: np.ndarray) -> float:
    """
    Minimize illumination differences between images
    """
    red, green, blue = get_red_green_blue_averages(pxarray)

    return round(green / ((red**0.667) * (blue**.333)), 2)


def ngrdi(pxarray: np.ndarray) -> float:
    """
    Can measure crop growth status
    """
    red, green, _ = get_red_green_blue_averages(pxarray)

    return round((green - red) / (green + red), 2)


def percent_green(pxarray: np.ndarray) -> float:
    """
    Returns the percentage of an image that is green, which can be used
    to identify plant cover
    """
    # redness value
    red = np.sum(pxarray[:, :, 0])

    # greenness value
    green = np.sum(pxarray[:, :, 1])

    # blueness value
    blue = np.sum(pxarray[:, :, 2])

    return round(green / (red + green + blue), 2)


def get_red_green_blue_averages(pxarray: np.ndarray) -> tuple:
    """
    Returns the average red, green, and blue values in a pxarray object
    """
    # redness value
    red = np.average(pxarray[:, :, 0])

    # greenness value
    green = np.average(pxarray[:, :, 1])

    # blueness value
    blue = np.average(pxarray[:, :, 2])

    return (red, green, blue)


def calculate(pxarray: np.ndarray) -> list:
    """Calculates one or more values from plot-level RGB data
    Arguments:
        pxarray: Array of RGB data for a single plot
    Return:
        Returns a list of the calculated values from the
    """

    return [
        excess_greenness_index(pxarray),
        green_leaf_index(pxarray),
        cive(pxarray),
        normalized_difference_index(pxarray),
        excess_red(pxarray),
        exgr(pxarray),
        combined_indices_1(pxarray),
        combined_indices_2(pxarray),
        vegetative_index(pxarray),
        ngrdi(pxarray),
        percent_green(pxarray)
    ]
