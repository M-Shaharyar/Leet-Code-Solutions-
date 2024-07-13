class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        lastcount = 0
        for i in s:
            if i !=" ":
                count+=1
                lastcount = count
            elif i == " ":
                count = 0
        return lastcount