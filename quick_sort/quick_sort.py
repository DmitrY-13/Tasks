from copy import deepcopy
from random import randint
from typing import TypeVar, MutableSequence

T = TypeVar('T')


def sort(collection: MutableSequence[T]):
    left_border = 0
    right_border = len(collection) - 1
    collection_copy = deepcopy(collection)

    _sort(collection_copy, left_border, right_border)

    return collection_copy


def _sort(collection: MutableSequence[T], left_border: int, right_border: int):
    if left_border >= right_border:
        return

    left_pointer = left_border
    right_pointer = right_border
    pivot = collection[randint(left_border, right_border)]

    while left_pointer <= right_pointer:
        while collection[left_pointer] < pivot:
            left_pointer += 1
        while collection[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer <= right_pointer:
            collection[left_pointer], collection[right_pointer] = collection[right_pointer], collection[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    _sort(collection, left_border, right_pointer)
    _sort(collection, left_pointer, right_border)
