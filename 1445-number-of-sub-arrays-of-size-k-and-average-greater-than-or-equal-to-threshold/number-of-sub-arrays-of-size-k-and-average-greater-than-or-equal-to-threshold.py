class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
        i = 0
        while i < len(arr):
            if (window_sum/k) >= threshold:
                count += 1
            window_sum -= arr[i]
            if (k+i) >= len(arr):
                break
            window_sum += arr[k+i]
            i += 1
        return count