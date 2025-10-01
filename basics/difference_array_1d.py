# We need the operations
def operate(diff, l, r, v):
    diff[l] += v
    if r+1 < len(diff):
        diff[r+1] -= v

def diffArray(arr, opr):
    n = len(arr)

    diff = [0 for _ in range(n)]

    for l, r, v in opr:
        operate(diff, l, r, v)

    res = arr[:]
    res[0] += diff[0]
    for i in range(1, n):
        diff[i] += diff[i-1]
        res[i] += diff[i]
    return res

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    opr = [[1, 3, 10], [2, 4, -5]]

    res = diffArray(arr, opr)

    for num in res:
        print(num, end=" ")
    print()
