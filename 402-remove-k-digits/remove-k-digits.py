class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        # Remove any remaining k digits from the end of the stack
        stack = stack[:len(stack) - k]

        # Convert to string and remove leading zeros manually
        res = "".join(stack).lstrip('0')

        # If the result is empty after removing leading zeros, return "0"
        return res if res else "0"
