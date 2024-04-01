class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        count = 0
        for char in reversed(s):
            if char == " ":
                break
            count += 1
        return count

print(Solution().lengthOfLastWord("   fly me   to   the moon  ")) # 4