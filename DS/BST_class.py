# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:29:37 2021

@author: Sagar.Agrawal
"""

#Creating a node Class that represent a single node of BST
class Node :
  def __init__(self , value) :
    self.left_child = None
    self.right_child = None
    self.value = value


class BSTOperations : 

  def BST_height(self,root_node):
    """
    Reference : https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
    """
    if root_node is None :
      return 0 
    else :

      left_height = self.BST_height(root_node.left_child)
      right_height = self.BST_height(root_node.right_child)

      if left_height > right_height:
        return left_height + 1
      else :
        return right_height + 1


  def BST_Nodes_at_given_Level(self,root_node, level):
    if root_node is None:
      return
    if level == 1 :
      print(root_node.value , end = ' ')
    elif level > 1:
      self.BST_Nodes_at_given_Level(root_node.left_child , level - 1)
      self.BST_Nodes_at_given_Level(root_node.right_child , level - 1)

  # Function to  print level order traversal of tree
  def BST_level_order_traversal(self,root_node ):
      h = self.BST_height(root_node)
      for i in range(1, h+1):
          print("{" , end = ' ')
          self.BST_Nodes_at_given_Level(root_node, i)
          print('}', end = ' ')

  def BST_insertion(self,root_node , value):
    if root_node is None :
      return (Node(value))
    else :
      if root_node.value == value :
        return root_node
      elif root_node.value < value :
        root_node.right_child = self.BST_insertion(root_node.right_child,value)
      else :
        root_node.left_child = self.BST_insertion(root_node.left_child,value)
    return (root_node)
    

  def BST_insertion_print(self,root_node ,value):
    root_node = self.BST_insertion(root_node , value)
    self.BST_level_order_traversal(root_node)
    return root_node


  ## Deletion 

  def minimumValueNode(self,root_node):
    """
    This is quite simple. Just traverse the node from root to left recursively until left is NULL. 
    The node whose left is NULL is the node with minimum value
    """
    current = root_node
 
    # loop down to find the leftmost leaf
    while(current.left_child is not None):
        current = current.left_child
 
    return current

  def BST_deletion(self,root_node,value):
    if root_node is None :
      return None

    # If the value is smaller than the root_node's value then it lies in  left subtree
    if value < root_node.value:
      root_node.left_child = self.BST_deletion(root_node.left_child, value)
    
    # If the value is larger than the root_node's value then it lies in  right subtree
    elif value > root_node.value:
      root_node.right_child = self.BST_deletion(root_node.right_child, value)
    # If value is same as root_node's value, then this is the node to be deleted
    else :
      
      # Deleting node with only one or No Child 
      if root_node.left_child is None:
        temp = root_node.right_child
        root_node = None
        return temp

      elif root_node.right_child is None:
        temp = root_node.left_child
        root_node = None
        return temp

      # Nodes with two children: 
      # First we get the inorder successor (smallest in the right subtree)
      temp = self.minimumValueNode(root_node.right_child)

      # Next we replace the content of node with the value of inorder successor
      root_node.value = temp.value

      # Delete the inorder successor
      root_node.right_child = self.BST_deletion(root_node.right_child, temp.value)
    return root_node

  def BST_deletion_print(self ,root_node,value):
    root_node = self.BST_deletion(root_node,value)
    self.BST_level_order_traversal(root_node)
    return root_node

  ## Searching

  def BST_search(self,root_node,value):
    
    if root_node is None or root_node.value == value :
      return root_node
    elif value < root_node.value:
      return self.BST_search(root_node.left_child,value)
    else :
      return self.BST_search(root_node.right_child,value)
      
  def Node_depth(self,root_node, data, level = 1):
      if (root_node == None):
          return 0
  
      if (root_node.value == data):
          return level
  
      downlevel = self.Node_depth(root_node.left_child,
                              data, level + 1)
      if (downlevel != 0):
          return downlevel
  
      downlevel = self.Node_depth(root_node.right_child,
                              data, level + 1)
      return downlevel


  def BST_Nodes_at_level(self,root_node,level,nodes):
    if root_node is None :
      return
    if level == 1:
      nodes.append(root_node.value)
    elif level > 1:
      self.BST_Nodes_at_level(root_node.left_child , level - 1,nodes)
      self.BST_Nodes_at_level(root_node.right_child , level - 1,nodes)

  def BST_search_print(self,root_node,value):

    all_nodes = []
    # First Check if the value is present in BST
    if self.BST_search(root_node,value) is None:
      print("Element not found : Level = -1 , Position = -1 ")
      return
    
    #If the element if found , lets find the depth of element from root node
    depth = self.Node_depth(root_node,value)

    # Now let us find all nodes at that depth
    self.BST_Nodes_at_level(root_node,depth,all_nodes)
    print("#########################")
    print(f"Element {value} is found at Level = {depth - 1} , Position = {all_nodes.index(value) + 1}")


if __name__ == "__main__":
    
    flag = 1
    print("#############################################")
    print("Binary Search Tree implementation Using Class")
    print("#############################################")
    
    root = None
    bst = BSTOperations()
    
    while (flag):
        print()
        print()
        print()
        print("Enter one of the following options :")
        print()
        print("Press 1 to Insert an element to BST ")
        print("Press 2 to Delete element from BST ")
        print("Press 3 to Search an element in BST ")
        print("Press 4 to Print BST (Level Order) ")
        print("Press 0 to Exit")
        
        choice = int(input())
        
        if choice == 1:
            element = int(input("Enter the element to be inserted : "))
            root = bst.BST_insertion_print(root,element)
            
        elif choice == 2:
            element = int(input("Enter the element to be deleted : "))
            root = bst.BST_deletion_print(root,element)
            
        elif choice == 3:
            element = int(input("Enter the value to be searched : "))
            bst.BST_search_print(root,element)
            
        elif choice == 4:
            print("BST ( Level Order ) : ")
            bst.BST_level_order_traversal(root)
        elif choice == 0:
            print("Thank You !")
            flag = 0
        else :
            print("! Invalid Input")
