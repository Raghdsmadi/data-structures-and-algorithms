from tree_breadth_first.breadthFirst import BinaryTree,TNode,breadth_first
import pytest


def test_breadth_first(myBinaryTree):
    assert breadth_first(myBinaryTree) == [23, 8, 42, 4, 16, 27, 85, 15, 22, 105]


def test_breadth_first():
    with pytest.raises(Exception):
        tree = BinaryTree()
        breadth_first(tree)


@pytest.fixture
def myBinaryTree():
    tree = BinaryTree()
    tree.root = TNode(23)
    tree.root.left, tree.root.right = TNode(8), TNode(42)

    tree.root.left.left, tree.root.left.right = TNode(4), TNode(16)
    tree.root.left.right.left, tree.root.left.right.right = TNode(15), TNode(22)

    tree.root.right.left, tree.root.right.right = TNode(27), TNode(85)
    tree.root.right.right.right = TNode(105)

    return tree