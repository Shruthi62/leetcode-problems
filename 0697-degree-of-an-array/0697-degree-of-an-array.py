
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            if num not in first:
                first[num] = i

            last[num] = i

        degree = max(freq.values())
        result = len(nums)

        for num in freq:
            if freq[num] == degree:
                length = last[num] - first[num] + 1
                result = min(result, length)

        return result
