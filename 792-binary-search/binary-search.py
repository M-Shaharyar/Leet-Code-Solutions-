class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[k] == target:
                        return k
        return -1
            