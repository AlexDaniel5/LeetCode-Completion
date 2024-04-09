## General Information
Name: Alex Daniel
Date: April 8, 2024

### To Run
- python countStudents.py

### Results
Speed: 21 ms and beats 48.80% of users
Memory: 11.35 MB and beats 99.76% of users

### Description
The number of students isn't critical, as each student will eventually have a turn. Therefore, we can tally the quantity of each type of student. Next, we iterate through the array of sandwiches. If we encounter a sandwich type for which there are no corresponding students, we stop the iteration and return.

### LeetCode Description
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

    If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 ### Topics
 - Array
 - Stack
 - Queue
 - Simulation