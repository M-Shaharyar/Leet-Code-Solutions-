class Solution:
    def bulbSwitch(self, n: int) -> int:
        for i in range(n):
            i = 1 + i
        return int(sqrt(n))
            