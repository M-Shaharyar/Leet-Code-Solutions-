class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = 2*len(nums)
        #ans = [0 for _ in range(size)]
        ans = []
        for i in nums:
            ans.append(i)
        for i in nums:
            ans.append(i)
        
        return ans
