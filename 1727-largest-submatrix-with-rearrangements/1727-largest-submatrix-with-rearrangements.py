class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n,ans,gist = len(matrix[0]), 0, [0]*len(matrix[0])
        for row in matrix:
            for j in range(n): gist[j] = 0 if not (m:=row[j]) else gist[j] +m
            ans = max(ans, max((k+1)*h for k,h in enumerate(sorted(gist, reverse=True))))
        return  ans

        