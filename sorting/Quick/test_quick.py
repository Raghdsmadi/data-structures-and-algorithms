from sorting.Quick.quick_sort import quick_sort


def test_quick_sort():
    assert [-5, 0, 1, 3, 6, 90] == quick_sort([3, 90, 6, -5, 0, 1], 0, 5)
