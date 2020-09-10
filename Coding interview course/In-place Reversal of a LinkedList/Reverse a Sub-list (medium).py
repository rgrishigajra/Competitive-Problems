from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    before_sublist = None
    after_sublist = None
    curr = head
    for i in range(p-2):
        print(curr.value)
        curr = curr.next
    before_sublist = curr
    print(curr.value)
    prev = curr
    curr = curr.next
    next = curr.next
    for i in range(q-p+1):
        print(curr.value)
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    before_sublist.next.next = next
    before_sublist.next = prev
    return head





def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
