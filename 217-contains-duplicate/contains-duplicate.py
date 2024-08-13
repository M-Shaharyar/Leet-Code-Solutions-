class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i,n in enumerate(nums):
            if i+1 < len(nums) and n == nums[i+1]:
                return True
        return False