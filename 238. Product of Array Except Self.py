from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lums = [0] * len(nums)
        pre = 1
        lums[0] = 1
        i = 0
        while i < len(nums) - 1:
            pre = pre * nums[i]
            lums[i + 1] = pre
            i += 1
        i = len(nums) - 1
        post = 1
        while i > 0:
            post = post * nums[i]
            lums[i - 1] *= post
            i -= 1
        return lums


obj = Solution()
nums = [1, 2, 3, 4]
ans = obj.productExceptSelf(nums)
print(ans)
