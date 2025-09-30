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


'''
Querying sum of submatrices using prefix sum
'''

def query_submatrix_sum(arr, queries):
    rows = len(arr)
    cols = len(arr[0])

    # 1 based indexing
    pre = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            pre[i][j] = arr[i - 1][j - 1] \
                        + pre[i - 1][j] \
                        + pre[i][j - 1] \
                        - pre[i - 1][j - 1]
        result = []

    # process each query using inclusion-exclusion
    for q in queries:
        topRow = q[0] + 1
        leftCol = q[1] + 1
        bottomRow = q[2] + 1
        rightCol = q[3] + 1

        # get total area from (1,1) to (bottomRow, rightCol)
        total = pre[bottomRow][rightCol]

        # subtract area above the submatrix
        top = pre[topRow - 1][rightCol]

        # subtract area to the left of the submatrix
        left = pre[bottomRow][leftCol - 1]

        # add back the overlapping top-left area,
        # which was subtracted twice
        overlap = pre[topRow - 1][leftCol - 1]

        # final submatrix sum using inclusion-exclusion
        result.append(total - top - left + overlap)

    return result
            


if __name__ == "__main__":
    arr = [[1,2,3,4],
           [5,6,7,8], 
           [9,10,11,12],
           [13,14,15,16]]
    print(prefix_sum_2d(arr))

    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    queries = [
        [1, 1, 2, 2]
    ]
    result = query_submatrix_sum(mat, queries)
    print(result)