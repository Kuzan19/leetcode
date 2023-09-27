from typing import Optional

head = [1, 2, 3, 4, 5]
left = 2
right = 4


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        prev, cur = None, head

        if left == right:
            return cur

        for i in range(left - 1):
            prev, cur = cur, cur.next

        connector_node = prev
        tail = cur

        for i in range(left - 1, right):
            next = cur.next

            cur.next = prev
            prev = cur
            cur = next

        tail.next = next

        if connector_node:
            connector_node.next = prev
        else:
            head = prev

        return head


if __name__ == "__main__":
    N = Solution
    print(N.reverseBetween(N, head, left, right))
