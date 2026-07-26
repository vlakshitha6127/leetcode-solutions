class Solution(object):
    def splitListToParts(self, head, k):
        # Step 1: Count the number of nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Step 2: Calculate base size and extra nodes
        base = n // k
        extra = n % k

        ans = []
        curr = head

        # Step 3: Split into k parts
        for i in range(k):
            if curr is None:
                ans.append(None)
                continue

            ans.append(curr)

            # Size of current part
            size = base
            if extra > 0:
                size += 1
                extra -= 1

            # Move to the last node of this part
            for _ in range(size - 1):
                curr = curr.next

            # Cut the list
            nextPart = curr.next
            curr.next = None
            curr = nextPart

        return ans