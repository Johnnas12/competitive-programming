def convert(arr):
    '''
    this is a naive approach to solve convert array problem time complexity is O(n^2) and space complexity would be 0(n)
    input: [10,20,15, 12, 11, 50]
    ouput: [0,4,3,2,1,5]
    '''
    # initializing new array of size arr
    new_arr = [0] * len(arr)
    # initialize current position to keep track of the positions in new array
    curr_pos = 0

    # loop through elements to find the minumum element and get its position 
    for i in range(len(arr)):
        idx = -1
        minimun = float("inf")
        for j in range(len(arr)):
            if arr[j] < minimun:
                minimun = arr[j]
                idx=j
        new_arr[idx] = curr_pos
        curr_pos += 1
        # assigning current index value  to make it large number(no longer minimum value) to keep finding the next minimum
        arr[idx] = float("inf")
    return new_arr


def convert_better(arr):
    # creating temporary array and copy over all the elements of original lists
    tmp = [arr[i] for i in range(len(arr))]
    # use builtin sort function
    tmp.sort()
    # creating empty hash table 
    umap = {}
    # initializing the value increases as we go from left to right
    val = 0
    # loop through all elements and increament the val and assign the key(the original number) their order 
    for i in range (len(tmp)):
        umap[tmp[i]] = val
        val += 1

    # maping the hash value to arr it just replacing the values with their rank
    for i in range (len(arr)):
        arr[i] = umap[arr[i]]

    return arr

if __name__ == '__main__':
    arr = [10, 20, 15, 12, 11, 50]
    print(convert(arr))
    test = [10, 20, 15, 12, 11, 50]
    print(convert_better(test))


