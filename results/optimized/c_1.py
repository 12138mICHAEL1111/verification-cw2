def find_median_sorted_arrays(nums1, nums2):
    array_a, array_b = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(array_b) < len(array_a):
        array_a, array_b = array_b, array_a
    
    left_index, right_index = 0, len(array_a) - 1
    while True:
        middle_a = (left_index + right_index) // 2
        middle_b = half - middle_a - 2
        
        a_left = array_a[middle_a] if middle_a >= 0 else float('-infinity')
        a_right = array_a[middle_a + 1] if (middle_a + 1) < len(array_a) else float('infinity')
        b_left = array_b[middle_b] if middle_b >= 0 else float('-infinity')
        b_right = array_b[middle_b + 1] if (middle_b + 1) < len(array_b) else float('infinity')
        
        if a_left <= b_right and b_left <= a_right:
            if total % 2:
                return min(a_right, b_right)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            right_index = middle_a - 1
        else:
            left_index = middle_a + 1

# Example usage
nums1 = [1, 2]
nums2 = [3, 4]
print(find_median_sorted_arrays(nums1, nums2))

# ************* Module c_1
# results/optimized/c_1.py:1:30: W0621: Redefining name 'nums1' from outer scope (line 29) (redefined-outer-name)
# results/optimized/c_1.py:1:37: W0621: Redefining name 'nums2' from outer scope (line 30) (redefined-outer-name)
# ------------------------------------------------------------------
# Your code has been rated at 9.17/10 (previous run: 3.33/10, +5.83)