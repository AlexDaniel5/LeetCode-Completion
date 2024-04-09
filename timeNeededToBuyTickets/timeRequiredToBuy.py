class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        cap = tickets[k]
        result = 0
        i = 0
        for ticket in tickets:
            # If the person has a greater value add the person's time at index k
            if ticket >= cap:
                result += cap
                # Person won't a second in the last loop
                if i > k:
                    result -= 1
            # The person will be done before person at index k
            else:
                result += ticket
            i += 1
        return result
    
print(Solution().timeRequiredToBuy([84,49,5,24,70,77,87,8], 3)) # 154