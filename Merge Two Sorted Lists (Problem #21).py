# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two linked lists into one sorted list
        
        :param list1: First linked list to be merged
        :param list2: Second linked list to be merged
        """
        
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
        
        # if there are still values in either list1 or list2
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
        