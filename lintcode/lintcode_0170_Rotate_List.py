class Solution:
    def rotateRight(self, head, k):
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        if len(stack) == 0:
            return head

        if k > len(stack) and len(stack) > 0:
            k = k % len(stack)

        rotate = stack[len(stack) - k :] + stack[: len(stack) - k]

        for i in range(len(rotate) - 1):
            rotate[i].next = rotate[i + 1]
        rotate[-1].next = None

        return rotate[0]
