# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
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


def reverse_ll(head, m, n):
    print(head, m, n)
    head.print_list()
    curr, prev = head, None
    while m > 1:
        prev = curr
        curr = curr.next
        m, n = m-1, n-1
    before_sl = prev
    firstnode_sl = curr
    while n and curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        n -= 1
    if before_sl:
        before_sl.next = prev
    else:
        head = prev
    firstnode_sl.next = curr
    head.print_list()
    return head


def reverse_every_k_elements(head, k):
    itr, l = 0, 0
    result = head
    curr = head
    while curr:
        l += 1
        curr = curr.next
    while itr <= l:
        result = reverse_ll(result, itr+1, min(itr+k, l))
        itr += k
    return result


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
