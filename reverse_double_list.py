"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if head is None:
        return head
    if head.next is None:
        return head
    prev = None
    curr = head
    
    while curr is not None:
        after = curr.next
        curr.next = prev
        curr.prev = after
        prev = curr
        curr = after
    
    head = prev
    return head
