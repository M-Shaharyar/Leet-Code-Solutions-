class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        result = 0
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hash_table:
                return [hash_table[result],i]
            hash_table[nums[i]] = i 
        
