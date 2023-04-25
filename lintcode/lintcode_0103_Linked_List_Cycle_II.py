class Solution:
  def detectCycle(self, head):
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        if fast is None or fast.next is None:
            return None

        while head and slow:
            if head == slow:
                return head

            head = head.next
            slow = slow.next
