import pytest
from sorting.merge.merge import mergeSort

def test_merge_sort():
    assert [-3, 0, 1, 3, 6] == mergeSort([0, -3, 1, 3, 6])
