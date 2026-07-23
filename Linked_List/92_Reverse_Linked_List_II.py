class Solution:
    def reverseBetween(self, head, left, right):

        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        # Reach the left position
        for i in range(left - 1):
            prev = curr
            curr = curr.next

        left_prev = prev      # Node before left
        left_node = curr      # First node of sublist

        prev = None

        # Reverse from left to right
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Reconnect
        left_prev.next = prev
        left_node.next = curr

        return dummy.next