class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        num = 0
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hash_table:
                return [hash_table[num],i]
            hash_table[nums[i]] = i
