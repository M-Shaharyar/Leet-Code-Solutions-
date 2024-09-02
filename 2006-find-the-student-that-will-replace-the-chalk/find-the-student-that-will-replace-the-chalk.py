class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k % total
        i = 0
        while i <= len(chalk):
            if k < chalk[i]:
                return i
            k = k - chalk[i]
            i += 1
        
