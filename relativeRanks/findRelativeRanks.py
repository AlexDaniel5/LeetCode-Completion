class Solution(object):
    def findRelativeRanks(self, score):
        length = len(score)
        # Keep track of the indexes of the integers
        index = list(range(length))
        # Resorts the index array based on the ranking of scores
        index.sort(key=lambda x: -score[x])
        print(index)
        # Assign placement strings
        top3 = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        placements = [None] * length
        for i in range(length):
            if i > 2:
                placements[index[i]] = str(i+1)
            else:
                placements[index[i]] = top3[i]
        return placements
    
print(Solution().findRelativeRanks([10,3,8,9,4])) # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]