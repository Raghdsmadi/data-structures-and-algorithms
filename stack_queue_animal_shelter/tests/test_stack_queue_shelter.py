from stack_queue_animal_shelter.stack_queue_shelter import AnimalShelter,Cat,Dog
import pytest


def test_enqueue():
    shelter1 = AnimalShelter()
    shelter1.enqueue(Cat())
    assert shelter1.peek() == "cat"



def test_dequeue(shelter1):
    assert str(shelter1.dequeue("dog")) == "dog"


def test_dequeue_2(shelter1):
    assert str(shelter1.dequeue("dog")) == "dog"
    assert str(shelter1.dequeue("cat")) == "cat"



# def test_dequeue_error_2():
#     with pytest.raises(Exception):
#         AnimalShelter().dequeue()


@pytest.fixture
def shelter1():
    shelter = AnimalShelter()
    shelter.enqueue("Marsha", "cat")
    shelter.enqueue("rex", "dog")
    shelter.enqueue("Tuna", "cat")
    shelter.enqueue("melo", "dog")
    return shelter


