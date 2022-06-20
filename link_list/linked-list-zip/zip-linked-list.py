from link_list.linked_list import LinkedList


# def zip_lists(ll1, ll2):
#     current1 = ll1.head
#     current2 = ll2.head
#
#
#     while current2:
#
#         current1.next = current1.next.next
#         current2.next = current2.next.next
#
#         current2.next = current1.next
#         current1.next = current2.next
#
#         current1 = current1.next
#         current2 = current2.next
#         current2 = current2.next


# def zipLinkedLists(l1, l2):
#     if l1 is None:
#         return l2
#
#     if l2 is None:
#         return l1
#     result = l1
#
#     recur = result.zipLinkedLists(l1.next, l2.next)
#
#     # result = l1
#     l1.next = l2
#     l2.next = recur
#
#     return result


def zipLinkedLists(l1, l2):
    current1 = l1.head
    current2 = l2.head
    #result= current2
    while current2:
        if current1:
          #  l1.insertBefore(current1.value, current2.value)
            l1.insertAfter(current1.value, current2.value)
            current1 = current1.next.next
            current2 = current2.next
        else:
            l1.append(current2.value)
            current2 = current2.next


if __name__ == '__main__':
    #ll = LinkedList()
    # ll.append(5)
    # ll.append(10)
    # ll.insert(15)
    # print(ll.includes(5))
    # print(ll.head.value)
    # print(ll.head.next.value)
    # ll.insertBefore(15,9)
    # ll.insertAfter(10,14)
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(5)

    l2.append(2)
    l2.append(4)
    l2.append(6)

    zipLinkedLists(l1, l2)
    print(l1.__str__())