# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps adjacent nodes of given linked list
        
        :param head: head of linked list to have its nodes swapped
        """
        
        if not head or not head.next:
            return head
        
        dummy: ListNode
        tmp: ListNode
        
        dummy = ListNode
        dummy.next = head
        
        while head and head.next:
            tmp = head.next.val
            head.next.val = head.val
            head.val = tmp
            
            head = head.next.next
        
        return dummy.next