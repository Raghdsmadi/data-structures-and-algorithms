import pytest
from graph_breadth_first.graph_breadth import *

def test_exists():
    assert Graph
def test_breadth_first_1():
    graph = Graph()
    test1 = graph.add_node("test")
    assert graph.breadth_first(test1) == ["test"]


def test_breadth_first_2():
    graph = Graph()
    test1 = graph.add_node("test1")
    test2 = graph.add_node("test2")
    graph.add_edge(test1, test2)
    assert graph.breadth_first(test1) == ["test1", "test2"]


def test_breadth_first_3():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(a, e)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)
    assert g.breadth_first(a) == ['A', 'B', 'E', 'C', 'D']