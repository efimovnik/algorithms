# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 2130. Maximum Twin Sum of a Linked List
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

# Example 3:
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

# 3 steps solution:
# 1) find the middle with fast & slow pointer
# 2) reverse second half of the list
# 3) traverse through first and second halves and calculate the sum

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find the mid with fast & slow pointers
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse second half of the list
        mid = slow
        prev = None
        while mid:
            next_node = mid.next
            mid.next = prev
            prev = mid
            mid = next_node
        ans = 0
        # calculate sum with 2 pointers
        while prev:
            ans = max(ans, prev.val + head.val)
            prev = prev.next
            head = head.next
        return ans
    
# time: O(3 * n) = O(n)
# space: O(1)