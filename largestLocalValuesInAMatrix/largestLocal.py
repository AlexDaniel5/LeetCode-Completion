class Solution(object):
    def largestLocal(self, grid):
        length = len(grid) - 2 # Size of result array
        result = [[0] * (length) for _ in range(length)]
        # Iterate through result array
        for i in range(length):
            for j in range(length):
                # Iterate through grid
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        result[i][j] = max(result[i][j], grid[r][c])
        return result

print(Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])) # [[9,9],[8,6]]
print(Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])) # [[2,2,2],[2,2,2],[2,2,2]]