# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        traversal = [root.val]
        if root.left:
            traversal[0:0] = self.inorderTraversal(root.left)
        if root.right:
            traversal.extend(self.inorderTraversal(root.right))
        return traversal
