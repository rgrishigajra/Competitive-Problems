# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle(head):
    slow_ptr = head
    fast_ptr = head
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if fast_ptr == slow_ptr:
            return slow_ptr
    return -1


def find_cycle_length(head):
    node = find_cycle(head)
    if node == -1:
        return -1
    count = 0
    ptr = node
    while True:
        ptr = ptr.next
        count += 1
        if ptr == node:
            break
    return count


def find_cycle_start(head):
    cycle_length = find_cycle_length(head)
    slow_ptr = head
    fast_ptr = head
    while cycle_length:
        fast_ptr = fast_ptr.next
        cycle_length -= 1
    while fast_ptr != slow_ptr:
        fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next
    return fast_ptr


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
