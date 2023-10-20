class Solution:
    def pred(self, root, ans):

        if not root:
            return

        for i in range(len(root.children)):
            self.pred(root.children[i], ans)
        ans.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.pred(root, ans)
        return ans