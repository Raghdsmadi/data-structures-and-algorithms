class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None
class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        if not isinstance(value, Node):
            value = Node(value)

        if self.is_empty():
            self.front, self.back = value, value
        else:
            self.back.pointer = value
            self.back = value

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.front.value == self.back.value:
            value = self.front.value
            self.front, self.back = None, None
            return value

        temp = self.front
        self.front = self.front.pointer
        temp.pointer = None
        return temp.value

    def is_empty(self):
        return self.front is None and self.back is None
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

def breadth_first(tree):
    """
          traverse the tree in a breadth-first manner
          """

    if not tree.root:
        raise (Exception("Tree is empty !"))

    output = []
    q = Queue()
    q.enqueue(tree.root)

    while not q.is_empty():
        front = q.dequeue()
        output.append(front.value)

        if front.left:
            q.enqueue(front.left)

        if front.right:
            q.enqueue(front.right)

    return output








if __name__ == "__main__":
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
    # print(tree.max_value())