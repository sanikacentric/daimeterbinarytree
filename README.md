# 🌳 Diameter of Binary Tree

Python solution for finding the diameter (longest path between any two nodes) of a binary tree using DFS.

## 🎯 Problem

Given the root of a binary tree, return the length of the diameter — the longest path between any two nodes (may or may not pass through the root).

## 💡 Approach

- **DFS Post-Order** — O(n) time, compute height while tracking max diameter
- - At each node: diameter = left_height + right_height
 
  - ## 🛠️ Tech Stack
 
  - - **Language**: Python
    - - **Category**: Trees, DFS
      - - **Difficulty**: Easy (LeetCode #543)
       
        - ## 📄 License
       
        - This project is open source and available for educational purposes.
