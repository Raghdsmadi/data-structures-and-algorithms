from stack_queue_pseudo.stack_que_pseudo import Stack,Queue,PseudoQueue
import pytest
def test_enqueue():
    pseudoQ = PseudoQueue()
    [pseudoQ.enqueue(i) for i in ["Marsha", "Tuna", "Rafaello"]]
    assert pseudoQ.dequeue() == "Marsha"

def test_dequeue(my_pseudo_queue):
    assert my_pseudo_queue.dequeue() == "Marsha"



@pytest.fixture
def my_pseudo_queue():
    q = PseudoQueue()
    [q.enqueue(i) for i in ["Marsha", "Tuna", "Rafaello"]]
    return q