from tree_max.treemax import TNode,BinaryTree


def test_Maximum_Number():
    node1 = TNode(2)
    node2 = TNode(7)
    node3 = TNode(2)
    node4 = TNode(6)
    node5 = TNode(5)
    node6 = TNode(11)
    node7 = TNode(9)
    node8 = TNode(4)
    node9 = TNode(5)
    node1.left = node2
    node1.right = node5
    node2.left = node3
    node2.right = node4
    node5.right = node7
    node4.left = node9
    node4.right = node6
    node7.left = node8
    tree = BinaryTree()
    tree.root = node1
    tree.pre_order()
    actual = tree.max_value()
    expected = 11
    assert actual == expected