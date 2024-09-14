class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res , n = 0 , len(s) - 1
        for i in range(len(s)):
            zero = one = 0
            for j in range(i,len(s)):
                if s[j] == '0': 
                    zero += 1
                if s[j] == '1':
                    one += 1
                if zero <= k or one <= k:
                    res += 1
        return res