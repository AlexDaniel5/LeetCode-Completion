class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        score = 0
        # While the tokens list exists
        while tokens:
            # If power is greater than the first token play it face up
            if power >= tokens[0]:
                score += 1
                power -= tokens[0]
                tokens.pop(0)
            # Else if the largest token is greater than the smallest token
            # Pop both the largest and smallest token to give the user more power
            elif len(tokens) > 2 and score > 0:
                power += tokens[-1] - tokens[0]
                tokens.pop(0)
                tokens.pop()
            # We've reached maximum score
            else:
                break
        return score

print(Solution().bagOfTokensScore([6,0,39,52,45,49,59,68,42,37], 99)) # 5
print(Solution().bagOfTokensScore([42,10,26,22], 65)) # 3