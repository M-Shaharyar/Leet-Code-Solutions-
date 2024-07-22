class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = len(nums)//3 +1
        ls = []
        my_map = {}
        for i in nums:
            my_map[i] = 1 + my_map.get(i,0)
            if my_map[i] == count:
                ls.append(i)
        return ls