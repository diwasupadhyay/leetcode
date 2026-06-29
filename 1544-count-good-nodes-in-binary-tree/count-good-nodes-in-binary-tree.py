# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_so_far: int) -> None:
            if node is None:
                return
            if node.val >= max_so_far:
                nonlocal good_node_count
                good_node_count += 1
                max_so_far = node.val
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        good_node_count = 0
        dfs(root, float('-inf'))
      
        return good_node_count