class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set("aeiouAEIOU")
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] not in v:
                left+=1
            if s[right] not in v:
                right-=1
            if s[left] in v and s[right] in v:
                s[left] , s[right] = s[right], s[left]
                left +=1
                right-=1
        return "".join(s)