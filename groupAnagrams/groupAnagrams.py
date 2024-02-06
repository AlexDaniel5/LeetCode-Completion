class Solution(object):
    def groupAnagrams(self, strs):
        # Dictionary
        anagramGroups = {}
        for string in strs:
            # items() returns a key-value pair
            # Dictionarys won't be considered equal if there keys aren't stored in the same order, thus we sort based on keys
            # We use tuple() to convert the dictionary into a hashable value so we can compare it to other dictionaries
            charCount = tuple(sorted(self.charFrequency(string).items()))
            # If there's a string with the same amount of characters add it to the dictionary
            if charCount in anagramGroups:
                anagramGroups[charCount].append(string)
            # Create a new instance in the dictionary otherwise
            else:
                anagramGroups[charCount] = [string]
        # values() to not print the keys (character count) and list() to put the information into a list format; no dict_values printed
        return list(anagramGroups.values())
    
    def charFrequency(self, string):
        charCount = {}
        for char in string: 
            # For the get method we're getting the value of the key char, if it doesn't have a value
            # It's default value will be 0, then add one to that value and set that to the key
            charCount[char] = charCount.get(char, 0) + 1
        return charCount
        
# To test
solution = Solution()

strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs1))