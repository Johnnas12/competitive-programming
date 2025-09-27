def prefix_sum(arr):
    result = []

    for i in range(len(arr)):
        result.append(sum(arr[:i+1]))
    return result

def prefix_sum_2(arr):
    n = len(arr)
    result = [0] * n

    result[0] = arr[0]

    for i in range(1, n):
        result[i] = result[i - 1] + arr[i]
    return result
    

if __name__ == "__main__":
    arr = [10, 20, 10, 5, 15]
    print(prefix_sum(arr))
    print(prefix_sum_2(arr))