class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return self.value


class LinkedList:


    def __init__(self):
        pass


    def __init__(self):
        self.head = None


    def Insert(self, value):

        if value is None:
            raise Exception("The provided values must not be (None) !")

        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            self.head = value
        else:
            value.next = self.head
            self.head = value

    def Includes(self, value):

        if value is None:
            raise Exception("The provided value must not be (None) !")

        if not isinstance(value, Node):
            value = Node(value)

        if self.head is None:
            return False

        else:
            current = self.head
            while current.next is not None:
                if value.value == current.value:
                    return True
                current = current.next
            else:
                if value.value == current.value:
                    return True

            return False

    def __str__(self):
        return self.ToString()

    def ToString(self):

        output = ""
        if self.head is None:
            output = "None"
        else:
            current = self.head
            while current is not None:
                output += f"{current.value} -> "
                current = current.next
            output += "NULL"

        return output

