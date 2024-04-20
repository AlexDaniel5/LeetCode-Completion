class Solution(object):
    def findFarmland(self, land):
        def dfs(row, col):
            if (
                0 <= row < len(land) # Out of bounds on row
                and 0 <= col < len(land[0]) # Out of bounds on column
                and land[row][col] == 1
            ):
                # Underscore is used to ensure we don't return a tuple and to get rid of the unneeded value
                rightestCol, _ = dfs(row, col+1)
                _, lowestRow = dfs(row+1, col)
                # If the rectangle has a length or width of 1
                if rightestCol is None:
                    rightestCol = col
                if lowestRow is None:
                    lowestRow = row
                # Convert farmland to forested land so we won't count the rectangle twice in the future
                for r in range(row, lowestRow+1):
                    for c in range(col, rightestCol+1):
                        land[r][c] = 0
                return rightestCol, lowestRow
            # If the recursive step is out of bounds or reaches forested land
            return None, None
        result = []
        rows = len(land)
        cols = len(land[0])
        # Check every tile of land for farmland
        for row in range(rows):
            for col in range(cols):
                if land[row][col] == 1:
                    rightestCol, lowestRow = dfs(row, col)
                    result.append((row, col, lowestRow, rightestCol))
        return result
    
print(Solution().findFarmland([[0,1],[1,0]])) # [[0,1,0,1],[1,0,1,0]]