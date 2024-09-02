class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)  # 2nd Example
        k = k % total_chalk       # 25%10  =  k = 5 
        i = 0
        while k >= chalk[i]:      # -2>=1   
            k -= chalk[i]         # k=k-chalk[i]                          
                                  # k=5-3  = 2  
                                  # i=0
                                  # k=2-4  = -2 
            i += 1                # i=1
        return i