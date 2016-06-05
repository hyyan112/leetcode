# encoding:utf-8
"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
===============================
中序遍历获得所有节点的值
即优先将左节点的值放入结果集
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        temp = []
        res = []
        while root or temp:
            while root:
                temp.append(root)
                root = root.left
            root = temp.pop()
            res.append(root.val)
            root = root.right
        return res
