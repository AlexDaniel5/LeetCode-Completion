class Solution(object):
    def canSortArray(self, nums):
        def countBits(n):
            return bin(n).count("1")
        
        curMin, curMax = nums[0], nums[0]
        prevMax = 0
        for n in nums:
            # Extend the current section if the number has the same count of set bits
            if countBits(n) == countBits(curMin):
                curMin = min(curMin, n)
                curMax = max(curMax, n)
            # Start a new section if the number has a different count of set bits
            else:
                # If the smallest number in the current section is less than the largest in the previous section, return False
                if curMin < prevMax:
                    return False
                # Update the previous section's maximum and reset current section bounds
                prevMax = curMax
                curMin, curMax = n, n
        # Ensure the last section is larger than the previous section
        return curMin > prevMax