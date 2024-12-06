class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)

        num_to_count = {}
        for i, num in enumerate(sorted_num):
            if not num in num_to_count:
                num_to_count[num] = i

        return [num_to_count[num] for num in nums]