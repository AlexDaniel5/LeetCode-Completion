Name: Alex Daniel
Date: January 29, 2024

To Run:
- python stackAsQueue.py

Description:
This Python program is quite straightforward and serves as a simple implementation for a daily coding challenge. It utilizes the
built-in deque functions to create a stack. Initially, my approach involved treating it as a queue by using pop() on every element
except the last one and then returning the last popped element. This is also required peek to return the last element instead of the first.
However, this strategy did not yield the expected results for some reason. Instead, we're creating a stack which still passes the tests.

LeetCode Description:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal
queue (push, peek, pop, and empty).

Implement the MyQueue class:

    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.
