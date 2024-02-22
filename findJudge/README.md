## General Information
Name: Alex Daniel
Date: February 22, 2024

### To Run
- python findJudge.py

### Results
Speed: 673ms and beats 12.82% of users
Memory: 16.90 MB and beats 64.10% of users

### Description
Identify the individual with the highest likability, as they are likely to serve as the judge. In the case of a tie for the highest likability among multiple individuals, return -1 to indicate the absence of a clear judge. Next, compile a list of everyone excluding the potential judge and verify that each person likes presumed judge, if somebody doesn't return -1. If all checks are successful, return the judge's number.

### LeetCode Description
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
