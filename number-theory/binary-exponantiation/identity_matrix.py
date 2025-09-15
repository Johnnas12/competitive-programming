def identity_matrix(n):
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)]

# we can implement in the same way like below too
def identity_matrix_option(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result
    
if __name__ == "__main__":
    # the below options should result in the same way
    print(identity_matrix(3))
    print(identity_matrix_option(3))