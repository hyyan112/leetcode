# coding=utf-8
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language

=======
给一个数n,计算从0到n每个数的二进制中有几个1
稍加演算便能发现一个规律

number      # of 1's
1             1
2             1
3=2+1         2
4             1
5=4+1         2
6=4+2         2
7=4+3         3
8             1
9=8+1         2
10=8+2        2
11=8+3        3
12=8+4        2
13=8+5        3

"""

"""
正向算

class Solution(object):
    def countBits(self, num):
        res = [0] * (num + 1)
        before = pow2 = 1
        for i in xrange(1,num + 1):
            if i == pow2:
                before = res[i] = 1
                pow2 <<= 1
            else:
                res[i] = res[before] + 1
                before += 1
        return res

"""

"""
逆向算
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
