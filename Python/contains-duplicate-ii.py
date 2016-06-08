# coding=utf-8
"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the difference between i and j is at most k.
==========================

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        r = dict()
        for i, item in enumerate(nums):
            if item in r.keys() and i - r[item] <= k:
                return True
            else:
                r[item] = i
        else:
            return False
