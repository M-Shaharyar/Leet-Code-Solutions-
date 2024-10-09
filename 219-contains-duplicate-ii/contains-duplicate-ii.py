class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = set()
        L = 0
        for i in range(len(nums)):
            if i - L > k:
                my_map.remove(nums[L])
                L += 1
            if nums[i] in my_map:
                return True
            my_map.add(nums[i])
        return False            
