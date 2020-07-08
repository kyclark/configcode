import algorithm_rgb
import os
import gdal
import numpy as np
import json

input1 = './test_input/rgb_1_2_E.tif'
input2 = './test_input/rgb_40_11_W.tif'
meta = './meta.json'


# --------------------------------------------------
def test_calculate1():
    """Test calculate"""

    run(input1, [
        14.0, 0.02, 16.16, -1.53, 56.53, -42.53, 30.16, 12.81, 1.02, -0.02,
        0.34
    ])


# --------------------------------------------------
def test_calculate2():
    """Test calculate"""

    run(input2, [
        88.27, 0.18, -14.96, 18.33, -1.44, 89.71, 73.31, 24.98, 1.4, 0.14, 0.42
    ])


# --------------------------------------------------
def run(file, expected):
    """Run calculate on a file"""

    assert os.path.isfile(file)

    if fh := gdal.Open(file):
        pix = np.array(fh.ReadAsArray())
        assert algorithm_rgb.calculate(np.rollaxis(pix, 0, 3)) == expected


# --------------------------------------------------
def test_meta():
    """Test meta"""

    assert os.path.isfile(meta)
    data = json.load(open(meta))
    assert data['authors']
