import pytest
from linked_list.linked_list import Node,LinkedList

def test_empty_list_instatiation():
    assert LinkedList().head is None


def test_inserting_into_linked_list(my_linked_list):
    my_linked_list.Insert(Node("Marsha"))
    assert str(my_linked_list) == "Marsha -> Tuna -> Rafaello -> Hero -> NULL"


def test_head_next_towards_first_node(my_linked_list):
    assert my_linked_list.head.value == Node("Tuna").value

def test_inserting_multiple_nodes(my_linked_list):
    [my_linked_list.Insert(Node(i)) for i in ["Marsha", "Meow", "cmcm"]]
    assert str(my_linked_list) == "cmcm -> Meow -> Marsha -> Tuna -> Rafaello -> Hero -> NULL"


def test_serching_for_existed_node(my_linked_list):
    assert my_linked_list.Includes("Tuna") == True


def test_serching_for_not_existed_node(my_linked_list):
    assert my_linked_list.Includes("mohsen") == False