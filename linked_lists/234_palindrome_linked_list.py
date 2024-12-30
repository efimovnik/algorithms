# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a 
# palindrome
#  or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            next_val = slow.next
            slow.next = prev
            prev = slow
            slow = next_val
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        
# time: O(n)
# space: O(1)