from matrix_exponentation import matrix_exponentiation
from matrix_multplication import mat_mul

'''
The below function computes the n-th Padovan number using binary exponentiation.
Its an efficient way to compute terms in the Padovan sequence.
'''

def padovan(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    # Transformation matrix for Padovan sequence
    T = [[0, 1, 1],
         [1, 0, 0],
         [0, 1, 0]]
    # Raise the transformation matrix to the (n-3)th power
    T_n_minus_3 = matrix_exponentiation(T, n - 3)
    # The n-th Padovan number is the sum of the first two elements of the first
    # row of the resulting matrix
    P_n = T_n_minus_3[0][0] + T_n_minus_3[0][1]
    return P_n

if __name__ == "__main__":
    n = 3
    print(f"The {n}-th Padovan number is: {padovan(n)}")

