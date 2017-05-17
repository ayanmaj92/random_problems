"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""


#########################################################################################
# Technique: We start from the heads of each list. We traverse both together            #
# until we converge at the common node. If we reach the end of any list before that,    #
# we make the current pointer of that list to point to the head of the other list.      #
# NB: This will work either on the 1st iteration of both lists if length of both lists  #
# are same, or on the second iteration. But the thing is we will always meet at the     #
# point of merge. For two lists, say uptil the point of merge the length of one list is #
# X, while for the other it is (X + Δ). Also, let the length from the merge node to the #
# end be Z. Then when we move over to the other lists, the basic traversal will become  #
# equal. So, for list1 it will be X + Z + (X + Δ) = 2X + Z + Δ. For list2, it will be   #
# (X + Δ) + Z + X = 2X + Z + Δ. As can be understood, if Δ is 0, then we do not need    #
# the second iteration. But ultimately, we will always meet at the merge node.          #
#########################################################################################



def FindMergeNode(headA, headB):
    currentA = headA
    currentB = headB
    while (currentA != currentB):
        # for list A
        if currentA.next is None:
            currentA = headB
        else:
            currentA = currentA.next
        # for list B
        if currentB.next is None:
            currentB = headA
        else:
            currentB = currentB.next
    return currentB.data
