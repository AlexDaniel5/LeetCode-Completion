class Solution(object):
    def threeSum(self, nums):
        sums = []
        nums.sort()
        length = len(nums) - 1
        
        for i, num in enumerate(nums):
            # If the number is the same as the previous number
            if i > 0 and num == nums[i-1]:
                continue
            # Skip the first number as num is already that value
            l, r = i + 1, length
            # Find all combinations of a three sum with num as the third number
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                # Three sum adds to zero
                else:
                    sums.append([num, nums[l], nums[r]])
                    l += 1
                    # Ensure the left interval doesn't contain the same value as previously
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return sums 
    
print(Solution().threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2], [-1,0,1]]