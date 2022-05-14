# Complexity
#     Time: O(n)
#     Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if not list1 and not list2:
            return head
        
        list_merged = []
        while list1 or list2:
            cur = 0
            if list1 and list2:
                if list1.val < list2.val:
                    cur = list1.val
                    list1 = list1.next
                else:
                    cur = list2.val
                    list2 = list2.next
            elif list1:
                cur = list1.val
                list1 = list1.next
            else:
                cur = list2.val
                list2 = list2.next
                    
            if list_merged:
                list_merged.next = ListNode(cur, None)
                list_merged = list_merged.next
            else:
                list_merged = ListNode(cur, None)
                head = list_merged
                
        return head
