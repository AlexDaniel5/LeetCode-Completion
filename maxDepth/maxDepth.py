class Solution(object):
    def maxDepth(self, s):
        count = 0
        highest = 0
        for char in s:
            if char == "(":
                count += 1
                # Check if it's the highest count has been
                if highest < count:
                    highest = count
            elif char == ")":
                count -= 1
        return highest

print(Solution().maxDepth("(1+(2*3)+((8)/4))+1")) # 3