class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        si = 0
        gi = 0
        while si < len(s) and gi < len(g):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                count += 1
            elif s[si] < g[gi]:
                si += 1
            elif s[si] > g[gi]:
                gi += 1
        return count