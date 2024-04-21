class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next_node = None  # Changed from 'next' to 'next_node'

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next_node = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        previous, next_node = node.prev, node.next_node
        previous.next_node, next_node.prev = next_node, previous

    def _add(self, node):
        pre_tail = self.tail.prev  # Changed from 'p' to 'pre_tail'
        pre_tail.next_node = node
        self.tail.prev = node
        node.prev = pre_tail
        node.next_node = self.tail

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
            node_to_remove = self.head.next_node  # Changed from 'n' to 'node_to_remove'
            self._remove(node_to_remove)
            del self.cache[node_to_remove.key]

# Usage can be kept as is.

# ************* Module c_0
# results/optimized/c_0.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
# ------------------------------------------------------------------
# Your code has been rated at 9.76/10 (previous run: 9.22/10, +0.54)