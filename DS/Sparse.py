import random
class Sparse:

  # Initialisation
  def __init__(self,rows,columns):

      self.triplet_representation= [[None for _ in range(3)] for _ in range(len(rows))]

      for i , (row , col) in enumerate(zip(rows,columns)):
        self.triplet_representation[i][0] = row
        self.triplet_representation[i][1] = col
        if i == 0:
            # At index 0 of value column , we store the number of non zero elements in sparse matrix
            self.triplet_representation[i][2] = len(rows) - 1
        else :
            self.triplet_representation[i][2] = random.randint(1, 100)
      
      self.triplet_representation = [self.triplet_representation[0],] + sorted(self.triplet_representation[1:], key = lambda x: (x[0],x[1]))
      print("The Triplet representation :")
      print(self.triplet_representation)
      print()
      print()
      print("The Sparse matrix generated is as follows :" )
      self.print_sparse()

  # Print the sparse matrix:
  def print_sparse(self):
    row_size = self.triplet_representation[0][0]
    col_size = self.triplet_representation[0][1]
    
    # Sort the Triplet representation by row column
    data = sorted(self.triplet_representation[1:], key = lambda x: (x[0],x[1]))
    
    row, col , val = data.pop(0)
    for i in range(row_size):
      for j in range(col_size):
        if col == j and row == i:
          print(val,end = " ")
          try :
            row, col , val = data.pop(0)
          except :
            pass
          continue
        else:
          print(0,end = " ")
      print()

  def delete(self,row_del,col_del):
    index = 0
    for row,col in zip([r[0] for r in self.triplet_representation],[r[1] for r in self.triplet_representation]):
      if row == row_del and col == col_del:
        break
      else:
        index += 1
    
    print("Sparse matrix before deletion : ")
    print()
    self.print_sparse()

    length_before_deletion = len(self.triplet_representation)
    self.triplet_representation = self.triplet_representation[:index ] +self.triplet_representation[index + 1:]
    

    print("Sparse matrix after deletion : ")
    print()
    length_after_deletion = len(self.triplet_representation)
    
    if length_before_deletion > length_after_deletion:
        #If an element is deleted , then update the count of non zero elements in triplet representation
        # Decreasing the count of non zero values in sparse matrix
        self.triplet_representation[0][2] -= 1

        #print(self.triplet_representation)
    self.print_sparse()

  def insert(self,row_ins,col_ins,value):
    # Now here we are dynamically handling the size of sparse matrix
    # whenever an new element inserted is out of the bound of sparse matrix we incerement the size of spaerse matrix
    if row_ins  >= self.triplet_representation[0][0] - 1:
      self.triplet_representation[0][0] = row_ins + 1
    if col_ins >= self.triplet_representation[0][1] - 1:
      self.triplet_representation[0][1] = col_ins + 1
    
    print("Sparse matrix before insertion : ")
    self.print_sparse()

    self.triplet_representation.append([row_ins,col_ins,value])
    
    # Increasing the count of non zero values in sparse matrix when an element is inserted
    #self.triplet_representation[0][2] += 1

    print("Sparse matrix after insertion : ")
    self.print_sparse()


if __name__ == "__main__":
    
    flag = 1
    print("#############################################")
    print("Sparse Matrix implementation using Array")
    print("#############################################")
    
    
    while (flag):
        print()
        print()
        print()
        print("Enter one of the following options :")
        print()
        print("Press 1 to Initialize sparse matrix ")
        print("Press 2 to Delete element from sparse matrix ")
        print("Press 3 to Print sparse matrix ")
        print("Press 4 to Insert an element into sparse matrix")
        print("Press 0 to Exit")
        
        choice = int(input())
        
        if choice == 1:
            print("Enter row index elements seperated by spaces (first element corresponds to row size of sparse matrix): ")
            rows =list(map(int,input().strip().split()))
            
            if rows[0] < max(rows[1:]):
                raise Exception ("Invalid Index value , the index value must be lesser than row size of sparse matrix(first element of input list)")
        
            print("Enter columns index elements seperated by spaces (first element corresponds to column size of sparse matrix): ")
            cols =list(map(int,input().strip().split()))
            if cols[0] < max(cols[1:]):
                raise Exception ("Invalid Index value , the index value must be lesser than column size of sparse matrix (first element of input list)")
            
            #Initialisation
            sparse_obj = Sparse(rows,cols)

        elif choice == 2:
            row_del = int(input("Enter the row index of data point to be deleted : "))
            col_del = int(input("Enter the column index of data point to be deleted : "))
            print("Deleting ....")
            sparse_obj.delete(row_del,col_del)
            
        elif choice == 3:
            sparse_obj.print_sparse()
            
        elif choice == 4:
            row_ins = int(input("Enter the row index for data point to be inserted : "))
            col_ins = int(input("Enter the column index for data point to be inserted : "))
            value = int(input("Enter the value to be inserted : "))
            print("Inserting ....")
            sparse_obj.insert(row_ins,col_ins,value)
        elif choice == 0:
            print("Thank You !")
            flag = 0
        else :
            print("! Invalid Input")
