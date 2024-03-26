from random import choice

from binary_search import search


class Test:
    def test_searching_existent_value(self, sorted_unique_int_list):
        target_value = choice(sorted_unique_int_list)
        result_index = search(target_value, sorted_unique_int_list)
        assert sorted_unique_int_list[result_index] == target_value

    def test_searching_non_existent_value(self, sorted_unique_int_list):
        target_value = sorted_unique_int_list[-1] + 1
        result_index = search(target_value, sorted_unique_int_list)
        assert result_index is None
