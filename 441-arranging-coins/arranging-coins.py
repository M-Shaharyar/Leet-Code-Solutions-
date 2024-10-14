class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1 
        sum = 0
        while sum + i <= n:
            sum += i
            i += 1
        return i - 1