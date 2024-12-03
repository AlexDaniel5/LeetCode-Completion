class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        searchLen = len(searchWord)
        prefixWord = 1
        i = 0
        prevChar = " "
        for char in sentence:
            # Check if a new word starts and matches the first character of the search word
            if prevChar == " ":
                if char == searchWord[0]:
                    i = 1
                    # Return the word index if the search word is a single character to avoid index errors
                    if searchLen == 1:
                        return prefixWord
                else:
                    i = 0
            # Continue checking characters if they match the search word
            elif i > 0 and char == searchWord[i]:
                i += 1
                if i == searchLen:
                    return prefixWord
            # Reset if the characters don't match the search word
            else:
                i = 0
            # Increment word index when a space is encountered
            if char == " ":
                prefixWord += 1
            prevChar = char
        return -1


print(Solution().isPrefixOfWord("corona dream", "d")) # 2
print(Solution().isPrefixOfWord("hellohello hellohellohello", "ell")) # -1