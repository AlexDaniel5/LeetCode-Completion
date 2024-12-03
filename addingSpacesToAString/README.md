## General Information
Name: Alex Daniel

Date: Decemeber 3, 2024

### To Run
- python addSpaces.py

### Results
Speed: 148 ms and beats 57.69% of users
Memory: 37.47 MB and beats 100.00% of users
Time complexity: O(N)

### Description
When solving this problem, it's important to note that appending to a list is significantly faster than manipulating a string directly in Python. To optimize performance, we use a list to collect characters and convert it into a string only at the end of the function. The function employs two pointers: one to track when a space should be added and another to keep track of the current character being appended. Whenever the pointer for adding spaces matches the current position specified in the spaces list, a space is added. A character from the input string is appended during each loop iteration. To further improve efficiency, we stop looping through the string once all specified spaces have been processed, appending any remaining characters from the input string in one step.

### LeetCode Description
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

    For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".

Return the modified string after the spaces have been added.

### Topics
- Array
- Two Pointers
- String
- Simulation