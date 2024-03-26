import logging
from typing import Sequence, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar('T')


def search(target_value: T, collection: Sequence[T]) -> int | None:
    logger.info('searching for value')
    logger.debug(f'searching for {target_value=} in {collection=}')
    left_border = 0
    right_border = len(collection) - 1

    while left_border <= right_border:
        center_index = (right_border + left_border) // 2
        logger.debug(f'{left_border=}, {center_index=}, {right_border=}')
        center_value = collection[center_index]

        if target_value == center_value:
            logger.debug(f'{target_value=} == {center_value=}')
            logger.info('value found')
            return center_index

        if target_value < center_value:
            logger.debug(f'{target_value=} < {center_value=}')
            right_border = center_index - 1
        else:
            logger.debug(f'{target_value=} > {center_value=}')
            left_border = center_index + 1

    logger.debug(f'{left_border} > {right_border}')
    logger.info('value not found')
    return None
