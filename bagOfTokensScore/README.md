## General Information
Name: Alex Daniel
Date: March 4, 2024

### To Run
- python bagOfTokensScore.py

### Results
Speed: 31ms and beats 59.26% of users
Memory: 11.74 MB and beats 70.37% of users

### Description
Sort the list to simplify subsequent processes. While the `tokens` list exists, check if `power` is greater than the smallest value. If it is, play the smallest token face up. Otherwise, if the largest token is larger than the smallest token, play the largest token face down and the smallest token face up to provide the user with a bit more power to potentially achieve a higher score.

## Notes
- Sorting the list facilitates easier handling in subsequent steps.
- Checking whether the greatest power is larger than the smallest power might be time-consuming, so it's more efficient to exchange the values, even if they are equal in value.

### LeetCode Description
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

    Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
    Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.

Return the maximum possible score you can achieve after playing any number of tokens.
