"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
====================
给一个二叉树,找出是否有root-leaf的路线满足sum
有个坑就是注意leaf的定义,即没有子节点的节点,所以sum满足后还要判断左右节点为空
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.count(root, sum, 0)

    def count(self, root, sum, temp):
        if not root:
            return False
        else:
            temp += root.val
            if temp == sum and not root.left and not root.right:
                return True
            return self.count(root.left, sum, temp) or self.count(root.right, sum, temp)
