class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        # Not a real triangle
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
            return "scalene"
        else:
            return "isosceles"
        
print(Solution().triangleType([8, 4, 2])) # none