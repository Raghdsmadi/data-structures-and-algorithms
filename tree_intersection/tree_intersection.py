from hash_table.hash import HashTable
from trees.tree import *
# from tree_breadth_first.breadthFirst import *


def tree_intersection(tree1, tree2):
    """
         A function that accepts two binary trees and returns a list containing the values that are found in both trees.
         """
    ht = HashTable()
    for x in range(len(tree1)):
        if tree1[x] == tree2[x]:
            ht.set(str(tree1[x]), 1)
    return ht.key()


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = TNode(150)
    tree.root.left = TNode(6)
    tree.root.right = TNode(10)
    tree.root.left.left = TNode(90)
    tree.root.left.right = TNode(18)
    tree.root.right.left = TNode(17)
    tree.root.right.right = TNode(30)

    tree2 = BinaryTree()
    tree2.root = TNode(150)
    tree2.root.left = TNode(3)
    tree2.root.right = TNode(50)
    tree2.root.left.left = TNode(90)
    tree2.root.left.right = TNode(16)
    tree2.root.right.left = TNode(17)
    tree2.root.right.right = TNode(30)

    print(tree_intersection(tree.pre_order(), tree2.pre_order()))