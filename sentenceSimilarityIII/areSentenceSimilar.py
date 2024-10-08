class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        s1 = sentence1.split()
        s2 = sentence2.split()
        # Ensure s1 has fewer or equal number of words compared to s2
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        i = 0 # The pointer of the longer string (s2)
        length1 = len(s1)
        # Move the left pointer while the words of both strings match
        while i < length1 and s1[i] == s2[i]:
            i += 1
        lp = i
        i = len(s2) - 1
        rp = length1 - 1
        # Move the right pointer while the words of both strings match
        while i >= lp and rp >= 0 and s1[rp] == s2[i]:
            i -= 1
            rp -= 1
        # If the pointers crossed, all words match
        return lp > rp
    
print(Solution().areSentencesSimilar("hsYZKp Cn eE","hsYZKp eE")) # True