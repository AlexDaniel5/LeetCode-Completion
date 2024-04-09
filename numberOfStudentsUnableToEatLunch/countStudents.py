from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        result = len(students)
        count = Counter(students)
        for sandwich in sandwiches:
            # If there is a student of the sandwich type
            if count[sandwich] > 0:
                result -= 1
                count[sandwich] -= 1
            # If there is no student who can eat the sandwich
            else:
                break
        return result
    
print(Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])) # 3