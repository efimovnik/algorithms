# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]
 


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: If the list is empty or only one node, or no reversal needed
        if not head or left == right:
            return head

        # Step 1: Create a dummy node to simplify edge case handling
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 2: Move `prev` to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Step 3: Start the reversal process
        # `start` is the first node in the segment to be reversed
        # `then` is the node after `start` that will be moved during reversal
        start = prev.next
        then = start.next

        # Reverse the sublist between `left` and `right`
        for _ in range(right - left):
            # Move `then` to the front of the reversed segment
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        # Step 4: Return the updated list
        return dummy.next

# time: O(n)
# space: O(1)