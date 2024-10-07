class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = sum(arr[:k])
        i , j = 0 , k
        while j <= len(arr):
            if (window_sum/k) >= threshold:
                count += 1
            if j >= len(arr):
                return count
            window_sum -= arr[i]
            window_sum += arr[j]
            i += 1
            j += 1
        return count