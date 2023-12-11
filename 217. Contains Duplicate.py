from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)        



obj = Solution()
num = [0,1, 2,  3, 1]
ans = obj.containsDuplicate(num)
print(ans)
