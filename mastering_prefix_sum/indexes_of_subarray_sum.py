def indexes_of_subarray(arr, target):
    n = len(arr)
    umap = {}
    sum = 0

    for i in range(n):
        sum=sum+arr[i]
        extra_sum = sum - target

        # we may have edge cases where we have such as on input [0,0, 1, 4] where the target is 5,
        # so to avoid [2, 4] which normally sounds good but wrong we need the below check

        if extra_sum == 0: # ensure nothing is decreased (we need the whole thing)
            return 1, i + 1 

        # handling the chech and returning 1 bases indexes
        if extra_sum in umap:
            j = umap[extra_sum]
            return j+2, i+1
        
        if sum not in umap:
            umap[sum] = i
    return [-1]




if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    target = 12
    print(indexes_of_subarray(arr, target))
