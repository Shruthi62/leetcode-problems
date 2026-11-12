
class Solution:
    def findLHS(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = 0

        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]

                result = max(result, length)

        return result

        