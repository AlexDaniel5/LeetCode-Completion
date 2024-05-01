class Solution(object):
    def reversePrefix(self, word, ch):
        i = word.find(ch)
        # Character isn't found
        if i == -1:
            return word
        # Reversed prefix concated to the rest of the string
        return word[:i+1][::-1] + word[i+1:]
    
print(Solution().reversePrefix("abcdefd", "d")) # dcbaefd