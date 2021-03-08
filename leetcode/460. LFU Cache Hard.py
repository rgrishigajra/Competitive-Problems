class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1


class Dll:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, node):
        node.next = self.head
        node.prev = self.head.prev
        node.prev.next = node
        node.next.prev = node
        self.size += 1
        return

    def pop(self, node=None):
        if self.size == 0:
            return
        if not node:
            node = self.tail.next
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        self.size -= 1
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.node_map = {}
        self.freq_map = collections.defaultdict(Dll)
        self.capacity = capacity
        self.min_freq = 0
        self.size = 0

    def update(self, node):
        freq = node.freq
        self.freq_map[freq].pop(node)
        if self.min_freq == freq and not self.freq_map[freq]:
            self.min_freq += 1
        node.freq += 1
        freq = node.freq
        self.freq_map[freq].push(node)

    def get(self, key: int) -> int:
        # print(key)
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # print(key,value)
        if key in self.node_map:
            node = self.node_map[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freq_map[self.min_freq].pop()
                del self.node_map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.node_map[node.key] = node
            self.freq_map[1].push(node)
            self.min_freq = 1
            self.size += 1
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
