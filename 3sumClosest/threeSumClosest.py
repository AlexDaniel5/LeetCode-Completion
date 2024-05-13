class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        # Default solution
        result = nums[0] + nums[1] + nums[n - 1]
        i = 0
        # Have i be equal to every integer in the list except the last two numbers as the left and right pointer will already represent them
        while i < n - 2:
            l = i + 1
            r = n - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                # Found target value
                if currentSum == target:
                    return currentSum
                # Determine if the sum is any closer to the target value
                if abs(currentSum - target) < abs(result - target):
                    result = currentSum
                # Increase the current sum
                if currentSum < target:
                    l += 1
                # Decrease the current sum
                else:
                    r -= 1
            i += 1
        return result
    
print(Solution().threeSumClosest([-1,2,1,-4], 1)) # 2