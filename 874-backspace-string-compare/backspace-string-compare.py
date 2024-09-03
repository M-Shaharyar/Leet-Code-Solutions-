class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        for i in s:
            if i == "#" and len(ans1) != 0:
                ans1.pop()
            elif i != "#":
                ans1.append(i)
        for i in t:
            if i == "#" and len(ans2) != 0:
                ans2.pop()
            elif i != "#":
                ans2.append(i)
        return ans1 == ans2
        