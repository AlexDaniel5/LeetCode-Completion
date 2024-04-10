from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        length = len(deck)
        result = [None] * length # Initalize indexes as empty
        indices = deque(range(length)) # Initalize a double-ended queue with numbers 0 to length - 1
        i = 0
        while indices:
            # Add the card to the result array with the correct index
            currIndex = indices.popleft()
            result[currIndex] = deck[i]
            i += 1
            if indices: # Check this to avoid an error on the last loop
                indices.append(indices.popleft()) # Put the next index to the end of the loop
        return result

print(Solution().deckRevealedIncreasing([17,13,11,2,3,5,7])) # [2,13,3,11,5,17,7]