# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s , e = 0 , n
        
        while s <= e:
            mid = ( s + e )// 2
            num = guess(mid)
            if num == 0:
                return mid
            elif num == -1:
                e = mid - 1
            else: 
                s = mid + 1
        return mid
        