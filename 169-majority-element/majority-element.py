class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map =  dict()
        max_num = float('-inf')
        num = 0
        for i in nums:
            if i not in my_map:
                my_map[i]=1
                if my_map[i] > max_num:
                    max_num = my_map[i]
                    num = i
            elif i in my_map:
                my_map[i]+=1
                if my_map[i] > max_num:
                    max_num = my_map[i]
                    num = i
        return num