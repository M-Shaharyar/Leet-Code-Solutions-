from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        l = 1
        r = 1
        while r<size:
            if nums[r]==nums[r-1]:
                r = r + 1
            elif nums[r]!=nums[r-1]:
                nums[l] = nums[r]
                l = l + 1
                r = r + 1
        return l



obj = Solution()
num = [0,1, 2,  3, 4]
count = obj.removeDuplicates(num)
print(count)
