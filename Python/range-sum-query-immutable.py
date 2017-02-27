# coding=utf-8
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
=======
求前N项和,相减即可
"""


class NumArray(object):
    def __init__(self, nums):
        self.n = [0]
        for i in nums:
            self.n.append(self.n[-1] + i)

    def sumRange(self, i, j):
        return self.n[j + 1] - self.n[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
