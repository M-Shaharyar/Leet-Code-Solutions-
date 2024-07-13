class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = []
        for index in range(len(nums)):
            for i in range(index+1,len(nums)):
                if nums[index]+nums[i]==target:
                    num.append(index)
                    num.append(i)
                    return num