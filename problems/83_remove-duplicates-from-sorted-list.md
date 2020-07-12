## Problem

#### [83. remove-duplicates-from-sorted-list](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)



## Description

Given a sorted linked list, delete all duplicates such that each element appear only *once*.

**Example 1:**

> Input: 1->1->2
>
> Output: 1->2

**Example 2:**

> Input: 1->1->2->3->3
>
> Output: 1->2->3



## Solution：

#### Algorithm

Since the original linked list is a sorted linked list, there is no duplication of unconnected nodes. You only need to compare the current node and the next node in a loop:

1. The current node value is equal to the next node: point the current node to the next after next node, and continue to compare the current node and the next node in the next cycle
2. Unequal: indicating that the current value is not duplicated, and directly points the current node to the next node

#### Code

- [python](../python/problems/83_remove-duplicates-from-sorted-list.py)

#### Complexity

- Time complexity ：O(n)
- Space complexity ：O(1)