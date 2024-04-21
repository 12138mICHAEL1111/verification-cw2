def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(B) < len(A):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A's middle index
        j = half - i - 2  # B's middle index
        
        Aleft = A[i] if i >= 0 else float('-infinity')
        Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
        Bleft = B[j] if j >= 0 else float('-infinity')
        Bright = B[j + 1] if (j + 1) < len(B) else float('infinity')
        
        # Partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

# Example usage
nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))

# ************* Module c_1
# results/raw/c_1.py:1:0: C0103: Function name "findMedianSortedArrays" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:1:27: W0621: Redefining name 'nums1' from outer scope (line 30) (redefined-outer-name)
# results/raw/c_1.py:1:34: W0621: Redefining name 'nums2' from outer scope (line 31) (redefined-outer-name)
# results/raw/c_1.py:2:4: C0103: Variable name "A" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:2:7: C0103: Variable name "B" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:7:8: C0103: Variable name "A" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:7:11: C0103: Variable name "B" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:9:4: C0103: Variable name "l" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:9:7: C0103: Variable name "r" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:14:8: C0103: Variable name "Aleft" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:15:8: C0103: Variable name "Aright" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:16:8: C0103: Variable name "Bleft" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:17:8: C0103: Variable name "Bright" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:20:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
# results/raw/c_1.py:25:12: C0103: Variable name "r" doesn't conform to snake_case naming style (invalid-name)
# results/raw/c_1.py:27:12: C0103: Variable name "l" doesn't conform to snake_case naming style (invalid-name)
# ------------------------------------------------------------------
# Your code has been rated at 3.33/10 (previous run: 8.70/10, -5.36)