# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Takes two non-empty linked lists, each containing digits of a non-negative integer 
        stored in reverse order, and returns their sum as a linked list. 
        
        :param l1: first linked list representing a non-negative integer
        :param l1: second linked list representing a non-negative integer
        :return: the linked list representing the sum of the two parameter integers
        """
        
        # Flip list1 and list2
        flip_l1: Optional[ListNode] = self.flip(l1)
        flip_l2: Optional[ListNode] = self.flip(l2)
        
        # Merge digits of each list to make two distinct int values
        l1_int: int = self.merge_digits(flip_l1)
        l2_int: int = self.merge_digits(flip_l2)
        
        # Get sum of ints, split the digits of that sum into a new linked list
        my_sum: int = l1_int + l2_int
        my_sum_list: Optional[ListNode] = self.split_digits(my_sum)
        
        # Return the flipped version of that new linked list
        return self.flip(my_sum_list)
    
        
    def flip(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses the order of the nodes within a given linked list
        
        :param head: linked list that will have its nodes reversed
        :return: the flipped linked list
        """
      
        # set up head_flip and dummy so they have the same pointer
        head_flip: Optional[ListNode]
        dummy: Optional[ListNode]
        head_flip = dummy = ListNode()
        
        # assign linked list that has same length as parameter list
        head_flip.next = self.new_linked_list(self.linked_list_length(head))
        head_flip = head_flip.next

        while head:
            node: Optional[ListNode] = self.get_last(head)
            head_flip.val = node.val
            
            if not head_flip.next:
                break
            else:
                head_flip = head_flip.next
                self.last_node_none(head)
        
        return dummy.next
    
    
    def get_last(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Retrieves last index containing a non-None type value in a given linked list
        
        :param head: linked list that will have its last index w/ non-None value retreived
        :return: the last index within a linked list that is not None value
        """
        
        while head:
            if not head.next:
                return head
            else:
                head = head.next
        
        return None
    
    
    def last_node_none(self, head: Optional[ListNode]):
        """
        Assigns None to the last node with a non-None type value in a given linked list.
        Does not work if linked list only has one node.
        
        :param head: the linked list that will have its last non-None type node removed
        """
        
        while head:
            if not head.next:
                break
            elif not head.next.next:
                head.next = None
                break
            else:
                head = head.next
        
        
    def new_linked_list(self, num: int) -> Optional[ListNode]:
        """
        Creates linked list with a specified number of nodes
        
        :param num: number of nodes within new linked list
        :return: the linked list with n nodes
        """
    
        if num <= 0:
            print("Please enter positive integer.")
        elif num == 1:
            return ListNode()
        else:
            return ListNode(0, next = self.new_linked_list(num - 1))
        
        
    def linked_list_length(self, head: Optional[ListNode]) -> int:
        """
        Finds number of nodes within given linked list
        
        :param head: linked list that will have its nodes counted
        :return: number of nodes contained within linked list
        """
        
        count: int = 0
        
        while head:
            count += 1
            head = head.next
        
        return count
        
    
    def merge_digits(self, digit_list: Optional[ListNode]) -> int:
        """
        Combines a linked list representing an integer, with each node storing a digit
        
        :param digit_list: the linked list that will have its nodes combined
        :return: the integer created after combining the nodes
        """
        
        digit_str: str = ""
        
        while True:
            digit_str += str(digit_list.val)
            
            if not digit_list.next:
                break
            else:
                digit_list = digit_list.next
        
        return int(digit_str)
        
        
    def split_digits(self, num: int) -> Optional[ListNode]:
        """
        Seperates digits of a given int into a linked list
        
        :param num: the number that will be split into a linked list
        :return: the linked list with each node containing a single digit of given number
        """
        
        num_str: str = str(num)
        num_length: int = len(num_str)
        
        digit_list: Optional[ListNode]
        dummy: Optional[ListNode]
        
        digit_list = dummy = ListNode()
        digit_list.next = self.new_linked_list(num_length)
        digit_list = digit_list.next
        
        for i in range(num_length):
            digit_list.val = int(num_str[i])
            
            if digit_list.next:
                digit_list = digit_list.next
            
        return dummy.next
