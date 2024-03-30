class Solution(object):
    def countSubarrays(self, nums, k):
        subArrayCount = 0
        l = 0
        maxCount = 0
        length = len(nums)
        maximum = max(nums)
        for r in range(length):
            if nums[r] == maximum:
                maxCount += 1
            # Slide left interval if we have met more than k values of the maximum number or if we're at the maxCount
            while l <= r and maxCount > k or l <= r and maxCount == k and nums[l] != maximum:
                if nums[l] == maximum:
                    maxCount -= 1
                l += 1
            if maxCount == k:
                subArrayCount += l + 1 # Add all elements to the left plus one for index starting at 0
        return subArrayCount
    
print(Solution().countSubarrays([1,3,2,3,3], 2)) # 6