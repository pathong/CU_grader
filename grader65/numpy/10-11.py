import numpy as np
def get_column_from_bottom_to_top( A, c ):
    return np.flip(A[:, c])
def get_odd_rows( A ):
    return A[1:A.shape[0]:2]
def get_even_column_last_row( A ):
    return A[A.shape[0]-1, :A.shape[1]:2]
def get_diagonal1( A ): # A is a square matrix
    return A[[e for e in range(0,A.shape[0])], [e for e in range(0,A.shape[1])]]
def get_diagonal2( A ): # A is a square matrix
    return A[[e for e in range(0,A.shape[0])], [e for e in range(A.shape[1]-1,-1,-1)]]
exec(input().strip()) 
