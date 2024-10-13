class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first , end = 0 , len(nums) - 1

        while first <= end:
            mid = ( first + end ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]< target:
                first = mid+1
            else:
                end =mid - 1
        return -1