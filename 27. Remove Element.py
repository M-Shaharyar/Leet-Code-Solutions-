from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            if val == nums[s] and val != nums[e]:
                nums[s] = nums[e]
                nums[e] = "_"
                s += 1
                e -= 1
            elif val == nums[e]:
                nums[e] = "_"
                e -= 1
            else:
                s += 1


# Create an instance of the Solution class
solution = Solution()

# Call the merge method with sample inputs
nums1 = [3, 2, 2, 3]
val = 3
solution.removeElement(nums1, val)

print(nums1)
