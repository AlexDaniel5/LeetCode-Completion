class Solution(object):
    def largestPerimeter(self, nums):
        nums = sorted(nums)
        totalSum = sum(nums)
        # Iterate through the list backwards
        for num in nums[::-1]:
            totalSum -= num
            # If the current number is greater than all numbers smaller, we've determined the biggest perimeter of the polygon
            if totalSum > num:
                totalSum += num
                break
        # If we don't have a polygon with three sides return -1
        if totalSum < nums[0] + nums[1] + nums[2]:
            return -1
        return totalSum
    
solution = Solution()
nums = [1, 12, 1, 2, 5, 50, 3]
print(solution.largestPerimeter(nums)) #12
nums = [1, 1, 2]
print(solution.largestPerimeter(nums)) #-1
nums = [1, 5, 1, 5]
print(solution.largestPerimeter(nums)) #12
nums = [1, 5, 1, 7]
print(solution.largestPerimeter(nums)) #-1
