class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inord(cur, ans):
            if not cur:
                return
            inord(cur.left, ans)
            ans.append(cur.val)
            inord(cur.right, ans)

        inord(root, ans)
        return ans

