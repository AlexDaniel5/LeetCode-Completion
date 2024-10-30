class Solution(object):
    def maxMoves(self, grid):
        # Get grid dimensions
        m, n = len(grid), len(grid[0])
        directions = [(-1, 1), (0, 1), (1, 1)] # Possible moves: up-right, right, down-right
        memo = {}

        def dfs(row, col):
            # If at the right edge, no more moves are possible
            if col == n - 1:
                return 0
            # Return cached result if this cell has already been computed
            if (row, col) in memo:
                return memo[(row, col)]
            
            maxMoves = 0
            currentValue = grid[row][col]
            # Use DFS search to check possible moves
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < m and newCol < n and grid[newRow][newCol] > currentValue:
                    maxMoves = max(maxMoves, 1 + dfs(newRow, newCol))
            # Cache the result for this cell
            memo[(row, col)] = maxMoves
            return maxMoves

        result = 0
        # Start DFS from each cell in the first column
        for i in range(m):
            result = max(result, dfs(i, 0))

        return result
    
print(Solution().maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]])) # 3