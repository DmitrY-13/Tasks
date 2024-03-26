from random import choice

from encoder.exceptions import EncoderInputDataError
from encoder.types import Size


class Encoder:
    @staticmethod
    def encode(data: str, table_size: Size):
        if len(data) > table_size.width * table_size.height:
            raise EncoderInputDataError('table cannot fit in data')

        result = ''
        data_last_index = len(data) - 1
        for x in range(table_size.width):
            for y in range(table_size.height):
                index = x + table_size.width * y
                result += data[index] if index <= data_last_index else choice(data)

        return result

    @staticmethod
    def decode(data: str, table_size: Size):
        if len(data) < table_size.width * table_size.height:
            raise EncoderInputDataError('less data than table suggests')

        result = ''
        for y in range(table_size.height):
            for x in range(table_size.width):
                index = y + table_size.height * x
                result += data[index]

        return result
