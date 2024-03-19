from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        taskCounts = Counter(tasks) # Create a hash map of the counts of every character
        maxCount = max(taskCounts.values()) # Find the task with the largest occurence
        maxOccurrences = list(taskCounts.values()).count(maxCount) # Determine the number of tasks with same number of occurences
        # Formula used to determine runtime
        return max(len(tasks), (maxCount - 1) * (n + 1) + maxOccurrences)
    
print(Solution().leastInterval(["A","C","A","B","D","B"], 1)) # 6
print(Solution().leastInterval(["A","A","A","B","B","B"], 2)) # 8