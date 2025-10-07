def longest_sum_of_array(arr, target):
    n = len(arr)
    sum = 0
    umap = {}
    res = 0

    for i in range(n):
        sum += arr[i]

        if sum == target:
            res = max(res, i+1)
        else:
            diff = sum - target
            if diff in umap:
                j = umap[diff]
                res = max(res, i - j )
        if sum not in umap:
            umap[sum] = i
    return res



    

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, -10]
    target = 15
    print(longest_sum_of_array(arr, target))