def minmax(arr):
    '''
    function to determine maximum and minimum in an array
    '''
    min = float("inf")
    max = float("-inf")
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return min, max

def minmax2(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    print(minmax(arr))
    print(minmax2(arr))