class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed = [0]+flowerbed+[0]
        size = len(flowerbed)
        for i in range(1,len(flowerbed)-1,1):
            if flowerbed[i-1]!=1 and flowerbed[i+1]!=1 and flowerbed[i]!=1:
                n -=1
                flowerbed[i]=1
            if n == 0:
                return True
        if n!=0:
            return False
        else:
            return True