from random import getrandbits

import pytest


@pytest.fixture
def sorted_unique_int_list():
    result = []
    number = 0
    while len(result) < 100:
        if getrandbits(1):
            result.append(number)
        number += 1
    return result
