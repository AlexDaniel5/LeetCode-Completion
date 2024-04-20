from collections import deque

class Solution(object):
    def numIslands(self, grid):
        # Converts an island to water using BFS
        def bfs(startRow, startCol):
            # Add the initial tile to the queue and convert it to water
            queue = deque([(startRow, startCol)])
            grid[startRow][startCol] = "0"

            while queue:
                row, col = queue.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                # Check the cardinal directions for land and convert it to water
                for rowMove, colMove in directions:
                    newRow, newCol = row + rowMove, col + colMove
                    if (
                        0 <= newRow < len(grid) # Out of range check for row
                        and 0 <= newCol < len(grid[0]) # Out of range check for column
                        and grid[newRow][newCol] == "1"
                    ):
                        grid[newRow][newCol] = "0"
                        queue.append((newRow, newCol))

        rows = len(grid)
        cols = len(grid[0])
        result = 0
        # For every tile check if it's land
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1": 
                    bfs(row, col)
                    result += 1
        return result
    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid)) # 1