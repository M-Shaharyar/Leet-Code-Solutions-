from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        if count_s == count_t:
            return True
        return False


obj = Solution()
s = "rat"
t = "rat"
ans = obj.isAnagram(s, t)
print(ans)
