# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaves(node: Optional[TreeNode], leaf_values: List[int]) -> None:
            if not node:
                return
            if node.left is None and node.right is None:
                leaf_values.append(node.val)
                return
            if node.left:
                collect_leaves(node.left, leaf_values)
            if node.right:
                collect_leaves(node.right, leaf_values)
        leaves_tree1 = []
        leaves_tree2 = []
        collect_leaves(root1, leaves_tree1)
        collect_leaves(root2, leaves_tree2)
        return leaves_tree1 == leaves_tree2