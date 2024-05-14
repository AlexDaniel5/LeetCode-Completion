class Solution(object):
    def getMaximumGold(self, grid):
        def dfs(row, col):
            # If we're out of range or the cell has no gold return 0
            if (
                min(row, col) < 0 or row == rows or col == cols
                or grid[row][col] == 0):
                return 0
            temp = grid[row][col]
            # Set the cell as visited
            grid[row][col] = 0
            result = 0
            moves = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            # Recursively call the DFS function keeping track of the amount of gold collected
            for horiz, vert in moves:
                result = max(result, temp + dfs(horiz, vert))
            # Reset the cell's value for when we start a DFS search at another cell
            grid[row][col] = temp
            return result
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        # Start a DFS search at each cell
        for row in range(rows):
            for col in range(cols):
                result = max(dfs(row, col), result)
        return result
    
print(Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])) # 28