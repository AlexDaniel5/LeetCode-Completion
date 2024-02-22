class Solution(object):
    def findJudge(self, n, trust):
        # If list is empty
        if not trust:
            # A bug
            if n == 1:
                return 1
            return -1
        # Get the count for the most liked person
        count = {}
        for sublist in trust:
            if sublist[1] not in count:
                count[sublist[1]] = 1
            else:
                count[sublist[1]] += 1
        maxCount = max(count.values())
        # Get a list of most liked people
        mostPopular = [
            element
            for element, elementCount in count.items()
            if elementCount == maxCount
        ]
        # If there is a tie for most liked person
        if len(mostPopular) > 1:
            return -1   
        # Get a list of every other person
        nonPopular = [
            element 
            for element in count.keys() 
            if element not in mostPopular
        ]
        allLiked = set()
        potentialJudge = mostPopular[0]
        for sublist in trust:
            # If judge likes someone
            if sublist[0] == potentialJudge:
                return -1
            # Else add the person to people that like the judge
            elif sublist[0] in nonPopular:
                allLiked.add(sublist[0])
        # If not everybody likes the judge
        if allLiked != set(nonPopular):
            return -1
        return potentialJudge   
        
solution = Solution()
print(solution.findJudge(2, [[1,2]])) # 2
print(solution.findJudge(3,[[1,3],[2,3],[3,1]])) # -1
print(solution.findJudge(2,[])) # -1
print(solution.findJudge(1, [])) # 1