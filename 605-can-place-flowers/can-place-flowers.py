class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0]+flowerbed+[0]
        size = len(f)-1
        for i in range(1,size,1):
            if f[i-1]!=1 and f[i+1]!=1 and f[i]!=1:
                n -=1
                f[i]=1
        return n<=0