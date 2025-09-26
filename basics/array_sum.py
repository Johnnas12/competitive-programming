def array_sum(arr):
    '''
    function to sum elements in array (recursive implementation)
    '''
    if len(arr) == 1:
        return arr[0]
    return arr[0] + array_sum(arr[1:])


def array_sum_iteration(arr):
    result = 0
    for element in arr:
        result+=element
    return result

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(array_sum(arr))
    print(array_sum_iteration(arr))