class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        input: Value
        output: None
        It will create a node and assign it to the top.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        input: None
        output: Value of the node that poped
        It will remove the top from the stack and return the value of that      node, and       assgin new top
        """
        if not self.top:
            raise Exception("Pop from empty stack is not allowed")

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        """
        input stack
        output True if its empty otherwise return False
        """
        # if self.top is None :
        #   return True
        # else:
        #   return False
        return True if self.top is None else False

    def peek(self):
        '''
        input : nothing
        output : The value of the top if the stack is not empty,
        and an error if the stack is empty
        '''
        if self.is_empty() == False:
            return self.top.value
        else:
            raise Exception("peek from empty stack is not allowed")





def validate_brackets(item: str):
    stack = Stack()

    for brackets in item:
        if brackets == "{" or brackets == "[" or brackets == "(":
            stack.push(brackets)

        elif brackets == "}" or brackets == "]" or brackets == ")":
            if stack.peek() == "{" or stack.peek() == "[" or stack.peek() == "(":
                stack.pop()
            else:
                return False

    if stack.top:
        return False
    else:
        return True
