class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key, value):
        node = self.cache.get(key)
        if node:
            self._remove(node)
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.cache[n.key]

# Usage
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)           # evicts key 2
print(cache.get(2))       # returns -1 (not found)
cache.put(4, 4)           # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4

# ************* Module c_0
# results/raw/c_0.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
# results/raw/c_0.py:18:14: W0622: Redefining built-in 'next' (redefined-builtin)
# results/raw/c_0.py:22:8: C0103: Variable name "p" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_0.py:44:12: C0103: Variable name "n" doesn't conform to snake_case naming style (invalid-name)
# -------------------------------------------------------------------
# Your code has been rated at 9.22/10 (previous run: 10.00/10, -0.78)