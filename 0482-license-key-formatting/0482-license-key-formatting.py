
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        first = len(s) % k
        result = []

        if first > 0:
            result.append(s[:first])

        for i in range(first, len(s), k):
            result.append(s[i:i + k])

        return "-".join(result)
