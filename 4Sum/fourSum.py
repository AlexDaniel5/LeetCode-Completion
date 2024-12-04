class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res, quad = [], []
        def kSum(k, start, target):
            if k != 2:
                # Find a value to work with, leaving enough numbers to finish the quad (k - 1)
                for i in range(start, len(nums) - k + 1):
                    # Skip duplicates
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    # Find a second number to work with
                    kSum(k - 1, i + 1, target - nums[i])
                    # Get rid of the old list and make a new list in the next iteration
                    quad.pop()
                return
            # Find the remaining two numbers to find the target
            lp, rp = start, len(nums) - 1
            while lp < rp:
                # Make a larger sum
                if nums[lp] + nums[rp] < target:
                    lp += 1
                # Make a smaller sum
                elif nums[lp] + nums[rp] > target:
                    rp -= 1
                # Sum is equal to target
                else:
                    res.append(quad + [nums[lp], nums[rp]])
                    lp += 1
                    # Skip duplicates
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
        kSum(4, 0, target)
        return res
    
print(Solution().fourSum([1,0,-1,0,-2,2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution().fourSum([2,2,2,2,2], 8)) # [[2, 2, 2, 2]]