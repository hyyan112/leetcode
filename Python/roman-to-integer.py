# encoding:utf-8
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
==============
将罗马数字转为整数
"""
d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res
