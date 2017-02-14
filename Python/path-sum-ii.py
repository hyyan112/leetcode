"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
==========
为了省时,采用同一个path而不是每条路线都实例化一个path
由于list是mutable的,所以每经历过一个节点后要将自己从path中剔除
需要注意的是加到result里的path需要新实例化,不然在pop后都空掉的
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        self.count(root, sum, path, result)
        return result

    def count(self, root, target, path, result):
        if not root:
            return False
        path.append(root.val)
        if sum(path) == target and not root.left and not root.right:
            result.append(list(path))
        else:
            self.count(root.left, target, path, result)
            self.count(root.right, target, path, result)
        path.pop(len(path) - 1)
