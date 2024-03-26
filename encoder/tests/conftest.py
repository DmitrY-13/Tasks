from math import ceil
from random import randint

import pytest

from encoder.types import Size


def random_ascii():
    return chr(randint(32, 126))


@pytest.fixture
def data():
    return ''.join(random_ascii() for _ in range(100))


@pytest.fixture
def table_size(data):
    data_length = len(data)
    width = randint(2, data_length - 1)
    height = ceil(data_length / width)
    return Size(width, height)
