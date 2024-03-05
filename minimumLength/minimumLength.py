class Solution(object):
    def minimumLength(self, s):
        if len(s) == 1:
            return 1
        start = 0
        end = len(s) - 1
        # Check matching ending and starting characters
        while start < end and s[start] == s[end]:
            letter = s[start]
            start += 1
            end -= 1
            # Remove matching prefix character
            while start <= end and s[start] == letter:
                start += 1
            # Remove matching suffix character
            while end > start and s[end] == letter:
                end -= 1
        return end + 1 - start # Add one since an index starts at 0
        

solution = Solution()
print(solution.minimumLength("cabaabac")) # 0
print(solution.minimumLength("aabccabba")) # 3
print(solution.minimumLength("abbba")) # 0 Outer loop won't stop on odd ending character count