from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return f'{self.value}'
    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    mid, fast = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        mid = mid.next
    prev = None
    node = mid.next
    mid.next = None
    while node:
        nex = node.next
        node.next = prev
        prev = node
        node = nex
    # print(prev.print_list(), head.print_list())
    node2 = prev
    node1 = head
    while node1 or node2:
        nex1 = node1.next
        node1.next = node2
        if node2:
            nex2 = node2.next
            node2.next = nex1
        node1 = nex1
        node2 = nex2
    return


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
