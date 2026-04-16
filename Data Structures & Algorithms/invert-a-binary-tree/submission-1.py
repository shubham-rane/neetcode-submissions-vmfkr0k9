# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        ans = root
        while len(stack) > 0:
            temp = TreeNode()
            if not root:
                return ans
            
            temp = root.left
            
            root.left = root.right
            root.right = temp
            
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
            root = stack.pop(-1)
        return ans

            
        