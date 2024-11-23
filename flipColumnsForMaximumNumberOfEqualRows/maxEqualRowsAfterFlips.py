from collections import defaultdict

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        rows = defaultdict(int)
        for row in matrix:
            # Flip the row
            flippedArray = tuple([1 - x for x in row])
            rows[tuple(row)] += 1
            rows[flippedArray] += 1
        # Return the highest value
        return max(rows.values())

print(Solution().maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]])) # 2