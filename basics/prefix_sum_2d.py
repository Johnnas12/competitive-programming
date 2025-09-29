def prefix_sum_2d(arr):
    rows = len(arr)
    cols = len(arr[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j  in range(cols):
            result[i][j] = arr[i][j]

            if i > 0:
                result[i][j] += result[i-1][j]
            if j > 0:
                result[i][j] += result[i][j-1]
            if j > 0 and i > 0:
                result[i][j] -= result[i-1][j-1]
    return result


if __name__ == "__main__":
    arr = [[1,2,3,4],
           [5,6,7,8], 
           [9,10,11,12],
           [13,14,15,16]]
    print(prefix_sum_2d(arr))