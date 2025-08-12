# DSA problems

This repository contains Data Structures and Algorithms (DSA) problems that I took from the AI and solved it.

Each problem includes:

- A clear description

- Input/output examples

- My Python solution

- Basic test cases
------------------------------------------------------------------------------------------------------------------------------------
# DAY 1:

1- problem 1: Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

example: 

Input: [[1,3],[2,6],[8,10],[15,18]]  

Output: [[1,6],[8,10],[15,18]]

2- problem 2: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

example: 

Input: [100, 4, 200, 1, 3, 2] 

Output: 4

------------------------------------------------------------------------------------------------------------------------------------
# DAY 2:

1- problem 3: Given an integer array nums and an integer k, return the k most frequent elements.

example: 

Input: nums = [1,1,1,2,2,3], k = 2   

Output: [1,2]

------------------------------------------------------------------------------------------------------------------------------------
# DAY 3:

1- problem 4: You are given an integer array coins representing coin denominations, and an integer amount representing a total amount of money. Return the minimum number of coins needed to make up that amount. If it is not possible, return -1.

example: 

Input: coins = [1, 2, 5], amount = 11  

Output: 3 , Explanation: 11 = 5 + 5 + 1

2- problem 5: Given a 2D grid of '1's (land) and '0's (water), count the number of islands. An island is formed by connecting adjacent '1's horizontally or vertically (not diagonally). You may assume the grid is surrounded by water ('0's).

example: 

Input: grid = [ ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
              ]                                    
              
Output: 3

------------------------------------------------------------------------------------------------------------------------------------
# DAY 4:

1- problem 6: Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

example: 

Input: nums = [1, 1, 1], k = 2  

Output: 2

2- problem 7: Given a string containing digits from 2 to 9, return all possible letter combinations that the number could represent. Each digit maps to letters like on a phone keypad.

example: 

Input: digits = "23"

Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

------------------------------------------------------------------------------------------------------------------------------------
# DAY 5:

1- problem 8: Given a string s, return the longest palindromic substring in s.

example: 

Input: s = "babad"

Output: "bab"

(Note: "aba" is also valid)

2- problem 9: You’re given an array of integers temperatures, where temperatures[i] is the temperature on day i. Return an array answer such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature. If there’s no future day where this happens, put 0 instead.

NOTE: RUNTIME must be O(n), not O(n²)

example: 

Input:  temperatures = [73,74,75,71,69,72,76,73]

Output: [1, 1, 4, 2, 1, 1, 0, 0]

------------------------------------------------------------------------------------------------------------------------------------
# DAY 6:

1- problem 10: Given two strings s and t, return the minimum window in s which will contain all the characters in t.

example: 

Input: s = "ADOBECODEBANC", t = "ABC"  

Output: "BANC"

------------------------------------------------------------------------------------------------------------------------------------
# DAY 7:

1- problem 11: Given a string s, find the length of the longest substring without repeating characters.

example: 

Input: s = "abcabcbb"

Output: abc

Explanation: The answer is "abc", with length 3.

2- problem 12: Given a string s, return the index of the first non-repeating character.

example: 

Input: s = "leetcode"

Output: 0

3- problem 13: You are given a list of integers. Your task is to find the two numbers whose sum is closest to zero and return them.

example: 

Input: [-8, -66, -60]

Output: (-60, -8)

------------------------------------------------------------------------------------------------------------------------------------
# DAY 8:

1- problem 14: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

example: 

Input: nums = [2, 7, 11, 15], target = 9  

Output: [0, 1]

2- problem 15: Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.

example: 

Input: s = "eceba", k = 2  

Output: 3  

Explanation: "ece" has length 3 and only two distinct characters: 'e' and 'c'.

3- problem 16: Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

example: 

Input: root =         

                      1
                     / \                   
                    2   3
                     \
                      4


Output: [[3],[9,20],[15,7]]

------------------------------------------------------------------------------------------------------------------------------------
