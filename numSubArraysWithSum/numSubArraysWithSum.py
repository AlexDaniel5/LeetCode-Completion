class Solution(object):
    # Calculates the number of subarrays with a sum at most equal to the goal
    def atMost(self, nums, goal):
        l = 0
        r = 0
        ans = 0
        total_sum = 0
        length = len(nums)
        # Iterate through the array with a right pointer
        while r < length:
            total_sum += nums[r]
            # If the sum is larger than the goal, slide the left pointer
            while total_sum > goal and l <= r:
                total_sum -= nums[l]
                l += 1
            # Add all subarrays from the right to the left pointer
            ans += r - l + 1
            r += 1
        return ans
    
    # Calculates the number of subarrays with a sum exactly equal to the goal
    def numSubarraysWithSum(self, nums, goal):
        return self.atMost(nums, goal) - self.atMost(nums, goal - 1)
    
print(Solution().numSubarraysWithSum([0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0], 3)) # 48
print(Solution().numSubarraysWithSum([1,0,0,0,0,0,0,0,0,0], 1)) # 10
print(Solution().numSubarraysWithSum([1,0,1,0,1], 2)) # 4