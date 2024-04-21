class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if head is None or k == 1:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    prev, curr = dummy, dummy.next
    
    count = 0
    while curr:
        curr = curr.next
        count += 1

    while count >= k:
        curr = prev.next
        next_ = curr.next
        for _ in range(1, k):
            curr.next = next_.next
            next_.next = prev.next
            prev.next = next_
            next_ = curr.next
        prev = curr
        count -= k

    return dummy.next

# Helper to populate a linked list from a Python list
def build_list(elements):
    head = ListNode(elements[0])
    current = head
    for elem in elements[1:]:
        current.next = ListNode(elem)
        current = current.next
    return head

# Helper to print a linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

# Example usage
vals = [1, 2, 3, 4, 5]
k = 3
head = build_list(vals)
new_head = reverseKGroup(head, k)
print_list(new_head)

# ************* Module c_4
# results/raw/c_4.py:2:30: W0622: Redefining built-in 'next' (redefined-builtin)
# results/raw/c_4.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
# results/raw/c_4.py:6:0: C0103: Function name "reverseKGroup" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_4.py:6:18: W0621: Redefining name 'head' from outer scope (line 52) (redefined-outer-name)
# results/raw/c_4.py:6:24: W0621: Redefining name 'k' from outer scope (line 51) (redefined-outer-name)
# results/raw/c_4.py:34:4: W0621: Redefining name 'head' from outer scope (line 52) (redefined-outer-name)
# results/raw/c_4.py:42:15: W0621: Redefining name 'head' from outer scope (line 52) (redefined-outer-name)
# ------------------------------------------------------------------
# Your code has been rated at 8.37/10 (previous run: 9.11/10, -0.74)