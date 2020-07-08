import algorithm_rgb as al
import os
import osgeo.gdal as gdal
import numpy as np
import json

input1 = './test_input/rgb_1_2_E.tif'
input2 = './test_input/rgb_40_11_W.tif'
meta = './meta.json'


# --------------------------------------------------
def test_input_files():
    """Test input files exist"""

    assert os.path.isfile(input1)
    assert os.path.isfile(input2)


# --------------------------------------------------
def test_get_red_green_blue_averages():
    """Test get_red_green_blue_averages"""

    assert al.get_red_green_blue_averages(
        read_input(input1)) == (166.8537142857143, 160.37885714285713,
                                139.89971428571428)

    assert al.get_red_green_blue_averages(
        read_input(input2)) == (109.85485714285714, 144.25085714285714, 90.381)


# --------------------------------------------------
def test_excess_greenness_index():
    """Test excess_greenness_index"""

    assert al.excess_greenness_index(read_input(input1)) == 14.0
    assert al.excess_greenness_index(read_input(input2)) == 88.27


# --------------------------------------------------
def test_green_leaf_index():
    """Test green_leaf_index"""

    assert al.green_leaf_index(read_input(input1)) == 0.02
    assert al.green_leaf_index(read_input(input2)) == 0.18


# --------------------------------------------------
def test_cive():
    """Test cive"""

    assert al.cive(read_input(input1)) == 16.16
    assert al.cive(read_input(input2)) == -14.96


# --------------------------------------------------
def test_normalized_difference_index():
    """Test normalized_difference_index"""

    assert al.normalized_difference_index(read_input(input1)) == -1.53
    assert al.normalized_difference_index(read_input(input2)) == 18.33


# --------------------------------------------------
def test_excess_red():
    """Test excess_red"""

    assert al.excess_red(read_input(input1)) == 56.53
    assert al.excess_red(read_input(input2)) == -1.44


# --------------------------------------------------
def test_exgr():
    """Test exgr"""

    assert al.exgr(read_input(input1)) == -42.53
    assert al.exgr(read_input(input2)) == 89.71


# --------------------------------------------------
def test_combined_indices_1():
    """Test combined_indices_1"""

    assert al.combined_indices_1(read_input(input1)) == 30.16
    assert al.combined_indices_1(read_input(input2)) == 73.31


# --------------------------------------------------
def test_combined_indices_2():
    """Test combined_indices_2"""

    assert al.combined_indices_2(read_input(input1)) == 12.81
    assert al.combined_indices_2(read_input(input2)) == 24.98


# --------------------------------------------------
def test_vegetative_index():
    """Test vegetative_index"""

    assert al.vegetative_index(read_input(input1)) == 1.02
    assert al.vegetative_index(read_input(input2)) == 1.4


# --------------------------------------------------
def test_ngrdi():
    """Test ngrdi"""

    assert al.ngrdi(read_input(input1)) == -0.02
    assert al.ngrdi(read_input(input2)) == 0.14


# --------------------------------------------------
def test_percent_green():
    """Test percent_green"""

    assert al.percent_green(read_input(input1)) == 0.34
    assert al.percent_green(read_input(input2)) == 0.42


# --------------------------------------------------
def test_calculate():
    """Test calculate"""

    assert al.calculate(read_input(input1)) == [
        14.0, 0.02, 16.16, -1.53, 56.53, -42.53, 30.16, 12.81, 1.02, -0.02,
        0.34
    ]

    assert al.calculate(read_input(input2)) == [
        88.27, 0.18, -14.96, 18.33, -1.44, 89.71, 73.31, 24.98, 1.4, 0.14, 0.42
    ]


# --------------------------------------------------
def read_input(file) -> np.ndarray:
    """Run calculate on a file"""
    if fh := gdal.Open(file):
        pix = np.array(fh.ReadAsArray())
        return np.rollaxis(pix, 0, 3)


# --------------------------------------------------
def test_meta():
    """Test meta"""

    assert os.path.isfile(meta)
    data = json.load(open(meta))
    assert data['authors']
