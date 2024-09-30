class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i,n in enumerate(nums):
        #     if i+1 < len(nums) and n == nums[i+1]:
        #         return True
        # return False
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = i
            else:
                return True
        return False


