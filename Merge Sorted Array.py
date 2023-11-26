from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        size = m + n
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[size - 1] = nums2[n - 1]
                n -= 1
            elif nums1[m - 1] >= nums2[n - 1]:
                nums1[size - 1] = nums1[m - 1]
                m -= 1
            size -= 1
        if m ==0:
            for i in range(n):
                nums1[i] = nums2[i]

# Create an instance of the Solution class
solution = Solution()

# Call the merge method with sample inputs
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)

print(nums1)
