## General Information
Name: Alex Daniel

Date: October 7, 2024

### To Run
- python areSentenceSimilar.py

### Results
Speed: 5 ms and beats 96.07% of users
Memory: 11.58 MB and beats 80.16% of users

### Description
The main challenge was interpreting the problem rather than solving it. The key point is that a sentence can appear between words of the other sentence, not simply be inserted into it. Essentially, the task is to check whether one sentence can serve as both the prefix and/or suffix of the other. This can be handled with two pointers starting from opposite ends, advancing when matching words are found. Before applying this strategy, it's important to first compare the length of the sentences, since the longer sentence can't fit into the shorter one.

### LeetCode Description
You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,

    s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in s1.
    s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into s1, it is not separated from "Frog" by a space.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

# Topics
- Array
- Two Pointers
- String