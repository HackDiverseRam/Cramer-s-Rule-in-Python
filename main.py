# importing Numpy package 

import numpy as np 

#Makes sure decimal numbers are entered
def trial_and_error(rowCol): 
  try: 
    row_col_input = float(input()) 
    return row_col_input 
  except ValueError: 
    print('Please only input digits') 

class array_from_user: # main matrix class

  loopControl = 0 #counter throughout code 
  #variables for 3x3 matrix 
  Row1Col1 = 0 
  Row1Col2 = 0 
  Row1Col3 = 0 
   
  Row2Col1 = 0 
  Row2Col2 = 0 
  Row2Col3 = 0 
   
  Row3Col1 = 0 
  Row3Col2 = 0 
  Row3Col3 = 0 
   
  #variables for second matrix of knowns 

  row1_col1_second = 0 
  row2_col1_second = 0 
  row3_col1_second = 0 

  detOriginal = 0 
  det_delta_l = 0 
  det_delta_2 = 0 

  det_delta_3 = 0 
  
  original_array = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]]) 
  delta1_array = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]]) 
  delta2_array = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]]) 
  delta3_array = np.array([[0, 0, 0],[0, 0, 0],[0, 0, 0]]) 
  #__init__ is a constructor or start up class that will use ArraySelf as an instance 

  #specification throughout start up 
  def __init__(ArraySelf, row1_col1, row1_col2, row1_col3, row2_col1, 
  row2_col2, row2_col3, row3_col1, row3_col2, row3_col3, second_1, second_2, second_3 ): 
#All assignments of values
    ArraySelf.Row1Col1 = row1_col1 
    ArraySelf.Row1Col2 = row1_col2 
    ArraySelf.Row1Col3 = row1_col3 
     
    ArraySelf.Row2Col1 = row2_col1 
    ArraySelf.Row2Col2 = row2_col2 
    ArraySelf.Row2Col3 = row2_col3 

    ArraySelf.Row3Col1 = row3_col1 
    ArraySelf.Row3Col2 = row3_col2 
    ArraySelf.Row3Col3 = row3_col3 

    ArraySelf.row1_col1_second = second_1 
    ArraySelf.row2_col1_second = second_2 
    ArraySelf.row3_col1_second = second_3
    
    #Displayable Matrix results
    ArraySelf.original_array = np.array([[ArraySelf.Row1Col1, ArraySelf.Row1Col2, ArraySelf.Row1Col3], 
                    [ArraySelf.Row2Col1, ArraySelf.Row2Col2, ArraySelf.Row2Col3], 
                    [ArraySelf.Row3Col1, ArraySelf.Row3Col2, ArraySelf.Row3Col3]]) 
                    
    ArraySelf.delta1_array = np.array([[ArraySelf.row1_col1_second, ArraySelf.Row1Col2, ArraySelf.Row1Col3], 
                    [ArraySelf.row2_col1_second, ArraySelf.Row2Col2, ArraySelf.Row2Col3], 
                    [ArraySelf.row3_col1_second, ArraySelf.Row3Col2, ArraySelf.Row3Col3]]) 

                     

    ArraySelf.delta2_array = np.array([[ArraySelf.Row1Col1, ArraySelf.row1_col1_second, ArraySelf.Row1Col3], 

                    [ArraySelf.Row2Col1, ArraySelf.row2_col1_second, ArraySelf.Row2Col3], 

                    [ArraySelf.Row3Col1, ArraySelf.row3_col1_second, ArraySelf.Row3Col3]]) 

                     
    ArraySelf.delta3_array = np.array([[ArraySelf.Row1Col1, ArraySelf.Row1Col2, ArraySelf.row1_col1_second], 
                    [ArraySelf.Row2Col1, ArraySelf.Row2Col2, ArraySelf.row2_col1_second], 
                    [ArraySelf.Row3Col1, ArraySelf.Row3Col2, ArraySelf.row3_col1_second]]) 
          #Determinants solved           
    ArraySelf.detOriginal = np.linalg.det(ArraySelf.original_array) 
    ArraySelf.det_delta_l = np.linalg.det(ArraySelf.delta1_array) 
    ArraySelf.det_delta_2 = np.linalg.det(ArraySelf.delta2_array) 
    ArraySelf.det_delta_3 = np.linalg.det(ArraySelf.delta3_array) 

     
