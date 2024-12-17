from collections import Counter
import heapq

class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        # Calculate the frequency of each character in the string
        count = Counter(s)
        # Create a max-heap by storing negative ASCII values of characters with their frequencies
        maxHeap = [(-ord(c), cnt) for c, cnt in count.items()]
        # Transform the list into a heap, automatically sorting by frequency and character order
        heapq.heapify(maxHeap)
        res = []

        while maxHeap:
            # Pop the character with the highest frequency (convert ASCII back to character)
            char, cnt = heapq.heappop(maxHeap)
            char = chr(-char)

            curCnt = min(cnt, repeatLimit)
            res.append(char * curCnt)

            # If there are remaining occurrences of the current character
            if cnt - curCnt > 0 and maxHeap:
                # Pop the next character to break consecutive repetition
                nxtChar, nxtCnt = heapq.heappop(maxHeap)
                nxtChar = chr(-nxtChar)
                res.append(nxtChar)

                # Push the next character back into the heap if it still has occurrences
                if nxtCnt > 1:
                    heapq.heappush(maxHeap, (-ord(nxtChar), nxtCnt - 1))
                # Push the current character back into the heap with updated frequency
                heapq.heappush(maxHeap, (-ord(char), cnt - curCnt))
        return "".join(res)

print(Solution().repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1)) # "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba"