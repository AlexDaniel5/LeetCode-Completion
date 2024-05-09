class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse = True)
        i = 0
        total = 0
        # Iterate through the children while k is larger than zero
        while k > 0:
            happiness[i] -= i
            # All values won't change the total from here, might as will return
            if happiness[i] < 1:
                break
            total += happiness[i]
            i += 1
            k -= 1
        return total

print(Solution().maximumHappinessSum([12,1,42], 3)) # 53