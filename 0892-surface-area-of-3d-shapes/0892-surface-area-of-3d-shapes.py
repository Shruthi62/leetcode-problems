
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                height = grid[i][j]

                if height > 0:
                    area += 2
                    area += 4 * height

                    if i > 0:
                        area -= 2 * min(height, grid[i - 1][j])

                    if j > 0:
                        area -= 2 * min(height, grid[i][j - 1])

        return area
