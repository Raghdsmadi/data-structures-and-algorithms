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

    def max_value(self):
        if not self.root:
            return self.root

        def _walk(root):
            if root == None:
                return False
            max_val = root.value
            left_max = _walk(root.left)
            right_max = _walk(root.right)

            if left_max > max_val:
                max_val = left_max
            if right_max > max_val:
                max_val = right_max
            return max_val

        return _walk(self.root)




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
    print(tree.max_value())
