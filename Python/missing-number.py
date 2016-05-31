# encoding:utf-8
"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
======================================
找出包含n个数的由0到n组成的序列中缺少的那个数,位运算比普通求和/减差的方法时间差别不大,可能因为是Python的关系...
贴上普通解法:
class Solution(object):
    def missingNumber(self, nums):
        sum=0
        l=len(nums)
        for i in range(l):
            sum+=i-nums[i]
        return sum+l
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = 0
        l = 0
        while l < len(nums):
            missing ^= l ^ nums[l]
            l += 1
        return missing ^ l
