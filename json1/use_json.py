#!/usr/bin/env python3
""" Use JSON config """

import argparse
import json


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Use JSON config',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='JSON file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='config.json')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    config = json.load(args.file)
    print(config)


# --------------------------------------------------
if __name__ == '__main__':
    main()
