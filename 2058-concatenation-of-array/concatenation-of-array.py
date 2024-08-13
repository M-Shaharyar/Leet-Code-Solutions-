class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums) * 2
        ans = [0] * size
        for i,n in enumerate(nums):
            ans[i] = n
            ans[i+(len(nums))] = n
        return ans