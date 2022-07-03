class Node :
    def __init__(self,value):
        self.value= value
        self.next=None



class Stack:
    def __init__(self):
        self.top=None


    def push (self,value):
        """
          Takes the vlaue and make a node and append it to the top of the stack
          """
        node=Node(value)
        node.next=self.top
        self.top=node



    def pop (self):
        """
           a method to pop the top value of the stack
           input: no input
           output:
           the value popped from the stack
           """
        if self.isempty():
            raise Exception("stack is empty")

        temp=self.top
        self.top=self.top.next
        temp.next=None

        return temp.value


    def isempty(self):
        if self.top is None:
            return True
        return False
class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            result.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return result

    def in_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):

            if root.left:
                _walk(root.left)

            result.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return result

    def post_order(self):
        if not self.root:
            return self.root
        result = []

        def _walk(root):
            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

            result.append(root.value)

        _walk(self.root)
        return result

class Binary_Search_Tree(BinaryTree):

    def add(self, val):
        if not self.root:
            self.root = TNode(val)

        def _walk(root):
            if val < root.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = TNode(val)
            elif val > root.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = TNode(val)

        _walk(self.root)

    def contains(self, value):
        """
        input: value
        doing: check if the value is in the tree at least once
        output: boolean
        """

        current = self.root

        while True:
            if current.value == value:
                return True

            if current.left and value < current.value:
                current = current.left
            elif current.right and value > current.value:
                current = current.right
            else:
                break

        return False






if __name__ == "__main__":
    # node1 = TNode(7)
    # node2 = TNode(6)
    # node3 = TNode(5)
    # node4 = TNode(4)
    # node1.left = node2
    # node1.right = node3
    # node3.right = node4
    # tree = BinaryTree()
    # tree.root = TNode(10)
    # tree.root.left = TNode(20)
    # tree.root.right = TNode(50)
    # tree.root.left.left = TNode(30)
    # tree.root.left.right = TNode(40)
    # tree.root.right.left = TNode(60)

    # tree = BinaryTree()
    # tree.root = node1
    tree = BinaryTree()
    tree.root = TNode(1)
    tree.root.left = TNode(2)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(4)
    tree.root.left.right = TNode(5)
    tree.root.right.left = TNode(6)
    print(" pre order ")
    print(tree.pre_order())
    print("in order")
    print(tree.in_order())
    print("post order ")
    print(tree.post_order())

    bst = Binary_Search_Tree()
    bst.add(10)
    bst.add(20)
    bst.add(30)
    bst.add(40)
    print(bst.pre_order())


    # tree.pre_order_itiration()
    # tree.in_order_iteration()

    #
    # bst.root = node1
    #
    # tree.pre_order_iteration()
    # print(tree.root)
    # print(bst.root)











