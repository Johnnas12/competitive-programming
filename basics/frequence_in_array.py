def count_freq(arr):
    '''
    Brute force approach that runs O(n^2) time complexity and O(N) space complexity
    '''
    visited = []
    result = []
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        visited.append(arr[i])
        result.append((arr[i], count))
    return result

def binary_search_left(arr, k):
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == k:
            ans = mid
            right = mid - 1
        elif arr[mid] > k:
            right = mid -1
        else:
            left = mid + 1
    return ans

def binary_search_right(arr, k):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right: 
        mid = (right + left) // 2
        if arr[mid] == k:
            ans = mid
            left = mid + 1
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return ans


def count_freq_binary_search(arr):
    '''
    using Binary Search that assumes sorted array time complexity will be O(nlogn) and space complexity will be O(N)
    '''
    n = len(arr)
    i = 0
    arr.sort()
    result = []
    while i < n:
        first_index = binary_search_left(arr, arr[i])
        last_index = binary_search_right(arr, arr[i])

        freq = last_index - first_index + 1
        result.append([arr[i], freq])
        i = last_index + 1
    return result

def count_freq_hashmap(arr):
    mp = {}
    ans = []

    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    for num, freq in mp.items():
        ans.append([num, freq])
    return mp    


if __name__ == "__main__":
    arr = [10, 20, 10 , 22, 20, 5, 6, 5, 5]
    arr_to_search = [1,2,3,4,5,6,7,8]
    print(count_freq(arr))
    print(count_freq_binary_search(arr))   
    print(count_freq_hashmap(arr))

