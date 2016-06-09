# encoding:utf-8
"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
======================
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.reverse(None, head)

    def reverse(self, parent, node):
        n = node.next if node.next else None
        node.next = parent
        if n:
            return self.reverse(node, n)
        else:
            return node
