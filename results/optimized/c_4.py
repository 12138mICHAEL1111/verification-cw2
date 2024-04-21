class ListNode:
    """ Definition for singly-linked list. """
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def reverse_k_group(head, group_size):
    """ Reverse nodes in k group in linked list. """
    if head is None or group_size == 1:
        return head

    dummy = ListNode(-1)
    dummy.next = head
    prev_node, curr = dummy, dummy.next
    
    total_count = 0
    while curr:
        curr = curr.next
        total_count += 1

    while total_count >= group_size:
        curr = prev_node.next
        next_node = curr.next
        for _ in range(1, group_size):
            curr.next = next_node.next
            next_node.next = prev_node.next
            prev_node.next = next_node
            next_node = curr.next
        prev_node = curr
        total_count -= group_size

    return dummy.next

def build_list(elements):
    """ Helper function to build a linked list from a list of elements. """
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for elem in elements[1:]:
        current.next = ListNode(elem)
        current = current.next
    return head

def print_list(head):
    """ Helper function to print the linked list. """
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

# Example usage
vals = [1, 2, 3, 4, 5]
group_size = 3
linked_list_head = build_list(vals)
new_head = reverse_k_group(linked_list_head, group_size)
print_list(new_head)

# ************* Module c_4
# results/optimized/c_4.py:1:0: R0903: Too few public methods (0/2) (too-few-public-methods)
# results/optimized/c_4.py:7:26: W0621: Redefining name 'group_size' from outer scope (line 55) (redefined-outer-name)
# results/optimized/c_4.py:55:0: C0103: Constant name "group_size" doesn't conform to UPPER_CASE naming style (invalid-name)
# ------------------------------------------------------------------
# Your code has been rated at 9.33/10 (previous run: 8.37/10, +0.96)