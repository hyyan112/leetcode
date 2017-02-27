# coding=utf-8
"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
=========
设字符串为str，长度为n，p[i][j]表示第i到第j个字符间的子序列的个数（i<=j），则：
状态初始条件：dp[i][i]=1 （i=0：n-1）
状态转移方程：dp[i][j]=dp[i+1][j-1] + 2  if（str[i]==str[j]）
            dp[i][j]=max(dp[i+1][j],dp[i][j-1])  if （str[i]!=str[j]）
"""


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        return self.count(s, 0, len(s) - 1, dp)

    def count(self, s, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            dp[i][j] = self.count(s, i + 1, j - 1, dp) + 2
        else:
            dp[i][j] = max(self.count(s, i + 1, j, dp), self.count(s, i, j - 1, dp))
        return dp[i][j]
