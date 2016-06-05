# coding=utf-8


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
