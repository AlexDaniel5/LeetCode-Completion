class Solution(object):
    def intToRoman(self, num):
        symList = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400],
                    ["C", 100], ["XC", 90], ["L", 50], ["XL", 40],
                    ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        roman = ""
        for sym, val in symList:
            if num >= val:
                roman += sym * (num//val)
                num %= val
        return roman
    
print(Solution().intToRoman("MCMXCIV")) # 1994, great book by the way