# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, next = head)
        fast = dummy
        slow = dummy
        for i in range(n + 1):
            fast = fast.next
        while fast != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(val = 0, next = head)
        cur = dummyHead
        counter = 0
        while(cur.next != None):
            cur = cur.next
            counter += 1
        cur = head
        pre = dummyHead
        for i in range(0, counter - n):
            pre = cur 
            cur = cur.next
        else:
            pre.next = cur.next
            cur.next = None
        return dummyHead.next
