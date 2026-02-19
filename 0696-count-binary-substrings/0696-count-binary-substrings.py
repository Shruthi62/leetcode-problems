class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        total = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                total += min(prev, curr)
                prev = curr
                curr = 1
        
        total += min(prev, curr)
        return total
        