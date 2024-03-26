from quick_sort import sort


def test(unsorted_list, sorted_list):
    assert sort(unsorted_list) == sorted_list
