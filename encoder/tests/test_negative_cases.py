from encoder import Encoder
from encoder.exceptions import EncoderInputDataError
from encoder.types import Size


class TestNegativeCases:
    def test_encoding_with_too_small_table_size(self):
        try:
            Encoder.encode('12', Size(1, 1))
        except Exception as exc:
            assert isinstance(exc, EncoderInputDataError)
            assert str(exc) == 'table cannot fit in data'

    def test_decoding_with_too_short_data(self):
        try:
            Encoder.decode('1', Size(1, 2))
        except Exception as exc:
            assert isinstance(exc, EncoderInputDataError)
            assert str(exc) == 'less data than table suggests'
