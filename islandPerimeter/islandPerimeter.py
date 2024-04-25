from collections import deque

class Solution(object):
    def islandPerimeter(self, grid):
        def bfs(row, col):
            perimeter = 0
            # Start the queue with the found land tile
            queue = deque([(row, col)])
            visited.add((row, col))
            while queue:
                row, col = queue.popleft()
                # All cardinal directions possible
                for rowMove, colMove in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newRow, newCol = row + rowMove, col + colMove
                    if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]): # Tile is in bounds
                        # Add tile to visited
                        if grid[newRow][newCol] == 1 and (newRow, newCol) not in visited: # Tile is a land tile and hasn't been visited
                            queue.append((newRow, newCol))
                            visited.add((newRow, newCol))
                        # Water, thus add perimeter to island
                        elif grid[newRow][newCol] == 0:
                            perimeter += 1
                    # Out of bounds must be perimeter
                    else:
                        perimeter += 1
            return perimeter
        
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return bfs(row, col)