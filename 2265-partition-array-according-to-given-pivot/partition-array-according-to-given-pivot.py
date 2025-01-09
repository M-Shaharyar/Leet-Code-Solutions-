class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []
        
        # Partition the array
        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num == pivot:
                equal_to_pivot.append(num)
            else:
                greater_than_pivot.append(num)
        
        # Combine the partitions
        return less_than_pivot + equal_to_pivot + greater_than_pivot
