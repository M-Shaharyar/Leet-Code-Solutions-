class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res_num = 0
        temp = x
        while temp > 0:
            val = temp % 10
            temp = temp // 10
            res_num = res_num * 10 + val
        return res_num == x
