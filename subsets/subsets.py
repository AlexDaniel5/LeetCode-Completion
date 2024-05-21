class Solution(object):
    def subsets(self, nums):
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(list(subset))
                return
            # Include number
            subset.append(nums[i])
            dfs(i + 1)
            # Dont't include number
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return result

print(Solution().subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]