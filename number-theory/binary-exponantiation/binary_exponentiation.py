def binary_exponentiation(a, n):
    if n == 0:
        return 1
    tmp = binary_exponentiation(a, n//2)
    result = tmp * tmp
    if n % 2 == 1:
        result *= a
    return result

def binary_exponentiation_iterative(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a
        a = a * a
        n = n // 2
    return result 


if __name__ == "__main__":
    print(binary_exponentiation(2, 5))
    print(binary_exponentiation_iterative(2, 5))

