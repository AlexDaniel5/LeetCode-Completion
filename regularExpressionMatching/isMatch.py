class Solution(object):
    def isMatch(self, s, p):
        def dfs(i, j):
            # If the results are already in the cache, return
            if (i, j) in cache:
                return cache[(i, j)]
            # We've reached the end of the strings
            if i >= len(s) and j >= len(p):
                return True
            # Exhausted the pattern characters without reaching the end of the string
            if j >= len(p):  
                return False
            # Check if the characters match or if we have the universal period
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            # If we have the asterisk, check the two possibilties of using it or not
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False
        cache = {}
        return dfs(0, 0)
    
print(Solution().isMatch("aaa", "ab*a*c*a")) # True
print(Solution().isMatch("ab", ".*c")) # False