class Solution:
    def rearrangeArray(self, nums):
        length = len(nums)
        # Initialize the answer array with zeros to prevent index out of range issues
        ans = [0] * length
        posIndex = 0
        negIndex = 1
        # Iterate through the input array and rearrange positive and negative numbers
        for i in range(length):
            if nums[i] > 0:
                ans[posIndex] = nums[i]
                posIndex += 2
            else:
                ans[negIndex] = nums[i]
                negIndex += 2
        return ans
        
solution = Solution()
array = [3, 1, -2, -5, 2, -4]
print(solution.rearrangeArray(array))