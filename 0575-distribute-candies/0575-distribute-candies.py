class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:

        different_types = len(set(candyType))

        max_candies = len(candyType) // 2

        return min(different_types, max_candies)        