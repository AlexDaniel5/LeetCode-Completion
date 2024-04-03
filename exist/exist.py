class Solution(object):
    def exist(self, board, word):
        def dfs(row, col, char):
            if char == len(word):
                return True
            if (row < 0 or col < 0 or # Go out of bounds error
                row >= rows or col >= cols or
                word[char] != board[row][col] or # Char in index doesn't equal word's char
                (row, col) in path): # We've already visited that character
                return False 
            path.add((row, col))
            # Recursion to determine a valid path
            result = (dfs(row + 1, col, char + 1) or # Go right
                     dfs(row - 1, col, char + 1) or # Go left
                     dfs(row, col + 1, char + 1) or # Go up
                     dfs(row, col - 1, char + 1)) # Go down
            path.remove((row, col))
            return result

        rows = len(board)
        cols = len(board[0])
        path = set()
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False


print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True