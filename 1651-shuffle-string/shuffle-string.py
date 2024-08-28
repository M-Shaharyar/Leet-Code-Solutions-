class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res , i = [0] * len(s) , 0
        while i < len(s):
            res[indices[i]] = s[i]  
            i += 1
        return "".join(res)