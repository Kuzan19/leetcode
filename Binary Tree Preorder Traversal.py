class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inord(cur, ans):
            if not cur:
                return
            ans.append(cur.val)
            inord(cur.left, ans)
            inord(cur.right, ans)

        inord(root, ans)
        return ans