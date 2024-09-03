class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k % total
        i = 0
        while k >= 0:
            k -= chalk[i]
            i += 1
        return i-1 
        
