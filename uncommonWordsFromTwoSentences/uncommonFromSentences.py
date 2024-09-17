class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s = s1 + " " + s2
        # Extracts words from a string
        words = s.split()
        wordCount = {}
        # Count the number of each word
        for word in words:
            wordCount[word] = wordCount.get(word, 0) + 1
        # Return an array of words that have a count of one
        return [word for word, count in wordCount.items() if count == 1]

print(Solution().uncommonFromSentences("this apple is sweet","this apple is sour"))