class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k = k % total_chalk
        i = 0
        while k >=  0:
            k -= chalk[i]  # 5 -= 3 --> 2 
            i += 1
        return i - 1

       
