# encoding:utf-8
"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
===========================
给一个树,遍历获得所有节点的值

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        temp = []
        while root or temp:
            while root:
                temp.append(root)
                res.append(root.val)
                root = root.left
            root = temp.pop()
            root = root.right
        return res
