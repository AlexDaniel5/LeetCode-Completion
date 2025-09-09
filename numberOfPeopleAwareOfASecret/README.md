## General Information
Name: Alex Daniel

Date: September 9, 2025

### To Run
- python peopleAwareOfASecret.py

### Results
Speed: 0 ms and beats 100.00% of users
Memory: 12.54 MB and beats 37.14% of users

### Description
This code uses dynamic programming to track how many people learn the secret each day. It updates a running total of sharers, adding those who are now allowed to share and removing those who have forgotten. Finally, it sums the number of people who learned the secret within the last forget days to get the total number still aware.

### LeetCode Description
On day 1, one person discovers a secret.

You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.

### Topics
- Dynamic Programming
- Queue
- Simulation