# encoding:utf-8
"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
===============================
后序遍历获得所有节点的值
即优先将右节点的值放入结果集
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = []
        res = []
        while root or temp:
            while root:
                res.insert(0, root.val)
                temp.append(root)
                root = root.right
            root = temp.pop()
            root = root.left
        return res
