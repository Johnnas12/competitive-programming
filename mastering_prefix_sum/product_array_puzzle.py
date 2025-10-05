def product_array_puzzle(arr):
    '''
    To solve this problem we need to use prefix product and product sum, its a little bit tricky question, 
    most of us would think of finding the product of the array elements and returning the result of dividing the product by element at each index, 
    which will introduce multple edge case such as dividing by 0 error

    Here is the best approach:
    1, finding the suffix product
    2, finding the prefix product

    for example: if the given array is
    arr = [10,3,5,6,2]
    the result array would be 
    output = [180, 600, 360, 300, 900]

    The prefix product of the original array would be:
    pre = [10, 130, 150, 900, 1800]
    The suffix product of the original array would be:
    suff = [1800, 180, 60, 12, 2]

    Try to find the pattern between them 🫡
    '''

    n = len(arr)
    pref = list(arr)
    suff = list(arr)
    res = [0] * n

    # Implement Prefix Product 
    for i in range(1, n):
        pref[i] = pref[i] * pref[i-1]

    # Implement Suffix Product
    for i in range(n-2, -1, -1):
        suff[i] = suff[i] * suff[i+1]


    # here is the pattern and the relationship between them
    for i in range(n):
        if i == 0:
            res[i] = suff[i + 1]
        elif i == (n-1):
            res[i] = pref[n-2]
        else:
            res[i] = pref[i - 1] * suff[i + 1]

    return res


if  __name__ == "__main__":
    arr = [10,3,5,6,2]
    print(product_array_puzzle(arr))