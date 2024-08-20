class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        my_list = []
        val = 0
        while x > 0:
            val = x % 10
            x = x // 10
            my_list.append(val)
        left , right = 0 , len(my_list) - 1
        while left < right :
            if my_list[left] != my_list[right]:
                return False
            left , right = left + 1 , right - 1
        return True
