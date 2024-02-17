class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            middle = len(word) // 2
            # Check if the character at the end of the word matches the character at the beginning
            for i in range(middle):
                if word[i] != word[-(i + 1)]:
                    break
            # For loop finished without break
            else:
                return word           
        return ""        
        
                    
solution = Solution()
words = ["abc","car","ada","racecar","cool"] #ada
print(solution.firstPalindrome(words))