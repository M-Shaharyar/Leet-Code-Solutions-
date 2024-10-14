class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == target:
                    return j
        return -1
            