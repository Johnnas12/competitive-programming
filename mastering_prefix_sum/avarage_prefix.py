def avarage_prefix(arr):
    '''
    This is one of the easy problem: we are aiming to find prefix avarage for the array
    this time with time complexity of O(n) and space complexity O(1)
    '''
    for i in range(1, len(arr)):
        arr[i]+=arr[i-1]

    for i in range(1, len(arr)):
        arr[i] /= (i + 1)
    return arr




if  __name__ == "__main__":
    arr = [10,20,30,40,50]
    print(avarage_prefix(arr))