import pytest
from stack_queue.stack_and_queue import Stack,Queue


def test_push(stack):
    actual = stack.top.value
    expected = 8
    assert actual == expected


def test_pop(stack):
    actual = stack.pop()
    expected = 8
    assert actual == expected


def test_peek_of_stack(stack):
    actual = stack.peek()
    expected = 8
    assert actual == expected


def test_is_empty_stack():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected


# decorator
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(6)
    stack.push(7)
    stack.push(8)

    return stack


def test_enqueue(queue):
    actual = queue.rear.value
    expected = "3"
    assert actual == expected


def test_dequeue(queue):
    queue.dequeue()
    actual = queue.front.value
    expected = "2"
    assert actual == expected


def test_is_empty_queue(queue):
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected


def test_peek_of_queue(queue):
    actual = queue.peek()
    expected = "1"
    assert actual == expected


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")

    return queue
