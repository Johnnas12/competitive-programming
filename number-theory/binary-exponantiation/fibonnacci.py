from matrix_exponentation import matrix_exponentiation
from matrix_multplication import mat_mul
'''
Implementing fibonnacci sequence in O(logn) instead of implemening in old fashion which is o(n)
'''

# inefficient one using iterative method
def fibonnacci_n(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result[-1] + result[-2]


def fibonnacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci_recursive(n-1) + fibonnacci_recursive(n - 2)


def fibonnacci_optimal(n):
    if n == 1 or n == 0:
        return 1
    M = [[1,1], [1, 0]]
    F = [[1,0], [0,0]]

    result = matrix_exponentiation(M, n-1)
    mat_mul(result, F)

    return result[0][0]
     
if __name__ == "__main__":
    print(fibonnacci_n(10))
    print(fibonnacci_recursive(10))
    print(fibonnacci_optimal(10))
