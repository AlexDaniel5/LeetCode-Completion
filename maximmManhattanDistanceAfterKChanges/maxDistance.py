class Solution:

    # Calculate total distance in a line, plus any flips
    def count(self, a, b, flips):
        return abs(a - b) + 2 * flips
    
    def maxDistance(self, s, k):
        from collections import Counter
        ans = 0
        counts = Counter()
        for c in s:
            counts[c] += 1 # Increment the count for the current direction

            # Extract current counts for each direction
            north, south = counts['N'], counts['S']
            east, west = counts['E'], counts['W']

            # Calculate how many flips we can make for the vertical and horizontal direction
            times1 = min(north, south, k)
            times2 = min(east, west, k - times1)

            # Compute the total modified Manhattan distance using the count function
            total = self.count(north, south, times1) + self.count(east, west, times2)
            ans = max(ans, total)
        return ans

print(Solution().maxDistance("EWWE", 0)) # 1
print(Solution().maxDistance("NSWWEW", 3)) # 6