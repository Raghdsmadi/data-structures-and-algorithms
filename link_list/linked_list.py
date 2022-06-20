class Node:
    """
    It will store the data and the reference to next node
    """
    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return self.value


class LinkedList:
    """
     It will have a sequence of nodes
     """
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
        """
              inserting the node at the beginning of the linked list
              """
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

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

    def insertBefore(self, value, new_value):
        """
        adds a new node with the new value before the first node
        """

        if self.includes(value):
            current = self.head
            if current.value == value:
                newNode = Node(new_value)
                newNode.next = current
                self.head = newNode
            else:
                while current.next:
                    if current.next.value == value:
                        newNode = Node(new_value)
                        newNode.next = current.next
                        current.next = newNode
                        break
                    current = current.next
        else:
            return ("err")

    def insertAfter(self, value, new_value):
        """
        adds a new node with the  new value  after the first node
        """

        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    newNode2 = Node(new_value)
                    newNode2.next = current.next
                    current.next = newNode2
                    return
                elif current.next == None:
                    newNode2 = Node(new_value)
                    current.next = newNode2
                current = current.next
        # else: return ("err")

    def kthFromEnd(self, k):
        current = self.head
        if k < 0:
            return 'Please Enter a Positive Number!'
        count = 0
        while current.next:
            count += 1
            current = current.next
        if count + 1 == k:
            return 'the kth value is equal to the length of list'
        if count < k:
            return 'Invalid Error!!'
        pos = count - k
        current = self.head
        for x in range(pos):
            current = current.next
        return current.value





if __name__ == '__main__':
    ll = LinkedList()
    # ll.append(5)
    # ll.append(10)
    # ll.insert(15)
    # print(ll.includes(5))
    # print(ll.head.value)
    # print(ll.head.next.value)
    # ll.insertBefore(15,9)
    # ll.insertAfter(10,14)
    print(ll)
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    print(ll.kthFromEnd(0))
    print(ll.__str__())
