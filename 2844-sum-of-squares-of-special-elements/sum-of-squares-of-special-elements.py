class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result_sum = 0
        
        # Check each 1-indexed position
        for i in range(1, n + 1):
            if n % i == 0:  # If i divides n
                result_sum += nums[i - 1] ** 2  # Square of the value at position (i-1) in 0-indexed array
        
        return result_sum