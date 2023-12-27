from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[nums[i]] = i
        return


obj = Solution()
s = [3, 3]
t = 6
ans = obj.twoSum(s, t)
print(ans)
