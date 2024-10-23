class Solution:
    def makeGood(self,s:str)->str:
        stack = []
        i = 0
        while i < len(s):
            if (stack and 
                stack[-1] != s[i] and 
                stack[-1].lower() == s[i].lower()):
                stack.pop()
            else:
                stack.append(s[i])
            i +=1

        return "".join(stack) 
        
        
        
        
        
        # strr = ""
        # i = 0
        # while i < len(s) - 1:
        #     if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
        #         i += 2 
        #         continue
        #     strr += s[i]
        #     i += 1
        # if i < len(s):
        #     strr += s[i]
        # return strr