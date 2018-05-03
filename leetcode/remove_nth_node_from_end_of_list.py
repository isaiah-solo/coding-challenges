# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def recurse(self, prev, tocheck, n):
    """
    :type prev: ListNode
    :type tocheck: ListNode
    :type n: int
    :rtype: ListNode
    """
        
    # Set current pointer
    current = tocheck
        
    # Check through each node n spots after the node to check
    for i in range(n):
            
      # If exactly n from the end, remove node and return new sequence
      if not current.next:
        prev.next = tocheck.next
        return prev
            
      # Iterate
      current = current.next
        
    # If not found, set the next node as the current node
    prev.next = self.recurse(tocheck, tocheck.next, n)
        
    return prev
    
  def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
        
    # Create placeholder to begin, attached to given linked list
    placeholder = ListNode(0)
    placeholder.next = head
        
    # Start recursion and get result
    result = self.recurse(placeholder, head, n)
        
    return result.next
