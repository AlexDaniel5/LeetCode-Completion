## General Information
Name: Alex Daniel
Date: November 26, 2024

### To Run
- python findChampion.py

### Results
Speed: 7 ms and beats 76.92% of users
Memory: 13.29 MB and beats 8.33% of users

### Description
Iterate through the edges to calculate the count of times each team is weaker than another. Next, traverse the list of teams. If a team has a weaker count of 0, designate it as the champion. Continue checking the remaining teams; if another team also has a weaker count of 0, return -1, as there can only be one champion.

### LeetCode Description
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

Notes

    A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
    A DAG is a directed graph that does not have any cycle.

## Topics
- Graph