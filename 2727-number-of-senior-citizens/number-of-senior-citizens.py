class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age = 0
        count = 0
        for i in details:
            if int(i[11:13])>60:
                count+=1
        return count            