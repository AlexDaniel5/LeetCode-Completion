class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        l = 0
        goalSums = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum > goal:
                currSum -= nums[l]
                l += 1
            if goal == 0:
                goalSums += r - l + 1
            elif currSum == goal:
                goalSums += 1
                while l <= r and nums[l] == 0:
                    goalSums += 1
                    l += 1
        return goalSums
    
print(Solution().numSubarraysWithSum([0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0], 3)) # 48