# coding=utf-8
"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = temp = 0
        j = 1
        l = len(nums)
        while j <= l:
            if j < l and nums[j] - nums[temp] == 1:
                temp = j
                j += 1
            else:
                if i == temp:
                    result.append("{}".format(nums[i]))
                else:
                    result.append("{}->{}".format(nums[i], nums[temp]))
                i = temp = j
                j = i + 1
        return result
