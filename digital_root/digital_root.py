from typing import Final

DIVIDER: Final = 10


def find_digital_root(number: int) -> int:
    root = 0

    while number > 0:
        root += number % DIVIDER
        number //= DIVIDER

    if root > DIVIDER:
        root = find_digital_root(root)

    return root
