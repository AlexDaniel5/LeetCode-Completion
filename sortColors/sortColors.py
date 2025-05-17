class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with low pointer, then move both forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If it's 1, just move mid forward
                mid += 1
            else:
                # Swap current element with high pointer, move high backward
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

print(Solution().sortColors([2,0,2,1,1,0])) # [0,0,1,1,2,2]