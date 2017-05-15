#Python code to print a list in reverse... Giving only the function here.

def ReversePrint(head):

  #Base case bail-out... If list is empty or if we have reached the end of the list
  if head == None:
    return
  
  #Now we recursively call the function to basically put the nodes into the stack...
  ReversePrint(head.next)

  #While leaving the stack, simply print the node...
  print (head.data)
