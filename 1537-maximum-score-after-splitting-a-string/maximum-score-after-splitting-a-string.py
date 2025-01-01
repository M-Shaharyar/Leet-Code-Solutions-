class Solution:
    def maxScore(self, s: str) -> int:
        left = ""
        right = ""
        current_score = 0
        max_score = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            current_score = int(left.count('0')) + int(right.count('1'))
            max_score = max(current_score,max_score)
        return max_score