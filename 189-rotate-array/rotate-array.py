class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i+k < len(nums):
                res[i+k] = nums[i]
            elif i + k > len(nums)-1:
                res[(i+k)%len(nums)] = nums[i]
        for i in range(len(res)):
            nums[i] = res[i]
        