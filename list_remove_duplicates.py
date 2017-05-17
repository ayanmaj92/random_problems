"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head is None:
        return head
    prev = head
    curr = head.next
    while curr != None:
        if prev.data == curr.data:
            curr = curr.next
        else:
            prev.next = curr
            prev = curr
            curr = curr.next
    prev.next = curr
    return head
