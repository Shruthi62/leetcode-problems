
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        index_map = {}

        for i, name in enumerate(list1):
            index_map[name] = i

        min_sum = float('inf')
        result = []

        for j, name in enumerate(list2):

            if name in index_map:

                index_sum = index_map[name] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [name]

                elif index_sum == min_sum:
                    result.append(name)

        return result
