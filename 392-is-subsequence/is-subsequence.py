class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        elif len(t)==0 and len(s)!=0:
            return False
        index = 0
        for i in t:
            if s[index]==i:
                index+=1
            if index == len(s):
                return len(s)==index

        return len(s)==index
        