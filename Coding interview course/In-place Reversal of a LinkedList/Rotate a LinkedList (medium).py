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


def rotate(head, rotations):
    # TODO: Write your code here
    node = head
    idx = 1
    while node.next:
        node = node.next
        idx += 1
    le = idx
    node.next = head
    node = head
    prev = None
    rotations = rotations % le
    while rotations > 0:
        rotations -= 1
        prev = node
        node = node.next
    prev.next = None
    return node


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
