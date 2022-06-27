class Node:
    def __init__(self,value):
        self.value=value
        self.next=None



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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """It will add a new node to the end of the queue """
        node = Node(value)

        if not self.front:
            self.rear = node
            self.front = node

        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        temp = self.front
        self.front = self.front.next
        temp.next = None

    def is_empty(self):
        return self.front == None


class PseudoQueue:

    def __init__(self):
        '''function creates queue with 2 stacks'''
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = self.stack1.top
        self.rear = self.stack2.top

    def enqueue(self, value):
        '''enqueue that push the value to the first stack'''
        node = Node(value)
        node.next = self.front
        self.front = node
        self.stack1.push(node)

    def dequeue(self):
        ''' dequeue that pop the value from the second stack'''
        while self.stack1.top:
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop().value
