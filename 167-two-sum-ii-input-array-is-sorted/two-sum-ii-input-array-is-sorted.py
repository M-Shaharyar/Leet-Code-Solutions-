class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right , result = 0 , len(numbers) - 1 , []
        while left < right :
            if numbers[left] + numbers[right] == target:
                result.append(left+1)
                result.append(right+1)
                return result
            elif numbers[left] + numbers[right] > target:
                left -= 1
            elif numbers[right] + numbers[left] < target:
                right += 1
            left += 1
            right -= 1
