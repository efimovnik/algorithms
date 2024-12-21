# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3] 


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None                     # initialize for step 3
        dummy = head.next               # step 5
        while head and head.next:
            if prev: 
                prev.next = head.next   # step 4
            prev = head                 # step 3
            next_node = head.next.next  # step 2
            head.next.next = head       # step 1 
            
            head.next = next_node       # step 6
            head = next_node            # move to the next pair - step 3

        return dummy
    
    # time: O(n)
    # space: O(1)

# 1. Performs an edge swap from A -> B -> C -> ... to A <-> B C -> ....
# 2. Make sure we can still access the rest of the list beyond the current pair (saves C).
# 3. Now that A <-> B is isolated from the rest of the list, save a pointer to A to connect it with the rest of the list later. Move to the next pair.
# 4. Connect the previous pair to the rest of the list. In this case connecting A -> D.
# 5. Use a dummy pointer to keep a reference to what we want to return.
# 6. Handle the case when there's an odd number of nodes.
