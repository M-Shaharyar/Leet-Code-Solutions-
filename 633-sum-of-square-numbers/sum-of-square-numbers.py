class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0 
        right = int(sqrt(c))

        while(left <= right ):
            sumVal = left * left + right * right 
            if(sumVal > c):
                right -=1
            elif(sumVal < c):
                left +=1
            else:
                return True
        return False