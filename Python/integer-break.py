# encoding:utf-8
"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.

===============================
在n=4->n=10的演算中可以判断出,将数分解为3即可得到最大乘积
只要n>4,就继续减下去,因为如果此时n=4,再减3就余1,乘积肯定就不是最大的了
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2

        result = 1
        while n > 4:
            n -= 3
            result *= 3
        result *= n
        return result
