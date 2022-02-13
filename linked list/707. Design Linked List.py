class ListNode:
    def __init__(val = 0, next = None):
        self.val = val
        self.next = next



class MyLinkedList(object):

    def __init__(self):
        self._head = ListNode(val = 0)
        self._count = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        cur = self._head
        if 0 <= index < self._count:
            for i in range(index + 1):
                cur = cur.next
            return cur.val
        else:
            return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self._head
        if index <= 0:
            cur.val = val
            cur.next = 
        
        
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        

'''
to locate the index:
if the start point is dummy head:
# reach the node ahead of index for delete node in index and add node in index 
for i in range(index):
    cur = cur.next
# reach the node of index for check value of node in index
for i in range(index + 1):
    cur = cur.next

'''

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
