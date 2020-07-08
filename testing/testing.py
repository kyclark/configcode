#!/usr/bin/env python3
"""
Test algorithm_rgb
"""

import algorithm_rgb
import argparse
import gdal
import numpy as np
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Test algorithm',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        fh.close()
        run_test(fh.name)


# --------------------------------------------------
def run_test(filename):
    """Runs the extractor code using pixels from the file
    Args:
        filename(str): Path to image file
    Return:
        The result of calling the extractor's calculate() method
    Notes:
        Assumes the path passed in is valid. An error is reported if
        the file is not an image file.
    """
    try:
        with gdal.Open(filename) as fh:
            # Get the pixels and call the calculation
            pix = np.array(open_file.ReadAsArray())
            calc_val = algorithm_rgb.calculate(np.rollaxis(pix, 0, 3))

            # Check for unsupported types
            if isinstance(calc_val, set):
                raise RuntimeError(
                    "A 'set' type of data was returned and isn't supported. "
                    "Please use a list or a tuple instead"
                )

            # Perform any type conversions to a printable string
            if isinstance(calc_val, str):
                print_val = calc_val
            else:
                # Check if the return is iterable and 
                # comma separate the values if it is
                try:
                    _ = iter(calc_val)
                    print_val = ",".join(map(str, calc_val))
                except Exception:
                    print_val = str(calc_val)

            print(filename + "," + print_val)
    except Exception as ex:
        sys.stderr.write("Exception caught: " + str(ex) + "\n")
        sys.stderr.write("    File: " + filename + "\n")


# --------------------------------------------------
if __name__ == '__main__':
    main()
