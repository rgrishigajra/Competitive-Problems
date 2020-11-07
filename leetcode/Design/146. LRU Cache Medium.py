class Node:
    def __init__(self, key, val=-1, prev=None, next=None):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'node value: {self.value}'


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.prev = self.tail
        self.tail.next = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        return

    def add(self, node):
        prev = self.head.prev
        next = self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        return

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)
        if self.capacity < len(self.cache):
            node = self.tail.next
            self.remove(node)
            del self.cache[node.key]
        return node.value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
