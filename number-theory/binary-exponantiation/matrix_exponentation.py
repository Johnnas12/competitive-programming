from matrix_multplication import mat_mul
from identity_matrix import identity_matrix

def matrix_exponentiation(M, expo):
    result = identity_matrix(len(M))

    # lets do our fast exponentiation its really easy
    while expo > 0:
        if expo % 2 == 1:
            result = mat_mul(result, M)
        M = mat_mul(M, M)
        expo //=  2
    return result


if __name__ == "__main__":
   M =  [[1,2,3,],
        [2,3,4], 
        [1,2,5]]
   expo = 3
   print(matrix_exponentiation(M, expo))
