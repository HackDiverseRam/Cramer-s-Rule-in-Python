#For A[] * x[] = B[] with Delta: ∆j equals det(Bj) where column J is
# replaced by B to solve for 3 unknown variables
import numpy as np

Delta = np.array([[20, 30, 15], 
                  [17, 45, 66], 
                  [17, 28, 59]])
                        
Delta1 = np.array([[21, 30, 15], 
                   [22, 45, 66], 
                   [23, 28, 59]])
           
Delta2 = np.array([[20, 21, 15], 
                   [17, 22, 66], 
                   [17, 23, 59]])
                  
Delta3 = np.array([[20, 30, 21], 
                   [17, 45, 22], 
                   [17, 28, 23]])
                   
#Final prints contain the round function, set to 2 and the np.linalg.det() function for determinants
#The resulting divison gives each unknown individually
print('\nUnknown 1: [', round((np.linalg.det(Delta1) / np.linalg.det(Delta)), 2), ']') 
print('\nUnknown 2: [', round((np.linalg.det(Delta2) / np.linalg.det(Delta)), 2), ']')
print('\nUnknown 3: [', round((np.linalg.det(Delta3) / np.linalg.det(Delta)), 2), ']') 