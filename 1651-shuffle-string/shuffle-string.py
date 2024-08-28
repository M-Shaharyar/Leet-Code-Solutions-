class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        i = 0
        while i < len(s):
            res[indices[i]] = s[i]  
            i += 1
        return "".join(res)