import pytest
from link_list.linked_list import Node,LinkedList

def test_node(node):
    assert node


def test_the_value(node):
    assert node.value == 6


def test_the_next(node):
    assert node.next == None


def test_linked_list(ll):
    assert ll


def test_head_value(ll):
    actual = ll.head.value
    expected = 5

    assert actual == expected


def test_the_second_node(ll):
    actual = ll.head.next.value
    expected = 10

    assert actual == expected


def test_str(ll):
    actual = ll.__str__()

    expected = '< 5 > --> < 10 > --> < 15 > --> Null'


    assert actual == expected

def test_insert():
    ll1 = LinkedList()
    ll1.insert(8)
    actual = ll1.head.value
    expected = 8
    assert actual == expected

def test_includes_true(LL):
    # actual = LL.head.value
    # expected = True
    # assert actual == expected
    assert LL.includes(7) == True

def test_includes_false(LL):
    assert LL.includes(13) == False

def test_insert_before(LL):
    current = LL.head
    while current:
        if current.next.value == 7:
            actual = current.value
            break

        current = current.next
    # actual = LL.head.value
    expected = 9
    assert actual == expected


def test_insert_after(LL):
    current = LL.head
    while current:
        if current.value == 3:
            actual =current.next.value
            break

        current = current.next
    # actual = LL.head.value
    expected = 14
    assert actual == expected



@pytest.fixture
def node():
    nod = Node(6)
    return nod


@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    return ll

@pytest.fixture
def LL():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(3)
    LL.insert(5)
    LL.insert(7)
    print(LL)
   # LL.includes(5)
    LL.insertBefore(7,9)
    LL.insertAfter(3,14)
    return LL