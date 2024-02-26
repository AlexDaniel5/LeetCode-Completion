## General Information
Name: Alex Daniel
Date: February 23, 2024

### To Run
- python findCheapestPrice.py

### Results
Speed: 182ms and beats 19.82% of users
Memory: 13.00 MB and beats 78.86% of users

### Description
Set all nodes to infinity initially, indicating that they are unreachable. Then, set the source node to 0 as it marks our starting point. To maintain consistency across iterations, create a temporary prices array. This approach ensures that the original prices from the previous iteration are considered, preventing premature updates that might impact subsequent calculations.

Iterate through all possible options within k stops, calculating prices for traveling to any reachable destination. The resulting prices array will contain the cost of reaching each node. Finally, return the price to reach the destination node.

### LeetCode Description
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.