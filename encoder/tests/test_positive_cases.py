from encoder import Encoder


def test_encoding_and_decoding(data, table_size):
    encoded_data = Encoder.encode(data, table_size)
    decoded_data = Encoder.decode(encoded_data, table_size)

    assert decoded_data[:len(data):] == data
