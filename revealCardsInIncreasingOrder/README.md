## General Information
Name: Alex Daniel

Date: April 10, 2024

### To Run
- python deckRevealedIncreasing.py

### Results
Speed: 19 ms and beats 97.44% of users
Memory: 11.95 MB and beats 38.46% of users

### Description
I had hoped to find a more elegant solution, but I opted for a straightforward approach that mimics the simulation process, which I believe is the intended solution. Firstly, create a double-ended queue containing indices up to the length of the deck. Then, for each iteration, take the first index from the queue and add the corresponding deck value to the result array. After that, move the next index to the end of the queue. Repeat this process until we exhaust the entire deck.

### LeetCode Description
You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

    Take the top card of the deck, reveal it, and take it out of the deck.
    If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
    If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.

# Topics
- Array
- Queue
- Sorting
- Simulation