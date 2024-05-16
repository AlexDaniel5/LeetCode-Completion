class Solution(object):
    def letterCombinations(self, digits):
        result = []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                 "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def combination(combo, digits):
            # Base case
            if not digits:
                result.append(combo)
                return
            # Recursive case
            for letter in phone[digits[0]]:
                combination(combo + letter, digits[1:])
        if digits: # To ensure [""] isn't returned instead of []
            combination("", digits)
        return result
    
print(Solution().letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]