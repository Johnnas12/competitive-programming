def max_sub_array(arr):
    '''
    Naive approach to solve this problem is brute forcing the array and summing all the subarrays and comparing 
    this approach runs O(N^2) and O(1) space complexity
    '''

    n = len(arr)
    # assuming the first element is maximum
    result = arr[0]

    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += arr[j]
            result = max(currSum, result)

    return result


def max_sub_array_kadane(arr):
    '''
    Optimal solution: using kadane's algorithm time complexity is O(n) and space complexity O(1)
    '''

    n = len(arr)
    max_ending = arr[0]
    res = arr[0]

    for i in range(n):
       max_ending = max(max_ending + arr[i], arr[i])
       res = max(res, max_ending)
    return res
    


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(max_sub_array(arr))
    print(max_sub_array_kadane(arr))