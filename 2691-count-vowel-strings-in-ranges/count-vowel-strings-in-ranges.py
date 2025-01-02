class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def helperfunction(word):
            vowels  = {'a','e','i','o','u'}
            return word[0] in vowels  and word[-1] in vowels

        def prefix_sum(words):
            n = len(words)
            prefix  = [0] * n
            prefix[0] = 1 if helperfunction(words[0]) else 0

            for i in range(1,n):
                prefix[i] = prefix[i-1] + (1 if helperfunction(words[i]) else 0)
            return prefix

        def answer_quries(prefix,quries):
            result = []
            for li, ri in quries:
                if li == 0:
                    result.append(prefix[ri])
                else:
                    result.append(prefix[ri] - prefix[li - 1])
            return result
        prefix = prefix_sum(words)
        return answer_quries(prefix,queries)
    
    

        