def prefix_sum_2d(mat, queries):
    rows = len(mat)
    cols = len(mat[0])

    prefix = [[0] * cols for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            prefix[i][j] = mat[i][j]
            # Adding the left
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            # adding the top
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            # removing overlapping
            if j > 0 and i > 0:
                prefix[i][j] -= prefix[i-1][j-1]

    #initialize my result
    result = []
    
    # declare and assigning top_row, left_col, bottom_row and right_col from query
    for q in queries:
        top_row = q[0]
        left_col = q[1]
        bottom_row = q[2]
        right_col = q[3]
    # total sum we can get
    total = prefix[bottom_row][right_col]
    # top that we remove later
    top = prefix[top_row - 1][right_col]
    # left that we remove later
    left = prefix[bottom_row][left_col - 1]
    # the overlap that we will add from what we removed
    overlap = prefix[top_row -1][left_col - 1]

    # do the operation and append it to our result
    result.append(total - top - left + overlap)

    return result


if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    queries = [
        [1, 1, 2, 2]
    ]
    result = prefix_sum_2d(mat, queries)
    print(result)