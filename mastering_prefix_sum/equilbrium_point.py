def equilbrium_point(arr):
    '''
    Equilbrum state is state of balance in a system where opposing forces or influences are equal,
    this means in array its a point where the left side and right sides are equal

    Implementation: this can be solved using prefix sum and suffix sum the equilbrium point is a point where the suffix sum
    and prefix sum are equal

    Example: original array [1,2, 0, 3]
    prefix sum would be: [1,3,3,6]
    suffix sum would be: [6,5,3,3]

    so on the index 2 two arrays are becoming equal the value is 3

    Time Complexity O(N) and space complexity O(N)
    '''

    # initalize our prefix and suffix sum of the same value of the origina (copy of original)
    pre = list(arr)
    suf = list(arr)
    n = len(arr)

    # implement prefix sum
    for i in range(1, len(arr)):
        pre[i] = pre[i] + pre[i - 1]
    
    # implement suffix sum
    for i in range(n - 2, -1, -1):
        suf[i] = suf[i] + suf[i + 1]


    # finding the equilbrium point
    for i in range(n):
        if pre[i] == suf[i]:
            return i
    return -1


if __name__ == "__main__":
    test_array = [1,2,0,3]
    print(equilbrium_point(test_array))
