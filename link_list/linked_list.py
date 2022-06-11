class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return self.value


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        """
    It will add a node to the end of the linked list

    parameters : Value
    return: Nothing
    """
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def insert(self, value):

        if value is None:
            raise Exception("The provided values must not be (None) !")

        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
            value.next = self.head
            self.head = value

    def includes(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        return self.ToString()

    def ToString(self):

        current = self.head
        items = ''
        while current:
            items += f"< {current.value} > --> "
            current = current.next
        items += "Null"
        return items

