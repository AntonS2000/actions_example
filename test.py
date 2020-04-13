from assertpy import *

import main


def test_sum():
    assert_that(main.sum(2, 2)).is_equal_to(4)
