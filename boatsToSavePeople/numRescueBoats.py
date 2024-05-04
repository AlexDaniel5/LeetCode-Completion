class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        boats = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            # Remove heaviest person
            remain = limit - people[r]
            r -= 1
            # Remove the lightest person
            if remain >= people[l]:
                l += 1
            boats += 1
        return boats
    
print(Solution().numRescueBoats([3,2,2,1], 3)) # 3