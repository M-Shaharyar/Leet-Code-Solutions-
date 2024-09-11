class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ""
        b = ""
        for i in word1:
            a += i
        # a = abc
        for i in word2:
            b += i
        # b = abc
        return a == b
        

        