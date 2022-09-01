##For A[] * x[] = B[] with Delta Division for 3 unkwnowns
#Displayable Matrix results to display what's going on step by step
#Utilizing Array self as the instance as it applies Matrix B column by column into
#Matrix A, giving us Delta Delta 1, 2, 3  
import numpy as np 

class array_from_user: # main matrix class
  def __init__(ArraySelf, r1_c1, r1_c2, r1_c3,#First Array Initializer 
                          r2_c1, r2_c2, r2_c3, 
                          r3_c1, r3_c2, r3_c3, 
                          
                          second_1, second_2, second_3 ):#Second Array Initializer
                          
    ArraySelf.original_array = np.array([[r1_c1, r1_c2, r1_c3], 
                                         [r2_c1, r2_c2, r2_c3], 
                                         [r3_c1, r3_c2, r3_c3]]) 
                    
    ArraySelf.delta1_array = np.array([[second_1, r1_c2, r1_c3], 
                                       [second_2, r2_c2, r2_c3], 
                                       [second_3, r3_c2 ,r3_c3]])
                                       
    ArraySelf.delta2_array = np.array([[r1_c1, second_1, r1_c3], 
                                       [r2_c1, second_2, r2_c3], 
                                       [r3_c1, second_3, r3_c3]]) 

    ArraySelf.delta3_array = np.array([[r1_c1, r1_c2, second_1], 
                                       [r2_c1, r2_c2, second_2], 
                                       [r3_c1, r3_c2, second_3]])
                                       
    #These variables are to add readability to the rest of the code, they are the Determinants
    DeterOrigin = np.linalg.det(ArraySelf.original_array)
    DeterD1 = np.linalg.det(ArraySelf.delta1_array)
    DeterD2 = np.linalg.det(ArraySelf.delta2_array)
    DeterD3 = np.linalg.det(ArraySelf.delta3_array)
    
    #Print all values to the user upon current 
    print('Cramers Law step by step!\nUtilizing A [] X[] = B[] for the unknown\n' ) 
    print('\nDelta Array:', ArraySelf.original_array,'\nDeterminant:', DeterOrigin)
     
    print('\nDelta 1:\n',ArraySelf.delta1_array, 'Determinant:', DeterD1)
    print('\nDelta 2:\n',ArraySelf.delta2_array, 'Determinant:', DeterD2) 
    print('\nDelta 3:\n',ArraySelf.delta3_array, 'Determinant:',DeterD3) 
    
    #Defining final unknowns or x in A[]x[]=B[]
    
    unknown1 = round( (DeterD1 /  DeterOrigin), 2)
    print('\nDelta 1 / Delta =', unknown1) 
    unknown2 = round((DeterD2 / DeterOrigin ), 2)
    print('\nDelta 2 / Delta =', unknown2)
    unknown3 = round(DeterD3 / DeterOrigin), 2)
    print('\nDelta 3 / Delta =', unknown3) 
     
#main code, this simply displays the code via its initializer
#the final 3 values are for the known solutions for cramers 
# the first 9 digits are to fill a 3 x 3 matrix
user_array = array_from_user(20, 30, 15, #First Array
                             17, 45, 66, 
                             17, 28, 59, 

                             21, 22, 23) #Second Array