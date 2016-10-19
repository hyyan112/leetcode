# coding=utf-8
"""
Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s1 = []
        s2 = []
        r3 = []
        for i in num1:
            s1.append(ord(i) - 48)
        for i in num2:
            s2.append(ord(i) - 48)

        l = max(len(s1), len(s2))
        f = 0
        for i in range(l):
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            r = x + y + f
            if r >= 10:
                f = 1
                r -= 10
            else:
                f = 0
            r3.append(r)
        if f:
            r3.append(f)
        r3.reverse()
        return ''.join(map(str, r3))
