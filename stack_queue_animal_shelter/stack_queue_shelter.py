# from stack_queue.stack_and_queue import Stack,Queue

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Cat(object):

    def __str__(self):
        return "cat"


class Dog:
    def __str__(self):
        return "dog"


class mouse:
    def __str__(self):
        return "mouse"

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
        return temp.value


    def is_empty(self):
        return self.front == None

    def peek(self):
        return self.front.value

    def __str__(self):
        current = self.front
        items = ''

        while current:
            items += str(current.value) + '\n'
            current = current.next

        return items



class AnimalShelter(object):
    def __init__(self):
        self.shelter=Queue()

        # self.front = None
        # self.queue = None
    def enqueue(self, name, pref):
        pref = pref.lower()
        animal = {
            "name": name,
            "type": pref
        }
        if pref == "dog":
            self.shelter.enqueue(animal)
        elif pref == "cat":
            self.shelter.enqueue(animal)
        else:
            print("Invalid animal type")

    def dequeue(self, pref):
        pref = pref.lower()
        if (pref != "dog") and (pref != "cat"):
                raise Exception("The shelter is empty !")
        elif ((pref == "dog")):
             return self.shelter.dequeue()
        elif ((pref == "cat")):
            return self.shelter.dequeue()
        # while self.front != None:
        #     temp = self.front
        #     self.front = self.front.next
        #     if temp.value == pref:
        #         temp.next = None
        #         return temp.value



    def peek(self):
        return self.shelter.peek()

if __name__ == "__main__":
    shelter = AnimalShelter()

    shelter.enqueue("Marsha","cat")
    shelter.enqueue("rex", "dog")
    shelter.enqueue("Tuna", "cat")
    shelter.enqueue("melo", "dog")
    print(shelter.shelter)
    # print("\n")
    print(shelter.dequeue("cat"))
    # print("\n")

    print(shelter.shelter)


