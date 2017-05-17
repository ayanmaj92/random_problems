"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    if data < head.data:
        new_node.next = head
        head.prev = new_node
        head = new_node
        return head
    curr_node = head
    while (curr_node.next is not None and curr_node.next.data < data):
        curr_node = curr_node.next
    new_node.next = curr_node.next
    if curr_node.next is not None:
        curr_node.next.prev = new_node
    curr_node.next = new_node
    new_node.prev = curr_node
    
    return head
