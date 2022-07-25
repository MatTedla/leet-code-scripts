# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Takes linked list and sorts it in ascending order.
        
        :param head: Head of the linked list to be sorted
        """
        # base case: if there is no head - None is returned
        # base case: if the next element after head is None, then the list only has one
        # element and is therefore already sorted - head is returned
        if not head or not head.next:
            return head
        
        # split the list into two halves
        left: Optional[ListNode] = head
        right: Optional[ListNode] = self.getMid(head)
        tmp: Optional[ListNode] = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Returns the back half of a given linked list, from its midpoint to the last node
        
        :param head: Head of the linked list to be sorted
        """
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head.next
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Combines the two parameter linked lists into one linked list
        
        param list1: First half of given linked list
        param list2: Second/back half of given linked list
        """
        # variables dummy and tail now refer to the same beginning ListNode()
        # even if tail changes value, dummy will still refer to the beginning of the list
        dummy: ListNode
        tail: ListNode
        dummy = tail = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
        