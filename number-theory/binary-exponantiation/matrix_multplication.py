def mat_mul(A, B):
    row_a, col_a = len(A), len(A[0])
    row_b, col_b = len(B), len(B[0])

    if col_a != row_b:
        raise ValueError(f"Incompatible dimensions: {row_a}x{col_a} cannot be multiplied with {row_b}x{col_b}")

    C = [[0] * col_b for _ in range(row_a)]
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                C[i][j] += A[i][k] * B[k][j]
    return C



if __name__ == '__main__':
    my_a = [[1,2,3], 
            [3,4,5]]
    
    my_b = [[1,3, 2], 
            [4, 5, 6], 
            [1, 2, 3]]
    print(mat_mul(my_a, my_b))


'''
A = [[1,2,3]
    [2,3,4]]
    
B = [[2,3,4]
    [3,2,1]
    [1,1,3]]
'''