# -*- coding: utf-8 -*-
"""
Created on Mon May 31 18:49:06 2021

@author: Sagar.Agrawal
"""

import copy
import argparse

def BST_insert(bst_tree , value,parent_index = 0):
  if bst_tree[parent_index] == None or bst_tree[parent_index] == value:
    bst_tree[parent_index] = value
    return bst_tree

  elif bst_tree[parent_index] > value :
    left_child_index = 2*parent_index + 1
    BST_insert(bst_tree , value,left_child_index)
  else :
    right_child_index = 2*parent_index + 2
    BST_insert(bst_tree , value,right_child_index)


def Level_order_traverse(bst_tree):
  i = 0
  bst_tree_copy = copy.deepcopy(bst_tree)
  while bst_tree_copy:
    print('{',end = ' ')
    for index in range(2**i):
      value = bst_tree_copy.pop(0)
      if value : 
        print(value,end = ' ')
    i += 1
    print('}',end = ' ')

def BST_insert_print(bst_tree,value):
  BST_insert(bst_tree , value)
  bst_tree_copy = copy.deepcopy(bst_tree)
  Level_order_traverse(bst_tree_copy)

def BST_Search_index(bst_tree,element) : 
  #First let us find the index of element
  index = 0
  while ((bst_tree[index]!=element) and (bst_tree[index] != None)):

    if (element < bst_tree[index]):
        index = 2 * index + 1
    else :
      index = 2 * index + 2
  return(index)

def BST_deletion(bst_tree,element):

  index = BST_Search_index(bst_tree,element)
  print(index)
  ## Case 1 - Delete leaf node
  if((bst_tree[2*index + 1] == None) and (bst_tree[2*index +2] == None)):
    bst_tree[index] = None

  ## Case 2 - Delete node with one child
  ## if left child is not present
  if ((bst_tree[2*index + 1] == None)):
    bst_tree[index] = bst_tree[2*index +2]
    bst_tree[2*index +2] = None

  ## if Right child is not present
  elif ((bst_tree[2*index + 2] == None)):
    bst_tree[index] = bst_tree[2*index +1]
    bst_tree[2*index +1] = None

  ## Case 3 – Delete node with 2 children
  if ((bst_tree[2*index + 1] != None) and (bst_tree[2*index +2] != None)):
    # First we get the inorder successor (smallest in the right subtree) 
    bst_tree_temp = copy.deepcopy(bst_tree)
    bst_tree_temp.sort(key=lambda x: x or 0) # lambda to avoid None
    tree_root_index = bst_tree_temp.index(element)

    inorder_successor = min([ i for i in bst_tree_temp[tree_root_index + 1 : ] if i is not None])
    inorder_index = BST_Search_index(bst_tree,inorder_successor)
    check_i = inorder_index
    temp = bst_tree[inorder_index]
    bst_tree[index] = temp
    bst_tree[inorder_index] = None

    while bst_tree[2*check_i + 2] or bst_tree[2*check_i + 1]  :

      if bst_tree[2*check_i + 2] :
        temp = bst_tree[2*check_i + 2]
        bst_tree[check_i] = temp
        bst_tree[2*check_i + 2] = None
        check_i = 2*check_i + 2


      elif bst_tree[2*check_i + 1]:
        temp = bst_tree[2*check_i + 1]
        bst_tree[check_i] = temp
        bst_tree[2*check_i + 1] = None
        check_i = 2*check_i + 1
  
def BST_delete_print(bst_tree,value):
  BST_deletion(bst_tree , value)
  bst_tree_copy = copy.deepcopy(bst_tree)
  Level_order_traverse(bst_tree_copy)
  
def BST_search(bst_tree,k):
  print(bst_tree)  
  hash_dict_val = dict()
  for i in range(len(bst_tree)) :
    if bst_tree[i] is not None:
      hash_dict_val[bst_tree[i]] = k - bst_tree[i]
  for i in range(len(bst_tree)):
      if bst_tree[i] is not None and hash_dict_val[bst_tree[i]] in bst_tree :
          print(hash_dict_val[bst_tree[i]],k - hash_dict_val[bst_tree[i]])

  
if __name__ == "__main__":
    
    flag = 1
    print("#############################################")
    print("Binary Search Tree implementation Using Array")
    print("#############################################")
    
    print("Enter height of Binary Search Tree to be created : ")
    height = int(input())
    
    #Size of BST array
    N = 2**height - 1
    
    #Create an empty array for BST
    bst_tree = [None] * N
    
    while (flag):
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
            BST_insert_print(bst_tree, element)
            
        elif choice == 2:
            element = int(input("Enter the element to be deleted : "))
            BST_delete_print(bst_tree, element)
            
        elif choice == 3:
            k = int(input("Enter the K value for elements to be searched : "))
            BST_search(bst_tree,k)
            
        elif choice == 4:
            print("BST ( Level Order ) : ")
            Level_order_traverse(bst_tree)
        elif choice == 0:
            print("Thank You !")
            flag = 0
        else :
            print("! Invalid Input")
 
