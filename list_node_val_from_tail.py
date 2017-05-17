#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    node = head
    count = 0
    while (node != None):
        count += 1
        node = node.next
    #print ("Count: ",count)
    position = count - position - 1
    while position != 0 and head.next != None:
        position -= 1
        head = head.next
    return head.data
