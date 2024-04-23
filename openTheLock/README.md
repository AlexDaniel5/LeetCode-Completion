## General Information
Name: Alex Daniel
Date: April 22, 2024

### To Run
- python openLock.py

### Results
Speed: 623 ms and beats 57.78% of users
Memory: 12.66 MB and beats 50.37% of users

### Description
First, we check the special case that the deadend isn't 0000, which would prevent the computer from making any moves. Then, we create a set with the deadends as preset values. This set will contain any combination tested for being the target, thus avoiding testing it twice later on or falling into infinite loops of adding one and subtracting one from a combination. In a while loop, we remove an element from the queue and check if it matches the target. We then add any combinations that could be created from the lock while ensuring to increment the turn count and add it to the visited list. For any lock, we can generate 8 different locks from it: four by adding one to each digit and four by subtracting one from each digit. We simulate these possibilities in a function called children. Two important things to note in this function are that we use mod 10 to ensure the digit doesn't become two digits and for subtraction, we add 10 after subtracting one. The reason for this is that if we subtracted one from 0, it would become -1, and modding ten would leave it as -1, which is not desired. However, by adding 10 and then subtracting 1, we get 9 instead, which is a convenient workaround. If we've emptied the queue, it means reaching the target is impossible. Thus, we return -1 in that case.

### LeetCode Description
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

### Topics
- Array
- Hash Table
- String
- Breadth-First Search