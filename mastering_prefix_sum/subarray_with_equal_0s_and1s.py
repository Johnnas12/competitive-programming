def countSubarray(arr):
    n = len(arr)
    umap = {0: 1}
    res = 0
    curr_sum = 0

    # Replace 0 with -1
    arr = [-1 if x == 0 else x for x in arr]

    for i in range(n):
        curr_sum += arr[i]
        res += umap.get(curr_sum, 0)
        umap[curr_sum] = umap.get(curr_sum, 0) + 1

    return res


if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 1, 1]
    print(countSubarray(arr))
