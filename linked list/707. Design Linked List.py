class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self._head = ListNode()
        self._count = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if 0 <= index < self._count:
            cur = self._head
            for i in range(0, index+1):
                cur = cur.next
            return cur.val
        else:
            return -1
            
    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return
        
        # cur = self._head
        # for i in range(0, index):
        #     cur.next
        # tep = cur.next
        # cur.next = ListNode(val = val, next = tep)
        # self._count += 1
        
        self._count += 1
        add_node = ListNode(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node
        
    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # if 0 <= index < self._count:
            # cur = self._head
            # for i in range(0, index):
            #     cur.next
            # cur.next = cur.next.next
        
        if 0 <= index < self._count:
            # 计数-1
            self._count -= 1
            prev_node, current_node = None, self._head
            for _ in range(index + 1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
