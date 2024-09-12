class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)
        size = len(nums)
        for i in range(len(nums)):
            res[(i+k) % size] = nums[i]
        for i in range(len(res)):
            nums[i] = res[i]
        return nums