#Print all values to the user
    print('Cramers Law step by step\nOriginal Array:\n') 
    print(ArraySelf.original_array) 
    print('Determinant:') 
    print(ArraySelf.detOriginal) 

    print('\nDelta 1:\n ') 
    print(ArraySelf.delta1_array) 
    print('Determinant:') 
    print(ArraySelf.det_delta_l) 
     
    print('\nDelta 2:\n ') 
    print(ArraySelf.delta2_array) 
    print('Determinant:') 
    print(ArraySelf.det_delta_2) 

    print('\nDelta 3:\n ') 
    print(ArraySelf.delta3_array) 
    print('Determinant:') 
    print(ArraySelf.det_delta_3) 

    print('\nUnknown variable 1 delta 1 / original ') 
    print(ArraySelf.det_delta_l / ArraySelf.detOriginal) 

    print('\nUnknown variable 2 delta 2 / original ') 
    print(ArraySelf.det_delta_2 / ArraySelf.detOriginal) 

    print('\nUnknown variable 3 delta 3 / original ') 
    print(ArraySelf.det_delta_3 / ArraySelf.detOriginal) 

  #Used to set up original matrix and delta variants so that we  
  #can divide the determinants in the end. 
  #calls to reset the numbers in array 

  def setOriginal(ArraySelf): 
    ArraySelf.original_array = np.array([[Row1Col1, Row1Col2, Row1Col3], 

                    [Row2Col1, Row2Col2, Row2Col3], 

                    [Row3Col1, Row3Col2, Row3Col3]]) 

  def setDelta1(): 
    ArraySelf.delta1_array = np.array([[row1_col1_second, Row1Col2, Row1Col3], 
                    [row2_col1_second, Row2Col2, Row2Col3], 
                    [row3_col1_second, Row3Col2, Row3Col3]]) 

  def setDelta2(): 
    delta2_array = np.array([[Row1Col1, row1_col1_second, Row1Col3], 
                    [Row2Col1, row2_col1_second, Row2Col3], 
                    [Row3Col1, row3_col1_second, Row3Col3]]) 

                
  def setDelta3(): 
    delta3_array = np.array([[Row1Col1, Row1Col2, row1_col1_second], 
                    [Row2Col1, Row2Col2, row2_col1_second], 
                    [Row3Col1, Row3Col2, row3_col1_second]]) 

    return delta3_array 
  # calculating the determinant of matrixes and returns 

  def get_origin_determinant(): 
    return detOriginal 
    
  def get_delta1_determinant(ArraySelf): 
    tempArray = ArraySelf.det_delta_1 
    return tempArray 

  def get_delta2_determinant(): 
    return det_delta_2 

  def get_delta3_determinant(): 
    return det_delta_3 

  #get final results via three functions 

  def first_unknown(): 
    return det_delta_1/detOriginal 

  def second_unknown(): 
    return det_delta_2/detOriginal 

  def third_unknown(): 
    return det_delta_3/detOriginal 

  def get_first_array(): 
    print('Here we enter the 3 x 3 known matrix') 

    loopControl = 0 
    while loopControl < 9: 

      print ('\nEnter Row 1 Column 1') 
      Row1Col1 = trial_and_error(input) 
      loopControl += 1 

      if(loopControl == 1):   
        print ('Enter Row 1 Column 2') 
        Row1Col2 = trial_and_error(input) 
        loopControl += 1 

      if(loopControl == 2):   
        print ('Enter Row 1 Column 3') 
        Row1Col2 = trial_and_error(input) 
        loopControl += 1 

      if(loopControl == 3): 
        print ('\nEnter Row 2 Column 1') 
        Row2Col1 =trial_and_error(input) 
        loopControl += 1 
     
      if(loopControl == 4):    
        print ('Enter Row 2 Column 2') 
        Row2Col2 =trial_and_error(input) 
        loopControl += 1 

      if(loopControl == 5):   
        print ('Enter Row 2 Column 3') 
        Row2Col3 = trial_and_error(input) 
        loopControl += 1 
  
      if(loopControl == 6): 
        print ('\nEnter Row 3 Column 1') 
        Row3Col1 = trial_and_error(input) 
        loopControl += 1 
  
      if(loopControl == 7): 
        print ('Enter Row 3 Column 2') 
        Row3Col2 = trial_and_error(input) 
        loopControl += 1 
       
      if(loopControl == 8): 
        print ('Enter Row 3 Column 3') 
        Row3Col3 = trial_and_error(input) 
        loopControl += 1 
     
  def get_second_array(): 

    loopControl = 0 
    print ('Here we enter the 3 * 1 known matrix') 
    while loopControl < 3: 

      print ('Enter Row 1 Column 1') 
      row1_col1_second = trial_and_error(input) 
      loopControl += 1 
     
      if(loopControl == 1): 
        print ('Enter Row 2 Column 1') 
        row2_col1_second = trial_and_error(input) 

        loopControl += 1 

      if(loopControl == 2): 
        print ('Enter Row 3 Column 1') 
        row3_col1_second = trial_and_error(input) 
        loopControl += 1
   

#main code, this begins the class constructor and sets all values 
#the final 3 values are for the known solutions for cramers 
# the first 9 digits are to fill a 3 x 3 matrix 
user_array = array_from_user(20, 30, 15, 17, 45, 66, 17, 28, 59, 21, 22, 23) 
  
#array_from_user.get_first_array() 
#array_from_user.get_second_array() 
