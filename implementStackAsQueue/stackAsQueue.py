from collections import deque

class MyQueue(object):

    # Create an object of a class with a deque attribute
    def __init__(self):
        self.q = deque()

    # Add an item to the end of the list
    def push(self, x):
        self.q.append(x)
        
    # Pops the left-most element of the list
    def pop(self):
        return self.q.popleft()
        
    # Returns the leftmost value
    def peek(self):
        return self.q[0]
        
    # Check if the queue is empty
    def empty(self):
        return len(self.q) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Simulation of example 1
myQueue = MyQueue()
print(myQueue.push(1))  # Output: None
print(myQueue.push(2))  # Output: None
print(myQueue.peek())   # Output: 1
print(myQueue.pop())    # Output: 1
print(myQueue.empty())  # Output: False