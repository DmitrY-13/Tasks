from random import randint

import pytest


@pytest.fixture
def unsorted_list():
    return [randint(0, 100) for _ in range(100)]


@pytest.fixture
def sorted_list(unsorted_list):
    return sorted(unsorted_list)
