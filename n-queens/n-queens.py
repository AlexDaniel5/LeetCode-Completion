class Solution(object):
    def solveNQueens(self, n):
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):  # Loop through columns
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place the queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)  # Move to the next row

                # Backtrack (remove the queen)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result

print(Solution().solveNQueens(4)) # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]