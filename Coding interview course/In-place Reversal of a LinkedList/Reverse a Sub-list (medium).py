from __future__ import print_function


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()


def reverseBetween(head, m: int, n: int):
    before_sublist = None
    after_sublist = None
    curr,prev = head,None
    if not head:
        return None
    for i in range(m-1):
        prev = curr
        curr = curr.next
    before_sublist = prev
    firstnode_sublist=curr
    for i in range(n-m+1):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    if before_sublist:
        before_sublist.next = prev
    else:
        head = prev
    if firstnode_sublist:
        firstnode_sublist.next = curr
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
    result = reverseBetween(head, 2, 5)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
