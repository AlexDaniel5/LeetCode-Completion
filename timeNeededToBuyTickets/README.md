## General Information
Name: Alex Daniel
Date: April 9, 2024

### To Run
- python timeRequiredToBuy.py

### Results
Speed: 13 ms and beats 93.75% of users
Memory: 11.53 MB and beats 82.03% of users

### Description
We don't need to fully simulate the problem; instead, we can solve it efficiently in one iteration. By leveraging the value of the person at index k, we compare it with every person in the array, including person k. If a person's value is greater than or equal to that of person k, we add person k's value to the result since they will spend as much time getting a ticket as person k before the simulation concludes. Otherwise, we simply add the person's value to the result, considering that the simulation will continue after they finish getting their ticket. Additionally, we must check one more condition within this loop: if a person with a greater value than person k buys a ticket and they are positioned after person k in the line, we need to subtract one second from the result as that person will be cut short due to the simulation ending.

### LeetCode Description
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

# Topics
- Array
- Queue
- Simulation