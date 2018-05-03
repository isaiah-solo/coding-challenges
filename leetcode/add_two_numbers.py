# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        total = ListNode(0)
        current = ListNode(0)
        current.next = total
        carry = 0
        
        while l1 or l2:
            work = carry
            work += l1.val if l1 else 0
            work += l2.val if l2 else 0
            
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            
            current.next = current.next or ListNode(0)
            current.next.val = math.floor(work % 10)
            current = current.next
                
            carry = math.floor(work / 10)
        
        current.next = ListNode(carry) if carry > 0 else None
        
        return total
