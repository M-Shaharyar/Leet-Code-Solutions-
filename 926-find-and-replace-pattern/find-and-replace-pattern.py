class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word, pattern):
            if len(word) != len(pattern):
                return False
            
            # Create mappings from word to pattern and vice versa
            w_to_p = {}
            p_to_w = {}
            
            for w_char, p_char in zip(word, pattern):
                if w_char in w_to_p and w_to_p[w_char] != p_char:
                    return False
                if p_char in p_to_w and p_to_w[p_char] != w_char:
                    return False
                w_to_p[w_char] = p_char
                p_to_w[p_char] = w_char
            
            return True

        # Filter words that match the pattern
        return [word for word in words if matches(word, pattern)]