class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k = k % total_chalk
        i = 0
        while k >=  0:
            k -= chalk[i]  # 5 -= 3 --> 2 
            i += 1         # i = 1,  k = 2
        return i - 1       #  2 -= 4 --> -2
                            #   1 += 1   ---> 2


       
