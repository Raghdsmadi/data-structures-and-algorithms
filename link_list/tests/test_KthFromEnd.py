import pytest
from link_list.linked_list import LinkedList

def test_k_greater_than_the_linked_list(ll):
    actual = ll.kthFromEnd(6)
    expected = "Invalid Error!!"
    assert actual == expected


def test_the_linked_list_is_one(ll):
    actual = ll.kthFromEnd(0)
    expected = 1
    assert actual == expected


def test_k_is_negative(ll):
    actual = ll.kthFromEnd(-4)
    expected = "Please Enter a Positive Number!"
    assert actual == expected


def test_k_and_ll_are_same(ll):
    actual = ll.kthFromEnd(0)
    expected = 1
    assert actual == expected



@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
   # LL.includes(5)
   #  ll.insertBefore(7,9)
   #  ll.insertAfter(3,14)
    return ll